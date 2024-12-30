#Library
from PIL import Image
import base64
from datetime import datetime  
import time 
#Django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
from django.shortcuts import render, redirect
import io

from imagescoring.modules.bg_blur import blur_bg
from imagescoring.modules.bg_change import change_bg 

#Modules
from .modules.scoring import img_scoring
from .modules.style1 import style1
from .modules.bg_remove import remove_bg
from .modules.bg_change import change_bg
from .modules.face_focused import focused_face
from .modules.beautification import beautification
from .modules.make_same_size import make_same_size
BASE_DIR = settings.BASE_DIR



class Score(APIView):
    def post(self, request):
        score=0
        try:
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            #Using for TimeStamp
            time_stamp = time.time()
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d_%m_%Y__time-%H-%M-%S")
            filename="image_"+str(str_date_time)+".jpg"
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "image", filename)
            pil_image.save(img_path)
            obj=img_scoring(img_path)
            print(obj)
            score=obj['Overall_Image_Score']
            comment=obj['comment']
            image_quality_score=obj['img_quality_score']
            return Response({
                "image_quality_score":image_quality_score,
                "image_overall_score": score,
                "comment": comment,
                
            },status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                "image_quality_score":None,
                "image_score": None,
                "comment": None,
            },status=status.HTTP_404_NOT_FOUND)




class Style(APIView):
    def post(self, request):
        try:
            filters={} # create a filter dictionary
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            #Using for TimeStamp
            time_stamp = time.time()
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d_%m_%Y__time-%H-%M-%S")
            filename="image_"+str(str_date_time)+".jpg"
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "image", filename)
            pil_image.save(img_path)
            
            #get the number of filters
            directory = os.path.join(BASE_DIR, "media", "filter")
            lst = os.listdir(directory) # your directory path
            count_files = len(lst)

            #Get filtered images and store
            for i in range(count_files):
                filter_path=os.path.join(BASE_DIR, "media", "filter", "filter"+str(i)+".jpg")
                filter_image=style1(img_path,filter_path)
                filters["filter"+str(i)+""]:filter_image
            return Response(filters,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            directory = os.path.join(BASE_DIR, "media", "filter")
            lst = os.listdir(directory) # your directory path
            count_files = len(lst)
            print (count_files)
            for i in range(count_files):
                filters["filter"+str(i)+""]:None
            return Response(filters,status=status.HTTP_200_OK)
        
class BG_Remove(APIView):
    def post(self, request):
        try:
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            #Using for TimeStamp
            time_stamp = time.time()
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d_%m_%Y__time-%H-%M-%S")
            filename="image_"+str(str_date_time)+".jpg"
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "image", filename)
            print(img_path)
            pil_image.save(img_path)
            output=remove_bg(img_path)
            
            return Response({
                "output_image":output,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)

class BG_Blur(APIView):
    def post(self, request):
        try:
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            #Using for TimeStamp
            time_stamp = time.time()
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d_%m_%Y__time-%H-%M-%S")
            filename="image_"+str(str_date_time)+".jpg"
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "image", filename)
            pil_image.save(img_path)
            output=blur_bg(img_path)
            
            return Response({
                "output_image":output,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)

class BG_Change(APIView):
    def post(self, request):
        try:
            base64_image=request.data['image1']
            base64_image1=request.data['image2']
            print("got images")
            image_64_decode = base64.b64decode(base64_image)
            image_64_decode1 = base64.b64decode(base64_image1)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            pil_image1=Image.open(io.BytesIO(image_64_decode1))
            #Using for TimeStamp
            time_stamp = time.time()
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d_%m_%Y__time-%H-%M-%S")
            filename="image_"+str(str_date_time)+".jpg"
            filename1="bg_"+str(str_date_time)+".jpg"
            print(filename)
            print(filename1)
            img_path = os.path.join(BASE_DIR, "media", "image", filename)
            img_path1 = os.path.join(BASE_DIR, "media", "background", filename1)
            pil_image.save(img_path)
            pil_image1.save(img_path1)
            make_same_size(img_path,img_path1)
            output=change_bg(img_path,img_path1)
            
            return Response({
                "output_image":output,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)


#face focused
class Face_Focused(APIView):
    def post(self, request):
        try:
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            #Using for TimeStamp
            time_stamp = time.time()
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d_%m_%Y__time-%H-%M-%S")
            filename="image_"+str(str_date_time)+".jpg"
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "image", filename)
            pil_image.save(img_path)
            output=focused_face(img_path)
            
            return Response({
                "output_image":output,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)

#image beautification

class Beautification(APIView):
    def post(self, request):
        try:
            base64_image=request.data['image']
            whiten_rate=float(request.data['w'])
            smooth_rate=float(request.data['s'])
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            #Using for TimeStamp
            time_stamp = time.time()
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d_%m_%Y__time-%H-%M-%S")
            filename="image_"+str(str_date_time)+".jpg"
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "image", filename)
            pil_image.save(img_path)
            output=beautification(img_path,whiten_rate,smooth_rate)
            
            return Response({
                "output_image":output,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)