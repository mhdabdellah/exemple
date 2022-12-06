from django.shortcuts import redirect, render
from myapp.forms import FormVehicule
from django.urls import reverse
from myapp.models import Vehicule

# Create your views here.

def vehiculedetails(request, id):
    vehicule = Vehicule.objects.get(id=id)
    form = FormVehicule(request.POST or None, instance=vehicule )
    if form.is_valid():
        form.save()
        print('saved form')
    else:
        print("form not valid !")

    context={
      'updateVehiculeForm':form, 
      'vehicule':vehicule,
    }
    return render(request, 'myapp/details.html',context)