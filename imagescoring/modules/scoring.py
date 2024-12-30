import ast
from dataclasses import asdict
import json
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2
from brisque import BRISQUE
from .human_detection import human_detect
#from face_detection import extract_face
from .eye_detection import eye_detect
from .smile_detection import smile_detect
from mtcnn.mtcnn import MTCNN
from PIL import Image
import numpy as np

def img_scoring(img_path):
    #Face detection
    person={}
    comment=""
    whole_image=cv2.imread(img_path)  


    #Human Detection
    check = human_detect(img_path)
    if check==1:
        try:
            required_size=(512,512)
            # load image from file
            image = Image.open(img_path)
            # convert to RGB, if needed
            image = image.convert('RGB')
            # convert to array
            pixels = np.asarray(image)
            # create the detector, using default weights
            detector = MTCNN()
            # detect faces in the image
            results = detector.detect_faces(pixels)
            # extract the bounding box from the first face
            x1, y1, width, height = results[0]['box']
            # deal with negative pixel index
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
            # extract the face
            face = pixels[y1:y2, x1:x2]
            # resize pixels to the model size
            image = Image.fromarray(face)
            image = image.resize(required_size)
            face_array = np.asarray(image)
            try:
                obj= DeepFace.analyze(face_array,enforce_detection=False)
                emotion=obj['dominant_emotion']
                age=obj['age']
                gender=obj['gender']
                race=obj['dominant_race']
                em_rate=obj['emotion']
                emotional_rate=em_rate['happy']


                #Image Quality Scoring
                obj = BRISQUE(img_path, url=False)
                sc=obj.score()
                score=100-sc
                img_quality_score=score
                #print("Final Image Quality Score: ",score)
                # if(score<=25):
                #     print("Image Quality is Poor")
                # elif(score>25 and score <=50):
                #     print("Image Quality is Not Bad")
                # elif(score>50 and score <=70):
                #     print("Image Quality is Fair") 
                # elif(score>70 and score <=90):
                #     print("Image Quality is Good") 
                # elif(score>90):
                #     print("Image Quality is Excellent") 

                #################### END ####################

                #Eyes Detection
                ed=eye_detect(img_path,face) ##eye detection
                if(ed==1):
                    eye="Visible"
                    e=1
                else:
                    eye="Invisible"
                    e=0


                ######################################


                #Smile Detection

                sm=smile_detect(img_path,face) ##eye detection
                if(sm==1):
                    smile="Visible"
                    s=1
                else:
                    smile="Invisible"
                    s=0

                ######################################

                ####Evaluation
                score=score/2
                emotional_score=emotional_rate*0.1

                if(emotion=="angry"):
                    if(e==0 and s==0):
                        overall_score=score+emotional_score+40
                    elif(e==0 and s==1):
                        overall_score=score+emotional_score+20
                    elif(e==1 and s==0):
                        overall_score=score+emotional_score+40  
                    elif(e==1 and s==1):
                        overall_score=score+emotional_score+15
                
                elif(emotion=="disgust"):
                    if(e==0 and s==0):
                        overall_score=score+emotional_score+40
                    elif(e==0 and s==1):
                        overall_score=score+emotional_score+20
                    elif(e==1 and s==0):
                        overall_score=score+emotional_score+30  
                    elif(e==1 and s==1):
                        overall_score=score+emotional_score+25
                
                elif(emotion=="fear"):
                    if(e==0 and s==0):
                        overall_score=score+emotional_score+40
                    elif(e==0 and s==1):
                        overall_score=score+emotional_score+10
                    elif(e==1 and s==0):
                        overall_score=score+emotional_score+40 
                    elif(e==1 and s==1):
                        overall_score=score+emotional_score+20

                elif(emotion=="happy"):
                    if(e==0 and s==0):
                        overall_score=score+emotional_score+20
                    elif(e==0 and s==1):
                        overall_score=score+emotional_score+40
                    elif(e==1 and s==0):
                        overall_score=score+emotional_score+30
                    elif(e==1 and s==1):
                        overall_score=score+emotional_score+40

                elif(emotion=="sad"):
                    if(e==0 and s==0):
                        overall_score=score+emotional_score+40
                    elif(e==0 and s==1):
                        overall_score=score+emotional_score+15
                    elif(e==1 and s==0):
                        overall_score=score+emotional_score+35
                    elif(e==1 and s==1):
                        overall_score=score+emotional_score+20
                
                elif(emotion=="surprise"):
                    if(e==0 and s==0):
                        overall_score=score+emotional_score+15
                    elif(e==0 and s==1):
                        overall_score=score+emotional_score+40
                    elif(e==1 and s==0):
                        overall_score=score+emotional_score+40
                    elif(e==1 and s==1):
                        overall_score=score+emotional_score+30

                elif(emotion=="neutral"):
                    if(e==0 and s==0):
                        overall_score=score+emotional_score+25
                    elif(e==0 and s==1):
                        overall_score=score+emotional_score+30
                    elif(e==1 and s==0):
                        overall_score=score+emotional_score+40
                    elif(e==1 and s==1):
                        overall_score=score+emotional_score+25
            
        

                
                if(overall_score<=20):
                    comment="Don't bother. Bad concept, bad execution."
                    #print("Don't bother. Bad concept, bad execution.")
                elif(overall_score>20 and overall_score<=40):
                    comment="Bad, there may be promise in the concept, but problems harmed the experience too much"
                    #print("Bad, there may be promise in the concept, but problems harmed the experience too much")
                elif(overall_score>40 and overall_score<=60):
                    comment="Not Bad. Neutral."
                    #print("Not Bad. Neutral.") 
                elif(overall_score>60 and overall_score<=80):
                    comment="Good, You have to work on it."
                    #print("Good, You have to work on it.")
                elif(overall_score>80 and overall_score<=90):
                    comment="Nice, It can be better."
                    #print("Nice, It can be better.")     
                elif(overall_score>90):
                    comment="Great. But Not perfect."
                    #print("Great. But Not perfect.") 

                #Overall details

                person={
                    'emotion':emotion,
                    'Hapiness_rate':emotional_rate,
                    'age':age,
                    'gender':gender,
                    'race':race,
                    'smile':smile,
                    'eye':eye,
                    'img_quality_score':img_quality_score,
                    'Overall_Image_Score':overall_score,
                    'comment':comment

                }
                #print(person)
                ############end##########

                HUMAN={

                    'img_quality_score: '+str(img_quality_score)+'':img_quality_score,
                    'Overall_Image_Score: '+str(overall_score)+'':overall_score,
                    'comment:'+comment+'':comment

                    }
                    
                try:
                    coordinates = (x1-10,y1-10)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 0.5
                    color = (255,0,0)
                    thickness = 2
                    text=json.dumps(HUMAN)
                    image = cv2.putText(whole_image, text, coordinates, font, fontScale, color, thickness, cv2.LINE_4)
                    cv2.rectangle(whole_image, (x1,y1), (x2, y2), (0, 255 , 0), 10)
                    cv2.imwrite(img_path,whole_image)

                except Exception as e:
                    print (e)
        
            except:
                print("Oooopss!!! DEEPFace can't be prperly detetcted from this Image")
                print("Try again with another image")
        except:
            print("Face Detection Failed")
    elif check>1:
        print("Multiple Person object Detected")
        print("Please Try to Upload single Front Faced Image")
    else:
        print("No Person Detected")
        print("Please Try to Upload Image of Human")

    return person

