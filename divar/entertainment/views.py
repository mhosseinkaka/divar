from django.http.response import HttpResponse

def entertainment(response):
    return HttpResponse("سرگرمی و فراغت")

def ticket(response, place):
    return HttpResponse(f"ticket of {place}")

def tour(response, city_name):
    return HttpResponse(f"tours of {city_name}")

def books(response):
    return HttpResponse("کتاب و مجله")

def scoter(response):
    return HttpResponse("دوچرخه و اسکیت و اسکوتر")

def animal(response):
    return HttpResponse("حیوانات")

def music(response):
    return HttpResponse("الات موسیقی")

def sport(response):
    return HttpResponse("وسایل ورزشی")

def toys(response):
    return HttpResponse("اسباب بازی")