from rembg import remove # implemented here
import cv2
import base64
from django.conf import settings 
BASE_DIR = settings.BASE_DIR
  
##ALL in one
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as Img,ImageFilter
from skimage.transform import resize


def change_bg(input_path,bg_path):

    input = cv2.imread(input_path,cv2.IMREAD_UNCHANGED)
    input=cv2.cvtColor(input,cv2.COLOR_BGR2RGB)
    output = remove(input)


    # load and convert background to numpy array and rescale(255 for RBG images)
    RESCALE=255
    background_input = load_img(bg_path)
    background_inp_img = img_to_array(background_input)
    background_inp_img /= RESCALE

    # get dimensions of background (original image will be resized to dimensions of background image in this notebook)
    background_height = background_inp_img.shape[0]
    background_width = background_inp_img.shape[1]
    background_height,background_width
    # resize the image
    resized_rem_back  = resize(output, (background_height,background_width))

    # create a new array which will store the final result
    output_chbg = np.zeros((background_height, background_width, 3))
    output_chbg.shape

    # using the following o[c] = b[c]*(1-i[t])+i[c] {where o - output image, c - channels from 1-3, i - input image with background removed, t - transparent channel}, obtain values for the final result
    output_chbg[:,:,0] = background_inp_img[:,:,0]*(1-resized_rem_back[:,:,3])+resized_rem_back[:,:,0]
    output_chbg[:,:,1] = background_inp_img[:,:,1]*(1-resized_rem_back[:,:,3])+resized_rem_back[:,:,1]
    output_chbg[:,:,2] = background_inp_img[:,:,2]*(1-resized_rem_back[:,:,3])+resized_rem_back[:,:,2]

    bg_chnage=input_path
    output_chbg_scaled = Img.fromarray((output_chbg*RESCALE).astype('uint8'), 'RGB')
    # save the resulting image to colab
    output_chbg_scaled.save(bg_chnage)
    image = open(bg_chnage, 'rb') #open binary file in read mode
    image_read = image.read()
    #image_read = image_read.convert('RGB')
    image_64_encode = base64.b64encode(image_read)
    return image_64_encode




