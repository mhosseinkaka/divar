from django.http.response import HttpResponse


# Create your views here.
def car(response):
    return HttpResponse("ماشین")

def motorcycle(response):
    return HttpResponse("موتورسیکلت")

def truck(response):
    return HttpResponse("ماشین سنگین")

