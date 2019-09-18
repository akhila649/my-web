from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main.html'),
    path('post/<int:pk>/',views.wm_home,name='wm-home.html'),
    path('post/<int:pk>/',views.upload,name='upload.html'),
    path('post/<int:pk>/',views.feedback,name='feedback.html'),

]