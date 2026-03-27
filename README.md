# 🚦 Smart Traffic Analyzer

An AI-powered traffic monitoring system that detects and counts vehicles in real-time using computer vision.

Built with **YOLOv8** and **OpenCV**, this project can analyze video streams or webcam input to estimate traffic density.

---

## 🔥 Features

* 🚗 Detects vehicles (cars, bikes, buses, trucks)
* 📊 Real-time vehicle counting
* 🎥 Works with webcam or video input
* 🟩 Bounding boxes around detected vehicles
* ⚡ Fast and lightweight using YOLOv8

---

## 🛠️ Tech Stack

* Python
* OpenCV
* Ultralytics YOLOv8

---

## 📁 Project Structure

```
smart-traffic-analyzer/
│
├── main.py        # Main script
├── test_yolo.py   #Testing
├── README.md        # Documentation
└── traffic.mp4      # Demo video
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/smart-traffic-analyzer.git
cd smart-traffic-analyzer
```

---

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install ultralytics opencv-python
```

---

## ▶️ How to Run

### Run with webcam:

```
python main.py
```

---

### Run with video file:

1. Download a traffic video
2. Place it in the project folder
3. Update this line in `traffic.py`:

```
cap = cv2.VideoCapture("traffic.mp4")
```

4. Run:

```
python main.py
```

---

## 📸 Demo

Add a screenshot like this:

```
output.png
```

---

## 🧠 How It Works

1. YOLOv8 detects objects in each frame
2. Filters only vehicle classes
3. Draws bounding boxes
4. Counts total vehicles in frame

---

## 🚀 Future Improvements

* 🚦 Lane-wise vehicle counting
* 📊 Traffic density classification (Low / Medium / High)
* 🔁 Object tracking (avoid double counting)
* 🌙 Night-time detection improvements

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## ⭐ Acknowledgements

* Ultralytics YOLOv8
* OpenCV community

---

## 📬 Contact

If you liked this project, give it a ⭐ on GitHub!
