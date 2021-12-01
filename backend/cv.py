from fer import FER
import cv2
import pprint
from picamera import PiCamera
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def init_cam():
    #sets up Picam, can be altered for normal webcam
    camera = PiCamera()
    camera.resolution = (1024, 768)
    print('Camera initialized')
    return camera

def get_emotion(camera):
    
    result=[]
    faces_rects=[]
    ##repeatedly takes photos and checks each for valid face with expression, can change later for more specificity in selection
    while not np.any(faces_rects):
        camera.capture("/home/pi/fer-21.0.5/tests/sample.jpg")
        image = cv2.imread("/home/pi/fer-21.0.5/tests/sample.jpg")
        test_image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        haar_cascade_face = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')
        faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);
        print('Faces found: ', len(faces_rects))
        #Remainder of code only necessary for visual display of info, if the program only needs to know emotions internally, program can stop here
    for (x,y,w,h) in faces_rects:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    plt.imshow(convertToRGB(image))
    detector = FER()
    result = detector.detect_emotions(image)
    result2 = detector.top_emotion(image)
    bounding_box = result[0]["box"]
    emotions = result[0]["emotions"]
    
    print('got image')
    
    cv2.rectangle(
        image,
        (bounding_box[0], bounding_box[1]),
        (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
        (0, 155, 255),
        2,
    )

    for idx, (emotion, score) in enumerate(emotions.items()):
        color = (211, 211, 211) if score < 0.01 else (0, 255, 0)
        emotion_score = "{}: {}".format(
            emotion, "{:.2f}".format(score) if score > 0.01 else "")
        cv2.putText(
            image,
            emotion_score,
            (bounding_box[0], bounding_box[1] + bounding_box[3] + 30 + idx * 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            1,
            cv2.LINE_AA,
        )
    cv2.imwrite("/home/pi/fer-21.0.5/tests/sample.jpg", image)

    img=Image.open("/home/pi/fer-21.0.5/tests/sample.jpg")
    #img.show() #use for testing purposes, displays imgage w box
    #delete "user data" at end of execution
    os.remove("/home/pi/fer-21.0.5/tests/sample.jpg")
        
    return result2

if __name__ == '__main__':
    camera = init_cam()
    for i in range(3):
        print(get_emotion(camera))
    camera.close()

