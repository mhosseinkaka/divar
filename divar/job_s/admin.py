from django.contrib.admin import ModelAdmin, register
from job_s.models import Job_detail
# Register your models here.
@register(Job_detail)
class Job_detailAdmin(ModelAdmin):
    list_display = ['title', 'salary', 'place', 'history']