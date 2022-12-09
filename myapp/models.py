from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Employee(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    voiture = models.CharField(max_length=255)
    modele = models.CharField(max_length=255)
    valinitial = models.IntegerField(auto_created=True,default=500,null=True)
    valresudiel = models.IntegerField(auto_created=True,default=10,null=True)
    dureeAmortisssement = models.IntegerField(auto_created=True,default=5,null=True)# 5 ans 
    dureePasse = models.IntegerField(default=0,null=True)
    dateAmortissement = models.DateField(null=True) 
    amortissement = models.IntegerField(null=True)
    matercule = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, related_name='employee', on_delete=models.CASCADE, null=True)

    def __str__(self):
        dateCourant = timezone.now()
        anneeCourant = dateCourant.year
        if anneeCourant > self.dateAmortissement.year:
            self.dateAmortissement = dateCourant
            self.dureePasse += 1  # 1 ans 
            if self.dureePasse < self.dureeAmortisssement:
                if self.dureePasse > 0:
                    self.amortissement = (self.valinitial - self.valresudiel) / self.dureePasse
                else: 
                    self.amortissement = self.valinitial
            self.save()
        
        return f"le montant d'amortissement pour la Vehicule {self.voiture} c'est  {self.amortissement} d'apres {self.dureePasse} ans et aujourd'hui c'est le {dateCourant}"
    

class Historique(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return f'''la vehicule {self.vehicule} est utilisée par l'employee 
                    {self.employee} le {self.date}'''

    def new_historique(self, data):
        self.vehicule = data['vehicule']
        self.employee = data['employee']
        self.date = data['date']
        self.save()