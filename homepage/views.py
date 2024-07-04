from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .models import Vechile, VechileDriver, VechileMaitenance
from .gps import get_devices, get_position, get_details
# Create your views here.


def homepage(request):
    device = get_devices()
    position = get_position()
    vechile = Vechile.objects.all()
    device_data = {

    }

    position_data = {

    }
    for i in device:
        for j in vechile:
            if i['uniqueId'] == j.gps_tracking_no:
                device_data[j.id] = i
    
    for i, j in device_data.items():
        for p in position:
            if j['id'] == p['deviceId']:
                position_data[i] = p

    print(position_data)
                
       
    dist = {
        'vechile':vechile,
        'device':device_data,
        'position':position_data
        }
    
    return render(request, "index.html", dist)


def VechileDetails(request, id, track_no):

    vech = Vechile.objects.get(id = id)
   
    details = get_details(track_no)
    
    print(details)

    dist = {
        'vechile': vech,
        'driver':VechileDriver.objects.filter(using_vehicle = vech).order_by('-id'),
        'maintain':VechileMaitenance.objects.filter(vechile = vech).order_by('-id'),
        'details':details
    }

    return render(request, "vechile.html", dist)

def Login(request):
    template_name = "login.html"
  
  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        use = authenticate(request, username = username, password = password)
        if use is not None:
            login(request, use)
            # return redirect ('/admin/login/?next=/admin/')
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            messages.error(request, "गलत प्रयोगकर्ता नाम वा पासवर्ड")
            return render(request, template_name)
    
    return render(request, template_name)