import cv2
import numpy as np
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk


class FaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Détection et Reconnaissance de Visage")

        self.video_source = 0  # Utilisation de la webcam par défaut
        self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = Label(root)
        self.canvas.pack()

        self.btn_quit = Button(root, text="Quitter", command=self.quit_app)
        self.btn_quit.pack()

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        self.known_face = self.load_known_face("img.jpg")

        self.update_frame()

    def load_known_face(self, image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.equalizeHist(img)
        return img

    def recognize_face(self, detected_face):
        if self.known_face is None:
            return False

        detected_face = cv2.resize(detected_face, (self.known_face.shape[1], self.known_face.shape[0]))
        diff = cv2.absdiff(self.known_face, detected_face)
        score = np.mean(diff)
        return score < 85  # Seuil de reconnaissance (ajuster selon besoin)

    def update_frame(self):
        ret, frame = self.vid.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            gray = cv2.equalizeHist(gray)  # Amélioration du contraste

            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6, minSize=(30, 30))

            for (x, y, w, h) in faces:
                face_region = gray[y:y + h, x:x + w]
                is_recognized = self.recognize_face(face_region)
                color = (0, 255, 0) if is_recognized else (255, 0, 0)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.imgtk = imgtk
            self.canvas.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    def quit_app(self):
        self.vid.release()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectionApp(root)
    root.mainloop()