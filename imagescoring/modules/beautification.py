#Face Makeup
import cv2
import numpy as np
import base64
from django.conf import settings 
BASE_DIR = settings.BASE_DIR


def face_whiten(im_bgr, whiten_rate):
    im_hsv = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2HSV)
    im_hsv[:,:,-1] = np.minimum(im_hsv[:,:,-1] * (1 + whiten_rate), 255).astype('uint8')
    im_whiten = cv2.cvtColor(im_hsv, cv2.COLOR_HSV2BGR)
    return im_whiten

def face_smooth(im_bgr, smooth_rate):

    bi_ksize=15
    sigma=100
    ga_ksize=3
    im_bi = cv2.bilateralFilter(im_bgr, bi_ksize, sigma, sigma)
    im_ga = cv2.GaussianBlur(im_bi, (ga_ksize, ga_ksize), 0, 0)
    im_smooth = np.minimum(smooth_rate * im_ga + (1 - smooth_rate) * im_bgr, 255).astype('uint8')
    return im_smooth

def beautification(img_path,whiten_rate,smooth_rate):
    output_image=cv2.imread(img_path)
    output_image=cv2.cvtColor(output_image,cv2.COLOR_BGR2RGB)
    img=face_whiten(output_image,whiten_rate)
    pixels=face_smooth(img,smooth_rate)
    #bg_remove="image_bg_rmv_"+str(round(time_stamp))+".jpg"
    bg_remove=img_path
    cv2.imwrite(bg_remove,pixels)
    current_img = cv2.imread(bg_remove)
    input=cv2.cvtColor(current_img,cv2.COLOR_BGR2RGB)
    cv2.imwrite(bg_remove,input)
    image = open(img_path, 'rb') #open binary file in read mode
    image_read = image.read()
    #image_read = image_read.convert('RGB')
    image_64_encode = base64.b64encode(image_read)
    return image_64_encode