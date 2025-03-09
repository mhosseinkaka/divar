from django.http.response import HttpResponse

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


