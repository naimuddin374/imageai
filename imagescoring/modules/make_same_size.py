# import required module
from PIL import Image


def make_same_size(img_path,bg_path):
    # get image
    filepath = img_path
    img = Image.open(filepath)
    # get width and height
    width = img.width
    height = img.height
    print(img.size)

    img1 = Image.open(bg_path)
    print(img1.size)
    img1=img1.resize((width,height))
    print(img1.size)
    img1.save(bg_path)