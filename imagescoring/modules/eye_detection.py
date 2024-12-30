import cv2
import os
#Face Detection model
from mtcnn.mtcnn import MTCNN
from PIL import Image
import numpy as np
from django.conf import settings 

BASE_DIR = settings.BASE_DIR 
path =  os.path.join(BASE_DIR, "artifacts", "haarcascade_eye_tree_eyeglasses.xml")

eye_cascade = cv2.CascadeClassifier(path)


def eye_detect(img_path,face):
    image = img_path
    eyes = eye_cascade.detectMultiScale(face)
    if len(eyes)>0:
        e=1  # if eyes are visible
        
    else:
        e=0  # if eyes are Invisible

    return e