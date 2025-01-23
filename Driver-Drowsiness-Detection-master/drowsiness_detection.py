import cv2
import numpy as np
import dlib
import random
from imutils import face_utils
from pygame import mixer


mixer.init()
sound = mixer.Sound(r'C:\Drowsiness detection oldd\alarm.wav')

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Drowsiness detection oldd\Driver-Drowsiness-Detection-master\shape_predictor_68_face_landmarks.dat")

sleep = 0
drowsy = 0
active = 0
yawn_count = 0
status = ""
color = (0, 0, 0)
alarm_on = False

heart_rate = 70  
heart_rate_variation = 0

def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    if ratio > 0.25:
        return 2  
    elif ratio > 0.21 and ratio <= 0.25:
        return 1  
    else:
        return 0  

def mouth_aspect_ratio(landmarks):
    A = compute(landmarks[61], landmarks[67])  
    B = compute(landmarks[62], landmarks[66])
    C = compute(landmarks[63], landmarks[65])
    D = compute(landmarks[60], landmarks[64])  
    return (A + B + C) / (3.0 * D)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    face_frame = frame.copy()

    for face in faces:
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44], landmarks[47], landmarks[46], landmarks[45])
        mar = mouth_aspect_ratio(landmarks)

        if left_blink == 0 or right_blink == 0:  
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 6:
                status = "SLEEPING !!!"
                color = (255, 0, 0)
                if not alarm_on:
                    sound.play(-1)
                    alarm_on = True
        elif left_blink == 1 or right_blink == 1:  
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                status = "Drowsy !"
                color = (0, 0, 255)
                if not alarm_on:
                    sound.play(-1)
                    alarm_on = True
        else:  
            drowsy = 0
            sleep = 0
            active += 1
            if active > 6:
                status = "Active :)"
                color = (0, 255, 0)
                if alarm_on:
                    sound.stop()
                    alarm_on = False

        
        if mar > 0.6:
            yawn_count += 1
            status = "Yawning !"
            color = (0, 255, 255)
            if not alarm_on:
                sound.play(-1)
                alarm_on = True
        else:
            yawn_count = 0

        
        heart_rate_variation = random.randint(-2, 2)
        heart_rate += heart_rate_variation
        heart_color = (0, 255, 0) if heart_rate < 80 else (0, 255, 255) if heart_rate <= 100 else (255, 0, 0)

        cv2.putText(frame, f"Heart Rate: {heart_rate} bpm", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, heart_color, 2)
        cv2.putText(frame, status, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        
        for (x, y) in landmarks:
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)

    key = cv2.waitKey(1)
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()
