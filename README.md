# Tracking Students

This is a part of the 2023 startup project by a group consisting of four members: Dat Nguyen Tien, Nguyen Truong Phuc, Nguyen Thanh Tu, and Luyen Thanh Binh, under the guidance of Prof. Pham Minh Chuan. The project deals with the issue of managing students during examinations. Specifically, this section of code manages students within the examination room. Its task is to supervise, monitor, and detect any cheating candidates through facial recognition attendance. The detailed code segment is provided below.

## Contents
1. [Introduction](#introduction)
2. [Results](#results)
3. [Installation](#installation)
4. [Quick Start Overview](#quick-start-overview)
5. [Structures](#structures)
6. [Send Us Feedback!](#send-us-feedback)
7. [Thanks](#thanks)
8. [License](#license)


## Introduction
### Face Recognition
<p align="center">
    <img src="github/images_introduction/FaceRecognition.jpg" width="360">
</p>

Facial recognition is a rapidly developing technology that has attracted much attention in recent years. This technology involves automatically identifying and verifying individuals based on their facial features. It relies on collecting, analyzing, and comparing unique facial characteristics, such as the distance between the eyes and the shape of the nose.

With the use of deep learning algorithms, facial recognition systems have become highly accurate and are applied in various fields, including security, access control, and even on social media platforms. Implementing this system in examinations and education is an essential necessity. This system helps control and identify candidates within the examination room. It extracts facial information and, upon completion, exports it to Excel for cross-referencing when needed.

### Counting Students
<p align="center">
    <img src="github/images_introduction/tracking_people.jpg" width="360">
</p>
Alongside facial recognition technology, the technology for monitoring students during examinations has also seen significant advancements. This technology employs one of the most modern AI models available today. The system automatically captures and sends images to Telegram every 5 minutes, enabling educators to monitor student entries and exits while recording the timing of these movements with real-time results every 10 seconds.

By combining both machine learning and deep learning algorithms, the system for monitoring candidates is becoming increasingly accurate. Its application is gaining trust among people and expanding widely in both daily life and professional settings.

### Tracking People
<p align="center">
    <img src="github/images_introduction/cheating.jpg" width="360">
</p>
Another field that is rapidly developing and showing even greater potential in the future is the detection of cheating among candidates using AI. When operational, this system marks and captures images if it detects any anomalies or violations, sending them to Telegram for verification of the misconduct. The reliability of this system is currently at a credible level and is undergoing further development and testing.

This deep learning-based system is being applied in developed countries worldwide such as the UK, France, the USA, and various Asian countries like Japan, South Korea, among others. It is being implemented in collaboration with examination invigilators to achieve the highest effectiveness and ensure the utmost fairness in examinations.

# Results
### Counting Students (using Yolov8 )
<p align="center">
    <img src="/github/media/4104207604824701910.gif" width="1000">
    <br>
    <sup>Testing with 12422TN class <a href="https://github.com/ultralytics/ultralytics" target="_blank"><i> on Yolov8 </i></a>
</p>

### Cheating Recognition ( using OpenPose)
<p align="center">
    <img src="/github/media/5533218175348215452.gif" width="1000">
    <br>
    <sup>Testing with 12422TN class <a href="https://github.com/CMU-Perceptual-Computing-Lab/openpose" target="_blank"><i> on OpenPose </i></a>
</p>

# Installation

### With Python Base
1. Install dependences library
 ```bash
 pip install -r setup.txt
```
2. Install dependences files
After you must run ``` file_requirements.py ``` or
 ``` bash
python file_requirements.py
```
3. Install dependences files with other steps ( Optional )
- If you step 2 not successfully you can download weights from [Google Drive](https://drive.google.com/drive/folders/1Y4coXLsVzCXYuCKpyDfQBqpHH8Aj-Yg5?usp=sharing)
- Move folder ```graph_models``` downloaded to ```Pose\graph_models``` and copy folder you downloaded to```src\Pose\graph_models```\
- Paste file in folder ```Face-Recognition\Models``` you downloaded to ```Models``` in main

### With Anaconda 
1. Install dependences library
   - You can load dependences library with ``` env.yaml``` file.
   - You can find ```env.yaml``` file in folder ```Anaconda```
2. Install dependences files
After you must run ``` file_requirements.py ``` or
 ``` bash
python file_requirements.py
```
3. Install dependences files with other steps ( Optional )
- If you step 2 not successfully you can download weights from [Google Drive](https://drive.google.com/drive/folders/1Y4coXLsVzCXYuCKpyDfQBqpHH8Aj-Yg5?usp=sharing)
- Move folder ```graph_models``` downloaded to ```Pose\graph_models``` and copy folder you downloaded to```src\Pose\graph_models```\
- Paste all file in folder ```Face-Recognition\Models``` you downloaded to ```Models``` in main

### With Docker
You can build docker images with my docker file.
1. Build docker images
In folder ```main``` of this project open command prompt and run
``` bash
docker build -t [names_you_choose] .
Example: docker build -t nguyendat135/trackingstudents .
```

# Quick Start Overview
### With Python Base Environments and Anaconda Environment
1. Quick Run
You can run this file ```app.py``` to start this project. Input if login  ```username:abc``` and ```password:abc``` to login
The IP and Port you can access is ```http://localhost:8080/``` or with other laptop or smartphone in same network is ```http://192.168.1.44:8080```
2. To trainning model you read ```Hướng dẫn sử dụng``` in tab ```Tổng quan```

### With Docker
1. Quick Run
You access this project with this command
```bash
docker run -p 8080:8080 [name_you_choose in Installation]
```
Example: docker run -p 8080:8080 nguyendat135/trackingstudents
2. After you can access it with ```http://localhost:8080/``` or with other laptop or smartphone in same network is ```http://192.168.1.44:8080```
3. To trainning model you read ```Hướng dẫn sử dụng``` in tab ```Tổng quan```
# Structures
``` bash
Tracking_Students
+---.idea
¦   +---inspectionProfiles
+---Action
¦   +---training
¦   +---__pycache__
+---Auth
¦   +---__pycache__
+---Dataset
¦   +---FaceData
+---graph_models
¦   +---mobilenet_thin
¦   +---VGG_origin
+---Models
+---Pose
¦   +---graph_models
¦   ¦   +---mobilenet_thin
¦   ¦   +---VGG_origin
¦   +---__pycache__
+---profile_detection
¦   +---haarcascades
¦   +---__pycache__
+---src
¦   +---Action
¦   ¦   +---training
¦   ¦   +---__pycache__
¦   +---align
¦   ¦   +---__pycache__
¦   +---Auth
¦   ¦   +---__pycache__
¦   +---FCRN
¦   +---generative
¦   ¦   +---models
¦   +---models
¦   +---Pose
¦   ¦   +---graph_models
¦   ¦   ¦   +---mobilenet_thin
¦   ¦   ¦   +---VGG_origin
¦   ¦   +---__pycache__
¦   +---QSTP
¦   +---SoNguoi
¦   +---Tracking
¦   ¦   +---deep_sort
¦   ¦   ¦   +---__pycache__
¦   ¦   +---graph_model
¦   ¦   +---__pycache__
¦   +---ViPham
¦   +---__pycache__
+---test
+---test_out
+---Tracking
¦   +---deep_sort
¦   ¦   +---__pycache__
¦   +---graph_model
¦   +---__pycache__
+---trained
+---ViPham
+---__pycache__
```

# Send Us FeedBack
Our project is open source for research purposes, and we want to improve it! So let us know (create a new GitHub issue or pull request, email us, etc.) if you...
1. Find/fix any bug (in functionality or speed) or know how to speed up or improve any part of Students Tracking.
2. Want to add/show some cool functionality/demo/project made on top of Students Tracking. We can add your project link to your [Issue](https://github.com/datnguyen-tien204/Tracking_Students/issues)

# Thanks
Thank you for the guidance of Prof. Minh Chuan Pham in the process of creating this project, as well as the evaluation board consisting of Prof. Quoc Viet Hoang and Prof. Dinh Chien Nguyen, who helped us improve the results and provided feedback for this project.

# License
This project is freely available for free non-commercial use. If it useful you can give 1 star. Thanks for using.
