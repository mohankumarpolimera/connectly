'use strict';

const packageJson = require('../../package.json');

module.exports = {
    // Branding and customizations require a license: https://codecanyon.net/item/Connectly-p2p-webrtc-realtime-video-conferences/38376661
    brand: {
        app: {
            language: 'en', // https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
            name: 'Connectly',
            title: '<h1>Connectly</h1>Free browser based Real-time video calls.<br />Simple, Secure, Fast.',
            description:
                'Begin your next video call with just one click. No downloads, plug-ins, or logins needed. Jump right into talking, messaging, and screen sharing.',
            joinDescription: 'Choose a room name.<br />How about this one?',
            joinButtonLabel: 'JOIN ROOM',
            joinLastLabel: 'Your recent room:',
        },
        og: {
            type: 'app-webrtc',
            siteName: 'Connectly',
            title: 'Click the link to start a call.',
            description:
                'Connectly calling offers real-time HD quality and low latency, a step up from traditional tech.',
            image: 'https://p2p.Connectly.com/images/preview.png',
            url: 'https://p2p.Connectly.com',
        },
        site: {
            shortcutIcon: '../images/logo.svg',
            appleTouchIcon: '../images/logo.svg',
            landingTitle: 'Connectly: Free Secure Video Calls, Chat & Screen Sharing.',
            newCallTitle: 'Connectly: Free Secure Video Calls, Chat & Screen Sharing.',
            newCallRoomTitle: 'Choose a name. <br />Share the URL. <br />Begin your conference.',
            newCallRoomDescription:
                "Every room gets a unique, disposable URL. Simply choose a room name, share your custom link, and you're set. It's that simple.",
            loginTitle: 'Connectly - Host Protected Login Required.',
            clientTitle: 'Connectly WebRTC: Video Calls, Chat Rooms & Screen Sharing.',
            privacyPolicyTitle: 'Connectly - Privacy and Policy.',
            stunTurnTitle: 'Test Stun/Turn Servers.',
            notFoundTitle: 'Connectly - 404 Page Not Found.',
        },
        html: {
            features: true,
            browsers: true,
            teams: true, // please keep me always true ;)
            tryEasier: true,
            poweredBy: true,
            sponsors: false,
            advertisers: true,
            footer: false,
        },
    },
    /**
     * Configuration for controlling the visibility of buttons in the MiroTalk P2P client.
     * Set properties to true to show the corresponding buttons, or false to hide them.
     * captionBtn, showSwapCameraBtn, showScreenShareBtn, showFullScreenBtn, showVideoPipBtn, showDocumentPipBtn -> (auto-detected).
     */
    buttons: {
        main: {
            showShareQr: true,
            showShareRoomBtn: true, // For guests
            showHideMeBtn: true,
            showAudioBtn: true,
            showVideoBtn: true,
            showScreenBtn: true, // autodetected
            showRecordStreamBtn: true,
            showChatRoomBtn: true,
            showCaptionRoomBtn: true,
            showRoomEmojiPickerBtn: true,
            showMyHandBtn: true,
            showWhiteboardBtn: true,
            showSnapshotRoomBtn: true,
            showFileShareBtn: true,
            showDocumentPipBtn: true,
            showMySettingsBtn: true,
            showAboutBtn: true, // Please keep me always true, Thank you!
        },
        chat: {
            showTogglePinBtn: true,
            showMaxBtn: true,
            showSaveMessageBtn: true,
            showMarkDownBtn: true,
            showChatGPTBtn: true,
            showFileShareBtn: true,
            showShareVideoAudioBtn: true,
            showParticipantsBtn: true,
        },
        caption: {
            showTogglePinBtn: true,
            showMaxBtn: true,
        },
        settings: {
            showMicOptionsBtn: true,
            showTabRoomPeerName: true,
            showTabRoomParticipants: true,
            showTabRoomSecurity: true,
            showTabEmailInvitation: true,
            showCaptionEveryoneBtn: true,
            showMuteEveryoneBtn: true,
            showHideEveryoneBtn: true,
            showEjectEveryoneBtn: true,
            showLockRoomBtn: true,
            showUnlockRoomBtn: true,
            showShortcutsBtn: true,
        },
        remote: {
            showAudioVolume: true,
            audioBtnClickAllowed: true,
            videoBtnClickAllowed: true,
            showVideoPipBtn: true,
            showKickOutBtn: true,
            showSnapShotBtn: true,
            showFileShareBtn: true,
            showShareVideoAudioBtn: true,
            showPrivateMessageBtn: true,
            showZoomInOutBtn: false,
            showVideoFocusBtn: true,
        },
        local: {
            showVideoPipBtn: true,
            showSnapShotBtn: true,
            showVideoCircleBtn: true,
            showZoomInOutBtn: false,
        },
        whiteboard: {
            whiteboardLockBtn: false,
        },
    },
};
