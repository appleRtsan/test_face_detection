import os
import numpy as np
import imutils
import mtcnn
import cv2


one_size = 500

def get_data_from_webcam(image,detector):

    faces = detector.detect_faces(image)

    if (len(faces) == 0):
        return None
    left_eye_img = []
    right_eye_img = []
    got_left = False
    got_right = False
    for face in faces:
        x, y, w, h = face['box']
        if w < 50 or h < 25:
            continue
        # roi_face = image[y:y + h, x:x + w]
        # cv2.imshow('face',roi_face)
        # cv2.waitKey(0)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2) #draw face
        for key, value in face['keypoints'].items():
            
            if key == 'left_eye':
                left_eye_img = image[value[1]-25:value[1]+25, value[0]-25:value[0]+25]
                # cv2.imshow('leye',left_eye_img)
                cv2.rectangle(image,(value[0]-25, value[1]-25), (value[0]+25, value[1]+25), (0, 255, 0), 2)
                cv2.circle(image,(value[0], value[1]), 5, (255, 255, 0), -1)
                got_left = True
            elif key == 'right_eye':
                right_eye_img = image[value[1]-25:value[1]+25, value[0]-25:value[0]+25]
                #cv2.imshow('reye',right_eye_img)
                cv2.rectangle(image,(value[0]-25, value[1]-25), (value[0]+25, value[1]+25), (0, 255, 0), 2)
                cv2.circle(image,(value[0], value[1]), 5, (255, 255, 0), -1)
                got_right = True
                break
        
        if not( got_left and got_right):
            return None




def main():
    video_capture = cv2.VideoCapture(0)
    detector = mtcnn.MTCNN()
    while (True):
        _, frame = video_capture.read()
        if not _ :
            break
        frame = imutils.resize(frame, width=500)
        get_data_from_webcam(frame,detector)
        frame = cv2.resize(frame, (one_size, one_size))
        cv2.imshow("gaze point", frame)
        cv2.waitKey(1)


main()