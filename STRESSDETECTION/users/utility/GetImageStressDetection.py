from django.conf import settings
from PyEmotion import *
import cv2 as cv
import numpy as np
class ImageExpressionDetect:
    def getExpression(self,imagepath):
        filepath = settings.MEDIA_ROOT + "\\" + imagepath
        PyEmotion()
        er = DetectFace(device='cpu', gpu_id=0)

        # Open you default camera
        # img = cv.imread('test.jpg')
        # cap = cv.VideoCapture(0)
        # ret, frame = cap.read()

        frame, emotion = er.predict_emotion(cv.imread(filepath))
        cv.imshow('Alex Corporation', frame)
        cv.waitKey(0)
        print("Hola Hi",filepath,"Emotion is ",emotion)
        return emotion

    # def getLiveDetect(self):
    #     print("Streaming Started")
    #     PyEmotion()
    #     er = DetectFace(device='cpu', gpu_id=0)

        # Open you default camera

        # cap = cv.VideoCapture(0)
        # while (True):
        #     ret, frame = cap.read()
        #     frame, emotion = er.predict_emotion(frame)
        #     cv.imshow('Press Q to Exit', frame)
        #     if cv.waitKey(1) & 0xFF == ord('q'):
        #         break
        # cap.release()
        # cv.destroyAllWindows()



    # def getLiveDetect(self):
    #     print("Streaming Started")

    #     cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # 🔥 important on Windows

    #     if not cap.isOpened():
    #         print("Camera not opened")
    #         return

    #     while True:
    #         ret, frame = cap.read()
    #         if not ret:
    #             print("Failed to grab frame")
    #             break
    #         # ---- KEEP DISPLAY FRAME AS uint8 ----
    #         display_frame = frame.copy() 

    #         # ---- CONVERT ONLY FOR MODEL ----
    #         model_frame = frame.astype("float32") / 255.0

    #         # Predict emotion
    #         try:
    #             _, emotion = self.er.predict_emotion(model_frame)
    #         except Exception as e:
    #             print("Prediction error:", e)
    #             emotion = "Detecting..."
    #         # Draw emotion text
    #         cv.putText(
    #         display_frame,
    #         emotion,
    #         (30, 50),
    #         cv.FONT_HERSHEY_SIMPLEX,
    #         1,
    #         (0, 255, 0),
    #         2
    #         )

    #         # SHOW WINDOW
    #         cv.imshow("Live Emotion Detection - Press Q to Exit", display_frame)

    #         # REQUIRED for window refresh
    #         if cv.waitKey(1) & 0xFF == ord('q'):
    #             break

    #     cap.release()
    #     cv.destroyAllWindows()




    def getLiveDetect(self):
        print("Live Camera Started")

        PyEmotion()
        self.er = DetectFace(device='cpu', gpu_id=0)

        cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

        if not cap.isOpened():
            print("Camera not opened")
            return

        # window_name = "Live Emotion Detection (Press Q to Exit)"
        # cv.namedWindow(window_name, cv.WINDOW_NORMAL)

        face_cascade = cv.CascadeClassifier(
            cv.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        while True:
            ret, frame = cap.read()
            if not ret:
                break
             
            # Improve detection (CRITICAL)
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            gray = cv.equalizeHist(gray)

            # ---- FACE DETECTION (OPENCV) ----
            # face_cascade = cv.CascadeClassifier(
            #     cv.data.haarcascades + "haarcascade_frontalface_default.xml"
            # )

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=8,
                minSize=(120, 120)
            )

            # faces, _ = cv.groupRectangles(
            #     list(faces),
            #     groupThreshold=1,
            #     eps=0.2
            # )

            # for (x, y, w, h) in faces:
            if len(faces) > 0:
                x, y, w, h = max(faces, key=lambda f: f[2] * f[3])

                face_img = frame[y:y+h, x:x+w]

                try:
                    _, emotion = self.er.predict_emotion(face_img)
                    if isinstance(emotion, (list, tuple)):
                       emotion = emotion[0]
                except:
                    emotion = "Detecting..."

                # Draw face boxes
                cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
             
            # Draw label
            # cv.rectangle(frame, (20, 10), (420, 70), (0, 0, 0), -1)
                cv.putText(
                    frame,
                    emotion,
                    (x, y - 10),
                    cv.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2
                )

            cv.imshow("Live Emotion Detection (Press Q to Exit)", frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
             
        cap.release()
        cv.destroyAllWindows()


    

