# face_tracker.py
import cv2
import mediapipe as mp
import math

class FaceTracker:
    def __init__(self):
        self.mp_face = mp.solutions.face_mesh
        self.face_mesh = self.mp_face.FaceMesh(static_image_mode=False)
        self.left_eye = 33   # Landmark for left eye corner
        self.right_eye = 263 # Landmark for right eye corner

    def get_head_turn_angle(self, frame):
        h, w, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            left = landmarks[self.left_eye]
            right = landmarks[self.right_eye]

            dx = (right.x - left.x) * w
            dy = (right.y - left.y) * h
            angle = math.degrees(math.atan2(dy, dx))
            return angle  # Positive = turned right, Negative = turned left
        return 0
