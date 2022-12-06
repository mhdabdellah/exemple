from django.contrib import admin
from .models import Employee, Historique,Vehicule
# Register your models here.

admin.site.register(Employee)
admin.site.register(Vehicule)
admin.site.register(Historique)