import os
import numpy as np
from PIL import Image
from imutils import face_utils
import imutils
import mtcnn
import cv2


one_size = 500

def get_eye(shape, i, j, image):
    (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
    h_buffer = (100 - h)/2  #set image to 104x104
    w_buffer = (100 - w)/2
    roi = image[int(y - h_buffer) : int(y + h + h_buffer), int(x - w_buffer) : int(x + w_buffer + w) ]
    roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)
    # roa = cv2.resize(roi, (224, 224))
    cv2.rectangle(image, (int( x-w_buffer ), int(y-h_buffer)), (int(x + w_buffer + w), int(y + h + h_buffer)), (0, 255, 0), 2)
    return roi


def get_data_from_webcam(image):

    detector = mtcnn.MTCNN()
    faces = detector.detect_faces(image)

    if (len(faces) == 0):
        print("?")
        return None
    left_eye_img = []
    right_eye_img = []
    for face in faces:
        x, y, w, h = face['box']
        roi_face = image[y:y + h, x:x + w]
        cv2.imshow('face',roi_face)
        cv2.waitKey(0)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) #draw face
        # got_left = False
        # got_right = False
        # for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items(): #detecting eyes in range of face
        #     if (got_right and got_left):
        #         break
        #     if(name == 'right_eye'):
        #         right_eye_img = get_eye(shape, i, j, image)
        #         got_right = True
        #     elif(name == 'left_eye'):
        #         left_eye_img = get_eye(shape, i, j, image)
        #         got_left = True




def main():
    video_capture = cv2.VideoCapture(0)
    none_counter = 0
    while (True):
        _, frame = video_capture.read()
        frame = imutils.resize(frame, width=500)
        get_data_from_webcam(frame)
        frame = cv2.resize(frame, (one_size, one_size))
        cv2.imshow("gaze point", frame)
        cv2.waitKey(1)


main()