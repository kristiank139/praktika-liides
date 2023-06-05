from django.urls import path
from . import views

urlpatterns = [
    path("liides",  views.index, name="index")
]