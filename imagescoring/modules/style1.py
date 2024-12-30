import os
import tensorflow as tf
# Load compressed models from tensorflow_hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False
import numpy as np
import PIL.Image
import tensorflow_hub as hub
import base64 
from django.conf import settings 
BASE_DIR = settings.BASE_DIR

hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)

def load_img(path_to_img):
  max_dim = 512
  img = tf.io.read_file(path_to_img)
  img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)

  shape = tf.cast(tf.shape(img)[:-1], tf.float32)
  long_dim = max(shape)
  scale = max_dim / long_dim

  new_shape = tf.cast(shape * scale, tf.int32)

  img = tf.image.resize(img, new_shape)
  img = img[tf.newaxis, :]
  return img


def style1(content_image_path,filter_image_path):
    content_path = content_image_path
    style_path = filter_image_path
    content_image = load_img(content_path)
    style_image = load_img(style_path)
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    edited_image=tensor_to_image(stylized_image)
    filter_image_save = os.path.join(BASE_DIR, "media", "image", content_image_path)
    edited_image.save(filter_image_save)
    image = open(filter_image_save, 'rb') #open binary file in read mode
    image_read = image.read()
    image_64_encode = base64.b64encode(image_read)
    return image_64_encode

