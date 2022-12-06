from django.db import models

# Create your models here.

class Employee(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    voiture = models.CharField(max_length=255)
    modele = models.CharField(max_length=255)
    matercule = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, related_name='employee', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.voiture

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