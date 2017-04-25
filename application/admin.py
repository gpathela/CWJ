from django.contrib import admin
from application.models import *

# Register your models here.

admin.site.register(ApplicationStatus)
admin.site.register(Application)
admin.site.register(SaveJob)
admin.site.register(Message)