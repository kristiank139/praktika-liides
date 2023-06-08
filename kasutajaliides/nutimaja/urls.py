from django.urls import path
from . import views

app_name = "nutimaja"
urlpatterns = [
    path("",  views.index, name="index"),
    path('switch1/', views.switch1, name='switch1'),
    path('switch2/', views.switch2, name='switch2'),
    path('switch3/', views.switch3, name='switch3'),
    path('switch4/', views.switch4, name='switch4'),

]
