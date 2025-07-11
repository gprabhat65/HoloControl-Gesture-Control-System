# 🖐️ HoloControl: Touchless Brightness and Volume Adjustment

A real-time computer vision-based system that allows users to **adjust brightness and volume using hand gestures**—no physical contact required. Built with **OpenCV**, **MediaPipe**, and **Python**, this project provides an innovative and accessible method for human-computer interaction.

---

## 🚀 Features

- ✋ Hand gesture-based control system
- 💡 Left hand controls screen brightness
- 🔊 Right hand controls system volume
- 📷 Live webcam video processing
- ⚙️ Uses MediaPipe for hand tracking
- 🎯 Smooth interpolation for real-time adjustment
- 💻 Usable in hygiene-sensitive environments (e.g., hospitals, labs)

---

## 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV**
- **MediaPipe**
- **screen_brightness_control** (for brightness)
- **pycaw** (for volume)
- **NumPy**

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gprabhat65/HoloControl-Gesture-Control-System.git
   cd HoloControl-Gesture-Control-System

2. **Install dependencies**
pip install -r requirements.txt

3. **Run the project**
python holo_control.py

🧠 How It Works
The webcam captures the live video stream.

MediaPipe detects hand landmarks in each frame.

Distance between the thumb and index finger is calculated:

Right hand ➜ controls volume using pycaw

Left hand ➜ controls brightness using screen_brightness_control

The distance is mapped to respective control values using linear interpolation.

📚 References
MediaPipe Hands by Google

Pycaw (Python Core Audio Windows Library)

Screen Brightness Control by Crozz

OpenCV Documentation



🙌 Authors
Prabhat Kumar Gupta
Sulav Kumar Shresth
