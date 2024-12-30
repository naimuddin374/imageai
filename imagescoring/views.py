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
# from .modules.DALL_E_2 import variant
from .modules.GIF import make_gif
BASE_DIR = settings.BASE_DIR



class Image_Upload(APIView):
    def post(self, request):
        try:
            name=request.data['name']
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            print(pil_image.size)
            filename=name
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "uploaded", filename)
            print(img_path)
            print(pil_image.size)
            pil_image.save(img_path)
            basename=os.path.basename(img_path)

            
            return Response({
                "output_image":basename,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)


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
            
            filename=request.data['name']
            filename1=request.data['name1']
            base64_image=request.data['image']
            print("got images")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            print(filename)
            print(filename1)
            img_path = os.path.join(BASE_DIR, "media", "after_filtering", filename)
            img_path1 = os.path.join(BASE_DIR, "media", "filter", filename1)
            print(img_path)
            print(img_path1)
            pil_image.save(img_path)
            filter_image=style1(img_path,img_path1)
     
            return Response({
                "output_image":filter_image,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)

        
class BG_Remove(APIView):
    def post(self, request):
        try:
            name=request.data['name']
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            filename=name
            print(filename)
            img_path = os.path.join(BASE_DIR, "media","background_remove", filename)
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

#Blur API
class BG_Blur(APIView):
    def post(self, request):
        try:
            name=request.data['name']
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            filename=name
            print(filename)
            img_path = os.path.join(BASE_DIR, "media","background_blur",filename)
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
            filename=request.data['name']
            filename1=request.data['name1']
            base64_image=request.data['image']
            print("got images")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            print(filename)
            print(filename1)
            img_path = os.path.join(BASE_DIR, "media", "background_change", filename)
            img_path1 = os.path.join(BASE_DIR, "media", "background", filename1)
            pil_image.save(img_path)
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
            name=request.data['name']
            base64_image=request.data['image']
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            filename=name
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "face_focused", filename)
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
            #w=0.6 s=0.3
            name=request.data['name']
            base64_image=request.data['image']
            whiten_rate=float(request.data['w'])
            smooth_rate=float(request.data['s'])
            print("got image")
            image_64_decode = base64.b64decode(base64_image)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            filename=name
            print(filename)
            img_path = os.path.join(BASE_DIR, "media", "beautification", filename)
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

class BG_Custom(APIView):
    def post(self, request):
        try:
            name1=request.data['name1']
            name2=request.data['name2']
            base64_image=request.data['image1']
            base64_image1=request.data['image2']
            print("got images")
            image_64_decode = base64.b64decode(base64_image)
            image_64_decode1 = base64.b64decode(base64_image1)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            pil_image1=Image.open(io.BytesIO(image_64_decode1))
            filename=name1
            filename1=name2
            print(filename)
            print(filename1)
            img_path = os.path.join(BASE_DIR, "media", "background_change", filename)
            img_path1 = os.path.join(BASE_DIR, "media", "custom_background", filename1)
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



class Filter_Custom(APIView):
    def post(self, request):
        try:
            name1=request.data['name1']
            name2=request.data['name2']
            base64_image=request.data['image1']
            base64_image1=request.data['image2']
            print("got images")
            image_64_decode = base64.b64decode(base64_image)
            image_64_decode1 = base64.b64decode(base64_image1)
            pil_image=Image.open(io.BytesIO(image_64_decode))
            pil_image1=Image.open(io.BytesIO(image_64_decode1))
            filename=name1
            filename1=name2
            print(filename)
            print(filename1)
            img_path = os.path.join(BASE_DIR, "media", "after_filtering", filename)
            img_path1 = os.path.join(BASE_DIR, "media", "custom_filter", filename1)
            pil_image.save(img_path)
            pil_image1.save(img_path1)
            filter_image=style1(img_path,img_path1)
            
            return Response({
                "output_image":filter_image,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)


# class Variant(APIView):
#     def post(self, request):
#         try:
#             name=request.data['name']
#             base64_image=request.data['image']
#             print("got image")
#             image_64_decode = base64.b64decode(base64_image)
#             pil_image=Image.open(io.BytesIO(image_64_decode))
#             filename=name
#             print(filename)
#             img_path = os.path.join(BASE_DIR, "media","variant_images", filename)
#             print(img_path)
#             pil_image.save(img_path)
#             output=variant(img_path)

#             ##decide the output of variant and resize it real size
#             image_64_decode1 = base64.b64decode(output)
#             pil_image1=Image.open(io.BytesIO(image_64_decode1))
#             pil_image1=pil_image1.resize((pil_image.width,pil_image.height))
#             pil_image1.save(img_path)
            
#             return Response({
#                 "output_image":output,
                
#             },status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return Response({
#                 "output_image":None,
#             },status=status.HTTP_404_NOT_FOUND)

class MAKE_GIF(APIView):
    def post(self, request):
        try:
            input_file=request.data['input_name']
            bg_name=request.data['bg_remove']
            gif=request.data['gif']
            output_gif=request.data['output']
            print("got image")

            filename=input_file
            print(filename)
            input_path = os.path.join(BASE_DIR, "media", "uploaded",filename)
            print("input_path",input_path)

            filename1=bg_name
            print(filename1)
            output_path = os.path.join(BASE_DIR, "media","background_remove", filename1)
            print("output_path",output_path)

            filename2=gif
            print(filename2)
            gif_path = os.path.join(BASE_DIR, "media","gif", filename2)
            print("gif Path",gif_path)

            filename3=output_gif
            print(filename3)
            save_path = os.path.join(BASE_DIR, "media","after_gif", filename3)
            print("save Path",save_path)

            output=make_gif(input_path,output_path,gif_path,save_path)          
            return Response({
                "output_image":output,
                
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "output_image":None,
            },status=status.HTTP_404_NOT_FOUND)
