from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

import socket

HOST = '192.168.75.103' # Siia tuleb nüüd serveri IP-aadress. Kui server ja klient jooksevad samal masinal, saab kasutada praegust IP-aadressit.
PORT = 65432 # Port peab olema sama nagu serveril.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
response = client_socket.recv(4096).decode()
data = response.split('\r\n\r\n')[0]
print("Received data:")
status = {} 
statusList = data.split(";")
print(statusList)
temp, humidity = statusList[1].split(",")[0], statusList[1].split(",")[1]
tempInt = temp.split(":")[1]
humidityInt = humidity.split(":")[1]
for switch in statusList[0].split(","):
    status[switch.split(":")[0]] = int(switch.split(":")[1])
    print("1")

def switch1(request):
    try: 
        if int(status["led1"]) == 0:
            client_socket.sendall("led-on1".encode())
            status["led1"] = 1
        else:
            client_socket.sendall("led-off1".encode())
            status["led1"] = 0
    except Exception as e:
        print(f"Error sending command: {e}")

    updated_data = {'led1': status['led1']}
    return JsonResponse(updated_data)

def switch2(request):
    try: 
        if int(status["led2"]) == 0:
            client_socket.sendall("led-on2".encode())
            status["led2"] = 1
        else:
            client_socket.sendall("led-off2".encode())
            status["led2"] = 0
    except Exception as e:
        print(f"Error sending command: {e}")
    print(status["led2"])
    updated_data = {'led2': status['led2']}
    return JsonResponse(updated_data)

def switch3(request):
    try: 
        if int(status["led3"]) == 0:
            client_socket.sendall("led-on3".encode())
            status["led3"] = 1
        else:
            client_socket.sendall("led-off3".encode())
            status["led3"] = 0
    except Exception as e:
        print(f"Error sending command: {e}")
    print(status["led3"])
    updated_data = {'led3': status['led3']}
    return JsonResponse(updated_data)

def switch4(request):
    try: 
        if int(status["led4"]) == 0:
            client_socket.sendall("led-on4".encode())
            status["led4"] = 1
        else:
            client_socket.sendall("led-off4".encode())
            status["led4"] = 0  
    except Exception as e:
        print(f"Error sending command: {e}")
    print(status["led4"])
    updated_data = {'led4': status['led4']}
    return JsonResponse(updated_data)

def index(request):
    context = {"url": "http://127.0.0.1:8000/", "switchstatus1": int(status["led1"]), "switchstatus2": int(status["led2"]), "switchstatus3": int(status["led3"]), "switchstatus4": int(status["led4"]), 'temp': tempInt, 'humidity': humidityInt}
    return render(request, 'index.html', context)
