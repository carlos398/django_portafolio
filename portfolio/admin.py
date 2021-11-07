from django.contrib import admin
from .models import Project

# Register your models here.

admin.site.register(Project) #desde admin ejecutas el modulo site y funcion register y agregas tu modelo