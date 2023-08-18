from django.db import models

# Create your models
class Doctor(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=40)
    mobile_no = models.CharField(max_length=11, null=True, blank=True)
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return    self.name

class Patient(models.Model):
    pname = models.CharField(max_length=45)
    pgender = models.CharField(max_length=7, default="")
    pmobile_no = models.CharField(max_length=11, null=True, blank=True)
    paddress = models.TextField()

    def __str__(self):
        return self.Name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    

