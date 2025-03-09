from django.http.response import HttpResponse

def jobs_s(response):
    return HttpResponse("شغل")

def technical(response):
    return HttpResponse("فنی")

def management(response):
    return HttpResponse("مدیریت")

def assistant(response):
    return HttpResponse("مشاور")

