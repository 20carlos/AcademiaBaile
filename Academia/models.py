from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	usuario = models.CharField(max_length=600, blank=True, null=True, unique=True)
	correo = models.CharField(max_length=600, blank=True, null=True, unique=True)
	contraseña = models.CharField(max_length=6000, blank=True, null=True)

	def __str__(self):
		return str ("Usuario: "+(self.usuario)+" "+(self.correo))

class Clase(models.Model):
	nombre = models.CharField(max_length=600)
	horario = models.CharField(max_length=6000, blank=True, null=True)

	def __str__(self):
		return str ("Clase: "+(self.nombre)+" "+(self.horario))

class Alumno(models.Model):
	nombre = models.CharField(max_length=600)
	a_paterno = models.CharField(max_length=600)
	a_materno = models.CharField(max_length=600, blank=True, null=True)
	#correo = models.CharField(max_length=600, blank=True, null=True, unique=True)
	edad = models.IntegerField(default=1, blank=True, null=True)
	clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name="alumno_clase", blank=False, null=False)

	def __str__(self):
		return str ("Alumno: "+(self.nombre)+" "+(self.a_paterno)+" "+str(self.clase))