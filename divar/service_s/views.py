from django.http.response import HttpResponse

# Create your views here.

def service(response):
    return HttpResponse('صفحه خدمات')

def vehicles_services(response):
    return HttpResponse("خدمات ماشین")

def catering_services(response):
    return HttpResponse("خدمات پذیرایی")

def technology_services(response):
    return HttpResponse("خدمات کامپیوتری")

def financial_services(response):
    return HttpResponse("خدمات مالی")

def transport_logistic_services(response):
    return HttpResponse("خدمات حمل و نقل")