from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from datetime import datetime, timezone
import base64
import numpy as np
import cv2
import uvicorn
from ultralytics import YOLO

# Load YOLOv8l model
yolo_model = YOLO("yolov8l.pt")

# Host token (simple authentication)
HOST_TOKEN = "Hlo"  # Change to a secure value

# FastAPI app setup
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["attendance_db"]
final_logs = db["final_attendance"]

# In-memory attendance cache
attendance_cache = {}

# Data models
class Frame(BaseModel):
    image: str
    user_id: str
    session_id: str

class SessionComplete(BaseModel):
    user_id: str
    session_id: str

# Core detection function
def run_attention_analysis(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = yolo_model(img_rgb, verbose=False)
    boxes = results[0].boxes
    names = results[0].names
    class_ids = boxes.cls.cpu().numpy()
    person_detections = [i for i in class_ids if names[int(i)] == "person"]
    return len(person_detections) > 0

# Endpoint: analyze frame (runs every 5s per client)
@app.post("/analyze")
def analyze(frame: Frame):
    print("📥 Logging for:", frame.user_id, "|", frame.session_id)
    try:
        img_data = base64.b64decode(frame.image.split(",")[1])
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        attentive = run_attention_analysis(img)

        key = f"{frame.user_id}::{frame.session_id}"
        if key not in attendance_cache:
            attendance_cache[key] = {"total": 0, "attentive": 0}

        attendance_cache[key]["total"] += 1
        if attentive:
            attendance_cache[key]["attentive"] += 1

        return {"attentive": attentive}
    except Exception as e:
        return {"error": str(e)}

# Endpoint: get individual user attendance
@app.get("/attendance/{user_id}/{session_id}")
def calculate_attendance(user_id: str, session_id: str):
    print("🔍 Fetching for:", user_id, "|", session_id)
    key = f"{user_id}::{session_id}"
    if key not in attendance_cache:
        return {
            "user_id": user_id,
            "session_id": session_id,
            "total_frames": 0,
            "attentive_frames": 0,
            "attendance_percent": 0.0
        }
    stats = attendance_cache[key]
    percentage = (stats["attentive"] / stats["total"]) * 100 if stats["total"] else 0
    return {
        "user_id": user_id,
        "session_id": session_id,
        "total_frames": stats["total"],
        "attentive_frames": stats["attentive"],
        "attendance_percent": round(percentage, 2)
    }

# Endpoint: host-only - get all users' attendance in a session
@app.get("/attendance/session/{session_id}")
def get_all_attendance(session_id: str, request: Request):
    token = request.query_params.get("token")
    if token != HOST_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized: Host token invalid")
    
    print(f"📊 Host requested all attendance for session: {session_id}")
    session_data = []

    for key, stats in attendance_cache.items():
        user_id, sess_id = key.split("::")
        if sess_id == session_id:
            percentage = (stats["attentive"] / stats["total"]) * 100 if stats["total"] else 0
            session_data.append({
                "user_id": user_id,
                "session_id": session_id,
                "total_frames": stats["total"],
                "attentive_frames": stats["attentive"],
                "attendance_percent": round(percentage, 2)
            })

    return session_data

# Endpoint: finalize and store summary
@app.post("/finalize")
def finalize_session(data: SessionComplete):
    key = f"{data.user_id}::{data.session_id}"
    stats = attendance_cache.get(key)
    if not stats:
        return {"message": "No session data found."}

    percentage = (stats["attentive"] / stats["total"]) * 100 if stats["total"] else 0

    final_logs.insert_one({
        "user_id": data.user_id,
        "session_id": data.session_id,
        "timestamp": datetime.now(timezone.utc),
        "total_frames": stats["total"],
        "attentive_frames": stats["attentive"],
        "attendance_percent": round(percentage, 2)
    })

    del attendance_cache[key]

    return {
        "message": "Final attendance stored.",
        "attendance_percent": round(percentage, 2)
    }

# Start server with HTTPS
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        ssl_certfile=r"E:\MOHAN KUMAR\PROJECTS\connectly\app\ssl\cert.pem",
        ssl_keyfile=r"E:\MOHAN KUMAR\PROJECTS\connectly\app\ssl\key.pem",
        loop="asyncio"
    )
