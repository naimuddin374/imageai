import base64
from PIL import Image
import io

def img_to_encode(img_path):   
    image = open(img_path, 'rb') #open binary file in read mode
    image_read = image.read()
    #image_read = image_read.convert('RGB')
    image_64_encode = base64.b64encode(image_read)
    return image_64_encode

def img_to_decode(base64_image):   
    image_64_decode = base64.b64decode(base64_image)
    pil_image=Image.open(io.BytesIO(image_64_decode))
    return pil_image