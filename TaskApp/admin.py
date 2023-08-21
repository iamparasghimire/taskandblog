# myapp/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Task)  
admin.site.register(Blog)  
admin.site.register(Userprofile)  
admin.site.register(Comment)  
