#Library
from PIL import Image
import base64
from datetime import datetime  
import time
import json
#Django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
from django.shortcuts import render, redirect
import io
import requests
from django.core.files.storage import FileSystemStorage
from django.conf import settings
BASE_DIR = settings.BASE_DIR
 
#Uploaded Image's URL
import os
import glob


def home(request):
    return render(request, 'index_1updated.html')
def home1(request):
    return render(request, 'index3.html')

# def clear(request):
#     try:
#         files=[]
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/after_filtering/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/after_gif/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/background_blur/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/background_change/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/background_remove/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/beautification/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/custom_background/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/custom_filter/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/face_focused/*'))
#         files.append(glob.glob('C:/Users/ashik/ticon_projects/imageAI/media/uploaded/*'))
#         for index in range(len(files)):
#             for key in files[index]:
#             # print(index)
#                 print(key)
#                 os.remove(key)

#         data={
#             'message':'Data Clear Successfully'
#         }
#         return render(request, 'index4.html',data)

#     except Exception as e:
#         data={
#             'exception':e,
#             'message':'Data Clear Successfully'
#         }

#         return render(request, 'index4.html',data)