from io import BytesIO
from PIL import Image
import openai
import base64
import urllib.request


##API KEY
openai.api_key = "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"

def variant(img_path):
    # Read the image file from disk and resize it
    image = Image.open(img_path)
    width, height = 256, 256
    image = image.resize((width, height))

    # Convert the image to a BytesIO object
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_array = byte_stream.getvalue()


    try:
        response = openai.Image.create_variation(
        image=byte_array,
        n=1,
        size="256x256"
    )
        print(response['data'][0]['url'])
        image_url = response['data'][0]['url']
        urllib.request.urlretrieve(image_url, img_path)
        image = open(img_path, 'rb') #open binary file in read mode
        image_read = image.read()
        #image_read = image_read.convert('RGB')
        image_64_encode = base64.b64encode(image_read)
        return(image_64_encode)

    except openai.error.OpenAIError as e:

        print(e.http_status)
        print(e.error)
        return None
    