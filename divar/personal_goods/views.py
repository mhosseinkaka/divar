from django.http.response import HttpResponse

def personal_goods(response):
    return HttpResponse("وسایل شخصی")

def apparel(response):
    return HttpResponse("کیف و کفش و لباس")

def accessories(response):
    return HttpResponse("زیور آلات و اکسسوری")

def beauty(response):
    return HttpResponse("آرایشی و بهداشتی")

def child_apparel(response):
    return HttpResponse("کفش و لباس بچه")

def child_product(response):
    return HttpResponse("وسایل بچه و اسباب بازی")

def stationery(response):
    return HttpResponse("لوازم التحریر")