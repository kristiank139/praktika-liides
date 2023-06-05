from django.shortcuts import render

# Create your views here.

from gpiozero import LED
from time import sleep


led = LED(18)

def index():
    turn_on()
    sleep(1)
    turn_off()
    print("a")

def turn_on():
    led.on()

def turn_off():
    led.off()

index()
