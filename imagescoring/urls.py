from django.urls import path
from .views import *
from . import web_views


urlpatterns = [ 


    #from web_views
    path('web/', web_views.home, name='home'),
    path('test/', web_views.home1, name='home1'),
    # path('clear/', web_views.clear, name='clear'),


    
    
    #from_Views
    path('upload/', Image_Upload.as_view()),
    path('score/', Score.as_view()),
    path('style/', Style.as_view()),
    path('custom-filter/', Filter_Custom.as_view()),
    path('background-remove/', BG_Remove.as_view()),
    path('background-blur/', BG_Blur.as_view()),
    path('background-change/', BG_Change.as_view()),
    path('custom-background/', BG_Custom.as_view()),
    path('face_focused/', Face_Focused.as_view()),
    path('beauty/', Beautification.as_view()),
    # path('variant/', Variant.as_view()),
    path('gif/', MAKE_GIF.as_view()),

    

]