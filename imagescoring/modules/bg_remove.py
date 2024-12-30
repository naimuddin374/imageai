from rembg import remove # implemented here
import cv2
import base64
from django.conf import settings 
BASE_DIR = settings.BASE_DIR

def remove_bg(img_path):
    input = cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
    input=cv2.cvtColor(input,cv2.COLOR_BGR2RGB)
    output = remove(input)
    #bg_remove="image_bg_rmv_"+str(round(time_stamp))+".jpg"
    bg_remove=img_path
    cv2.imwrite(bg_remove,output)
    current_img = cv2.imread(bg_remove)
    input=cv2.cvtColor(current_img,cv2.COLOR_BGR2RGB)
    cv2.imwrite(bg_remove,input)
    image = open(bg_remove, 'rb') #open binary file in read mode
    image_read = image.read()
    #image_read = image_read.convert('RGB')
    image_64_encode = base64.b64encode(image_read)
    return image_64_encode