from mtcnn.mtcnn import MTCNN
from PIL import Image
import numpy as np
import cv2
import base64
from django.conf import settings 
BASE_DIR = settings.BASE_DIR

def focused_face(img_path):

    space=200
    # load image from file
    image = Image.open(img_path)
    # convert to RGB, if needed
    image = image.convert('RGB')
    # convert to array
    pixels = np.asarray(image)
    # create the detector, using default weights
    detector = MTCNN()
    # detect faces in the image
    results = detector.detect_faces(pixels)
    # extract the bounding box from the first face
    x1, y1, width, height = results[0]['box']
    # deal with negative pixel index
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    x1=round(x1-(x1*.20))
    x2=round(x2+(x2*0.20))
    y1=round(y1-(y1*.20))
    y2=round(y2+(y2*.20))
    # extract the face
    face = pixels[y1:y2, x1:x2]
    # resize pixels to the model size
    image = Image.fromarray(face)
    image = image.resize((512,512))
    face_array = np.asarray(image)
    ff=img_path
    cv2.imwrite(ff,face_array)
    current_img = cv2.imread(ff)
    input=cv2.cvtColor(current_img,cv2.COLOR_BGR2RGB)
    cv2.imwrite(ff,input)
    image = open(ff, 'rb') #open binary file in read mode
    image_read = image.read()
    #image_read = image_read.convert('RGB')
    image_64_encode = base64.b64encode(image_read)
    return image_64_encode