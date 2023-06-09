from django.urls import path
from . import views

app_name = "nutimaja"
urlpatterns = [
    path("",  views.index, name="index"),
    path('switch1/', views.switch1, name='switch1'),
    path('switch2/', views.switch2, name='switch2'),
    path('switch3/', views.switch3, name='switch3'),
    path('switch4/', views.switch4, name='switch4'),
    path('garage/', views.garage, name='garage'),
    path('all_light_on/', views.all_lights_on, name='all_lights_on'),
    path('all_lights_off/', views.all_lights_off, name='all_lights_off'),

]
