Face Recognition Based Attendance System

A Face Recognition Based Attendance System built using Python, combining image processing, machine learning, and a user-friendly GUI to automate attendance marking with high accuracy. The system captures real-time images, recognizes registered faces, and stores attendance records with date and time in a SQLite database.

🚀 Features

📸 Real-time Face Capture using OpenCV

🧠 Face Recognition using the face_recognition library

🗂 Stores Encoded Face Data using Pickle

🖼 Image Handling using Pillow

🖥 Simple & Clean GUI built with Tkinter

🧾 Automatic Attendance Marking (Name, Date, Time)

🛢 Database Integration using SQLite3

📂 Organized Dataset and Attendance Records

🛠 Tech Stack
Programming Language

Python

Libraries Used

OpenCV – Real-time video capture & image processing

face_recognition – Face detection & encoding

Pillow – Image loading & processing

pickle – Storing face encodings

tkinter – GUI framework

sqlite3 – Backend database

📁 Project Structure (Example)
Face-Recognition-Attendance/

├── main.py          # Main GUI + Logic                                                                                                                                                           
├──  util.py         # Face recognition + GUI helper functions 
├── test.py:         #Spoof detection module 
├── attendance.db    #store data   
├── db(folder):      #store images in pickle(binary format)
└── README.md        # Project documentation


(Your structure may vary — adjust as needed.)

📌 How It Works

User captures face through the camera.

System detects and encodes face using face_recognition.

Encoded data is stored using pickle.

During attendance, the camera scans faces in real time.

When a match is found, the system:

Marks attendance

Stores Name, Date & Time in SQLite3 database

Attendance can be viewed/exported through the GUI.

🖥 GUI Screens

Add New Student / Capture Face

Train / Encode Faces

Mark Attendance (camera-based)

View Attendance Records

Built with Tkinter for easy usage.

📦 Installation
1. Clone the repository
git clone https://github.com/your-username/face-recognition-attendance.git

2. Install dependencies
pip install opencv-python face_recognition pillow

3. Run the project
python main.py

📊 Future Enhancements

🔐 Add login/authentication for admin

🌐 Add cloud database support (Firebase/MySQL)

🚀 Improve accuracy using deep learning models

🤝 Acknowledgment

This project was developed as a practical implementation of face recognition technology using Python. Special thanks to the open-source community behind OpenCV, face_recognition, and Tkinter.
