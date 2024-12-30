from rembg import remove
import cv2
from PIL import Image, ImageSequence
import base64



def make_gif(input_path,output_path,gif_path,save_path):
    animated_gif = Image.open(gif_path)


    input = cv2.imread(input_path,cv2.IMREAD_UNCHANGED)
    #input=cv2.cvtColor(input,cv2.COLOR_BGR2RGB)
    output = remove(input)
    cv2.imwrite(output_path, output)
    im1 = Image.open(output_path)


    transparent_foreground = Image.open(output_path).convert("RGBA")
    frames = []
    for frame in ImageSequence.Iterator(animated_gif):
        frame = frame.copy()
        frame = frame.resize(im1.size)
        frame.paste(transparent_foreground, mask=transparent_foreground)
        frames.append(frame)
    frames[2].save(save_path, save_all=True, append_images=frames[1:])

    image = open(save_path, 'rb') #open binary file in read mode
    image_read = image.read()
    #image_read = image_read.convert('RGB')
    image_64_encode = base64.b64encode(image_read)
    return image_64_encode
