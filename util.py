import os
import pickle

import tkinter as tk
from tkinter import messagebox
import face_recognition


def get_button(window, text, color, command, fg='white'):
    button = tk.Button(
                        window,
                        text=text,
                        activebackground="black",
                        activeforeground="white",
                        fg=fg,
                        bg=color,
                        command=command,
                        height=2,
                        width=20,
                        font=('Helvetica bold', 20)
                    )

    return button


def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label


def get_text_label(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label


def get_entry_text(window):
    inputtxt = tk.Text(window,
                       height=2,
                       width=15, font=("Arial", 32))
    return inputtxt


def msg_box(title, description):
    messagebox.showinfo(title, description)


def recognize(img, db_path):
 
    embeddings_unknown = face_recognition.face_encodings(img)
    if len(embeddings_unknown) == 0:
        return 'no_persons_found'
    else:
        embeddings_unknown = embeddings_unknown[0]

    db_dir = sorted(os.listdir(db_path))
    known_encodings = []
    known_names = []

    for file_name in db_dir:
        path_ = os.path.join(db_path, file_name)
        with open(path_, 'rb') as f:
            embeddings = pickle.load(f)
            known_encodings.append(embeddings)
            known_names.append(file_name[:-7])  

    if not known_encodings:
        return 'no_persons_found'

    face_distances = face_recognition.face_distance(known_encodings, embeddings_unknown)
    best_match_index = face_distances.argmin()
    best_distance = face_distances[best_match_index]

    if best_distance < 0.45:
        return known_names[best_match_index]
    else:
        return 'unknown_person'




import sqlite3
def init_db():
    """Create attendance table if not exists"""
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def insert_attendance(name, timestamp, status):
    """Insert a new attendance record"""
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (name, timestamp, status) VALUES (?, ?, ?)", 
                   (name, str(timestamp), status))
    conn.commit()
    conn.close()
