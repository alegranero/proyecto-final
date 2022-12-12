from django.db import models

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()

def __str__(self): #dunder method - para que cdo haga un print me aparezca el return
      return f"{self.nombre}, {self.numero_pasaporte}, {self.direccion}, {self.id}"

class Dummy(models.Model):
      nombre = models.CharField(max_length=10)


