from django.http.response import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from electronic_devices.serializers import VideoAudioSerializer, E_deviceSerializer, ComputersSerializer, Game_consoleSerializer, TabletSerializer, MobileSerializer
from electronic_devices.models import *

def e_devices(response):
    return HttpResponse("دستگاه های الکترونیکی")

def tablet_mobile(response):
    return HttpResponse("موبایل و تبلت")

def computers(response):
    return HttpResponse("کامپیوتر")

def game_cosoles(response):
    return HttpResponse("کنسول بازی")

def video_audio(response):
    return HttpResponse("صوتی و تصویری")

def telephones(response):
    return HttpResponse("تلفن")


class EdeviceNew(ListCreateAPIView):
    queryset = E_device.objects.all()
    serializer_class = E_deviceSerializer

class TabletNew(ListCreateAPIView):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer

class MobileNew(ListCreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class ComputerNew(ListCreateAPIView):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer

class GameConsolNew(ListCreateAPIView):
    queryset = Game_console.objects.all()
    serializer_class = Game_consoleSerializer

class VideoAudioNew(ListCreateAPIView):
    queryset = Video_audio.objects.all()
    serializer_class = VideoAudioSerializer

class EdeviceNew2(RetrieveUpdateDestroyAPIView):
    queryset = E_device.objects.all()
    serializer_class = E_deviceSerializer

class TabletNew2(RetrieveUpdateDestroyAPIView):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer

class MobileNew2(RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class ComputerNew2(RetrieveUpdateDestroyAPIView):
    queryset = Computers.objects.all()
    serializer_class = ComputersSerializer

class GameConsolNew2(RetrieveUpdateDestroyAPIView):
    queryset = Game_console.objects.all()
    serializer_class = Game_consoleSerializer

class VideoAudioNew2(RetrieveUpdateDestroyAPIView):
    queryset = Video_audio.objects.all()
    serializer_class = VideoAudioSerializer