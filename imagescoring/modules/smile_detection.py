import cv2
import os
#Face Detection model
from mtcnn.mtcnn import MTCNN
from PIL import Image
import numpy as np
from django.conf import settings 


BASE_DIR = settings.BASE_DIR 
path =  os.path.join(BASE_DIR, "artifacts", "haarcascade_smile.xml")
smile =  cv2.CascadeClassifier(path)


def smile_detect(img_path,face): 

    image = img_path
    smiles = smile.detectMultiScale(face)
    if len(smiles)>0:
        s=1  # if eyes are visible
        
    else:
        s=0  # if eyes are Invisible

    return s