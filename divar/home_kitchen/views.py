from django.http.response import HttpResponse

def home_kitchen(response, objects):
    return HttpResponse(f"section {objects}")
