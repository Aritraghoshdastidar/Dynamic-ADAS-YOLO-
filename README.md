# Dynamic ADAS: Real-Time Object Detection with Model Switching

This project implements a **real-time object detection system** for **Advanced Driver Assistance Systems (ADAS)** that dynamically switches between lightweight and heavyweight YOLO models based on system resource availability (CPU and RAM usage).

## 🚗 Project Objective

To optimize object detection performance on **edge devices** (like Jetson Nano, Raspberry Pi) by:
- Using a **lightweight model (YOLOv11S)** when resources are low
- Switching to a **heavyweight model (YOLOv7X)** when resources are available
- Monitoring system stats (CPU/RAM) in real-time using `psutil`

## 🧠 Key Features

- ✅ **Dynamic model switching logic** using `psutil`
- ✅ **Real-time object detection** (cars, pedestrians, traffic objects)
- ✅ **YOLOv7X and YOLOv11S models trained on BDD100K**
- ✅ **Resource monitoring dashboard**
- ✅ Optimized for edge deployment using TensorRT and ONNX Runtime (WIP)

## 📚 Project Requirements

To reproduce or test this project, make sure to have the following:

### 🔸 Dataset

- **[BDD100K](https://bdd-data.berkeley.edu/):**  
  A diverse driving dataset used for training the YOLO models. Download the labeled images (100K) for object detection.

  📥 Download Link: [https://bdd-data.berkeley.edu](https://bdd-data.berkeley.edu)

### 🔸 YOLO Model Repositories

We used official implementations of two YOLO models:

- 🔹 **YOLOv7 (for heavy model)**  
  GitHub: [https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)  
  Used for accurate but resource-heavy inference.

- 🔹 **YOLOv11S (for lightweight model)**  
  GitHub: [https://github.com/WongKinYiu/yolov11](https://github.com/WongKinYiu/yolov11)  
  Used when system resources (CPU/RAM) are constrained.

> Note: Ensure you clone the respective repositories and install all required dependencies as mentioned in their documentation before training or running inference.
>
> 
## 🎥 Demo Video

https://github.com/your-username/dynamic-adas/assets/demo_video.mp4

> 🔽 Click the image to view the demo:

[![Watch the video](media/screenshot1.png)](media/demo_video.mp4)

## 📦 Model Files

Due to GitHub's file size limitations (100MB max per file on the free tier), we could not upload our trained YOLO models (`yolov7x_best.pt` and `yolov11s_best.pt`) to this repository.

> 🔗 If you'd like access to the models for testing, please contact the authors.


## 🛠️ Technologies Used

- Python
- YOLOv7 and YOLOv11S (Ultralytics)
- OpenCV
- psutil
- PyTorch
- TensorRT (planned)
- ONNX Runtime (planned)

## 📈 Future Work

- Integrate GPU-based switching
- Add LiDAR + camera fusion (multimodal)
- Deploy to Jetson Nano / Raspberry Pi and benchmark FPS
- Add alert system (pedestrian crossing, etc.)

## 👨‍💻 Authors

- Aritra Ghosh Dastidar
- Disha Bharadwaj
- Dhatri P Sriram
- Austin

