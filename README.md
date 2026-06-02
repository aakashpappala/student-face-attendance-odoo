# 🎓 Student Face Attendance System

AI-Powered Face Recognition Attendance Management System built using **Odoo 19**, **Python**, **OpenCV**, and **InsightFace**.

---

## 📌 Overview

Student Face Attendance System is a custom Odoo 19 module that automates attendance management using facial recognition technology.

The system captures student face samples through a webcam, generates facial embeddings using InsightFace, and automatically marks attendance when a registered student is recognized. This eliminates manual attendance processes and improves accuracy, security, and efficiency.

The project follows a layered architecture consisting of Models, Repositories, Services, AI Components, Configuration Modules, and Utility Components.

---

## 🚀 Features

### Student Management

* Student Registration
* Roll Number Management
* Branch Management
* Academic Year Tracking
* Profile Photo Support

### Face Registration

* Webcam Integration
* Automatic Face Detection
* Multi-Sample Face Capture (20 Images)
* Face Quality Validation
* Face Embedding Generation
* Face Dataset Storage

### AI Recognition Engine

* InsightFace Integration
* Face Embedding Extraction
* Similarity Score Calculation
* Student Identification
* Confidence Score Generation

### Attendance Management

* Session-Based Attendance
* Automatic Attendance Marking
* Duplicate Attendance Prevention
* Attendance History Tracking
* Confidence Score Recording
* Recognition Method Tracking

### Face Analysis

* Face Detection
* Eye Detection
* Face Angle Validation
* Image Quality Assessment
* Anti-Spoofing Framework

### Odoo Integration

* Custom Models
* Form Views
* Tree Views
* Menu Management
* Security Access Control
* PostgreSQL Database Integration

---

## 🎥 Demo Video

Project demonstration video:


https://youtu.be/B38Uye8HAOs



---

## 📸 Screenshots

### Student Registration
<img width="1914" height="958" alt="image" src="https://github.com/user-attachments/assets/b6a97c14-6d35-4cef-a362-9d3a05f5b9ec" />


### Attendance Session
<img width="1905" height="969" alt="image" src="https://github.com/user-attachments/assets/202594c2-0d05-4859-b689-0a1bc5c568ad" />


### Attendance Records

<img width="987" height="404" alt="image" src="https://github.com/user-attachments/assets/13482967-3554-4d23-a5e1-4de9db86fdf6" />


---

## 🏗️ Project Architecture

```text
student_face_attendance/

├── ai/
│   ├── recognition_engine.py
│   ├── similarity_engine.py
│   └── providers/
│
├── config/
├── constants/
├── controllers/
├── data/
├── exceptions/
│
├── models/
│   ├── student.py
│   ├── face.py
│   ├── attendance.py
│   └── attendance_session.py
│
├── repositories/
│   ├── student_repository.py
│   ├── face_repository.py
│   └── attendance_repository.py
│
├── services/
│   ├── face_registration_service.py
│   ├── face_recognition_service.py
│   ├── attendance_service.py
│   ├── attendance_scanner_service.py
│   ├── anti_spoofing_service.py
│   ├── face_detection_service.py
│   ├── eye_detection_service.py
│   ├── quality_assessment_service.py
│   ├── embedding_service.py
│   ├── camera_service.py
│   └── face_angle_service.py
│
├── utils/
├── views/
├── security/
├── __manifest__.py
└── __init__.py
```

---

## ⚙️ Prerequisites

Before running the project, ensure the following software is installed:

* Python 3.12+
* PostgreSQL 15+
* Odoo 19
* Git

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/aakashpappala/student-face-attendance-odoo.git

cd student-face-attendance-odoo
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 AI Dependencies

```bash
pip install insightface

pip install onnxruntime

pip install opencv-python

pip install numpy
```

---

## 🔧 Odoo Configuration

### Step 1: Copy Module

Copy the module into your custom addons directory.

Example:

```text
D:\odoo19\custom_addons\student_face_attendance
```

### Step 2: Update addons_path

In `odoo.conf`:

```ini
addons_path =
D:\odoo19\odoo\addons,
D:\odoo19\custom_addons
```

### Step 3: Start Odoo

```bash
python odoo-bin -d odoo_19 -c ..\odoo.conf
```

### Step 4: Install Module

1. Open Odoo
2. Update Apps List
3. Search for **Student Face Attendance**
4. Install the module

---

## 📖 Usage

### Step 1: Register Student

Create a student record with required details.

### Step 2: Register Face

Open the student record and click **Capture Face**.

The system captures 20 face samples and generates facial embeddings.

### Step 3: Create Attendance Session

Create a new attendance session and activate it.

### Step 4: Scan Attendance

Click **Scan Attendance** to start facial recognition.

### Step 5: Automatic Attendance Marking

When a registered face is recognized, attendance is automatically recorded.

---

## 🔄 System Workflow

```text
Student Registration
        ↓
Face Registration
        ↓
Capture 20 Face Samples
        ↓
Generate Face Embeddings
        ↓
Store Face Dataset
        ↓
Create Attendance Session
        ↓
Scan Attendance
        ↓
Recognize Student Face
        ↓
Mark Attendance Automatically
        ↓
Store Attendance Record
```

---

## 🗄️ Database Models

### Main Models

* student.student
* student.face
* student.attendance
* attendance.session

### Database

* PostgreSQL

---

## 🛠️ Technology Stack

### Backend

* Python
* Odoo 19

### AI & Computer Vision

* OpenCV
* InsightFace
* NumPy
* ONNX Runtime

### Database

* PostgreSQL

### Development Tools

* PyCharm
* Git
* GitHub

---

## 🔮 Future Enhancements

* Continuous Real-Time Attendance Scanning
* Configurable Confidence Threshold
* Advanced Anti-Spoofing Detection
* Attendance Analytics Dashboard
* Excel Export
* Email Notifications
* Multi-Face Recognition
* Real-Time Monitoring

---

## 👨‍💻 Author

**Aakash Pappala**


Python | Odoo | AI Development

---

## ⭐ Support

If you find this project useful, consider giving the repository a star.
