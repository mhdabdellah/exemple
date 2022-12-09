# from datetime import timezone
from django.utils import timezone
from django.shortcuts import redirect, render
from myapp.forms import FormVehicule
from django.urls import reverse
from myapp.models import Historique, Vehicule

# Create your views here.

def vehiculedetails(request, id):
    vehicule = Vehicule.objects.get(id=id)
    form = FormVehicule(request.POST or None, instance=vehicule )
    if form.is_valid():
        myformData = form.save()
        print("myformData : "+str(myformData))
        print(vehicule.employee)
        data = {
            'employee' : vehicule.employee,
            'date' : timezone.now(),
            'vehicule': vehicule
        }
        h = Historique()
        h.new_historique(data)
        # print("myformData : "+ myformDate.employee)
        print('saved form')
        return(redirect('/myapp/details/'+str(id)))
    else:
        print("form not valid !")

    context={
      'updateVehiculeForm':form, 
      'vehicule':vehicule,
    }
    return render(request, 'myapp/details.html',context)