from django.http.response import HttpResponse
# Create your views here.

def makan(response):
    return HttpResponse("املاک")

def makan_sell(response):
    return HttpResponse("فروش")

def makan_edari(response):
    return HttpResponse("اداری")