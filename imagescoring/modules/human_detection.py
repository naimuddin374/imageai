import os 

import cv2
import numpy as np
import imutils

from django.conf import settings 

BASE_DIR = settings.BASE_DIR 

protopath =  os.path.join(BASE_DIR, "artifacts", "MobileNetSSD_deploy.prototxt")
modelpath =  os.path.join(BASE_DIR, "artifacts", "MobileNetSSD_deploy.caffemodel")
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]


try:

    def human_detect(img_path):
        count=0
        image = cv2.imread(img_path)
        image = imutils.resize(image, width=180)

        (H, W) = image.shape[:2]

        blob = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)

        detector.setInput(blob)
        person_detections = detector.forward()
        #print(person_detections.shape)

        for i in np.arange(0, person_detections.shape[2]):
            #print(person_detections.shape[2])
            confidence = person_detections[0, 0, i, 2]
            #print(confidence)
            if confidence > 0.5:
                idx = int(person_detections[0, 0, i, 1])
                #print("idx value is : ",idx)
                if(idx==15):
                    if CLASSES[idx] != "person":

                        continue


                    person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                    #print("Person: ",person_box)
                    (startX, startY, endX, endY) = person_box.astype("int")
                    #print(person_box.shape)
                    count=count+1 # perosn count

                    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
                    break
    
        #Display the output
        return count

except:
    print("Human Detection Problem")
