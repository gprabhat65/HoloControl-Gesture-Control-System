import cv2
import mediapipe as mp
import numpy as np
from screen_brightness_control import set_brightness
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.75)
mp_draw = mp.solutions.drawing_utils

# Audio setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

def interpolate(val, src_min, src_max, dst_min, dst_max):
    val = max(min(val, src_max), src_min)
    return int((val - src_min) * (dst_max - dst_min) / (src_max - src_min) + dst_min)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label  # 'Left' or 'Right'

            lm_list = hand_landmarks.landmark
            x1, y1 = int(lm_list[4].x * img.shape[1]), int(lm_list[4].y * img.shape[0])   # Thumb
            x2, y2 = int(lm_list[8].x * img.shape[1]), int(lm_list[8].y * img.shape[0])   # Index
            dist = np.hypot(x2 - x1, y2 - y1)

            if label == 'Left':
                brightness = interpolate(dist, 30, 200, 0, 100)
                set_brightness(brightness)
                cv2.putText(img, f'Brightness: {brightness}%', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)

            if label == 'Right':
                vol = interpolate(dist, 30, 200, -65, 0)
                volume.SetMasterVolumeLevel(vol, None)
                cv2.putText(img, f'Volume: {int((vol+65)/65*100)}%', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("HoloControl", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
