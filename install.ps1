# ============================================
# RUN as Administrator: Right-click > Run with PowerShell
# ============================================

# Exit on error
$ErrorActionPreference = "Stop"

# Logging helper
function Log {
    param (
        [string]$Level,
        [string]$Message
    )

    $dateNow = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    switch ($Level.ToLower()) {
        "debug"   { Write-Host "$dateNow :: $Message" }
        "warning" { Write-Host "$dateNow :: $Message" -ForegroundColor Yellow }
        "error"   { Write-Host "$dateNow :: $Message" -ForegroundColor Red }
        default   { Write-Host "$dateNow :: $Message" -ForegroundColor Magenta }
    }
}

# -------------------------------------------------------
# Check if run as Administrator
# -------------------------------------------------------
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(`
    [Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Log "warning" "Please run this script as Administrator"
    exit
}

# -------------------------------------------------------
# Copy .env file if not present
# -------------------------------------------------------
$envFile = ".env"
$envTemplate = ".env.template"

if (-not (Test-Path $envFile)) {
    if (Test-Path $envTemplate) {
        Log "info" "Copying .env.template to .env"
        Copy-Item $envTemplate $envFile
    } else {
        Log "error" "Missing .env.template file!"
        exit
    }
}

# -------------------------------------------------------
# Install Node dependencies
# -------------------------------------------------------
if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    Log "error" "npm is not installed. Please install Node.js first: https://nodejs.org/"
    exit
}

Log "info" "Installing Node.js dependencies"
npm install

# -------------------------------------------------------
# Start the server
# -------------------------------------------------------
Log "info" "Starting the server"
npm start
