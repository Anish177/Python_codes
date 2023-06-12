from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'fish_information/index.html')

def temp(request):

    api = 'https://api.init.st/data/v1/events/latest?accessKey=ist_6jxPkB-hjd9Iv2qkz5hzoxjhwwD9tUf-&bucketKey=piot_temp_stream031815'
    values = requests.get(api)
    value = values.json()['temperature (C)']['value']

    context = {
        'temperature': value,
    }
    return render(request, 'fish_information/temp.html', context)

def ph(request):
    return render(request, 'fish_information/ph.html')

def detection(request):
    return render(request, 'fish_information/detection.html')