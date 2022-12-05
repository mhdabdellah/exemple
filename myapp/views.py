from django.shortcuts import redirect, render
from myapp.forms import FormVehicule
from django.urls import reverse
from myapp.models import Vehicule

# Create your views here.

def vehiculedetails(request, vehicule_id):
    vehicule = Vehicule.objects.get(id = vehicule_id)
   
    if request.method=="POST":
        # vehicule = Vehicule.objects.get(id = id)
        form = FormVehicule(request.POST or None, instance=vehicule )
        if form.is_valid():
            form.save()
            return redirect(reverse('myapp:details'))
    else:
        form=FormVehicule()

    context={
      'updateVehiculeForm':form, 
      'vehicule':vehicule,
    #   'vehiculeDetail': vehiculeDetail
    }
    return render(request, 'myapp/details.html',context)