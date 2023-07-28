from django.db import models

# Create your models
class Doctor(models.Model):
    Name = models.CharField(max_length=45)
    Email = models.EmailField(max_length=40)
    Mobile_No = models.CharField(max_length=11)
    Speciality = models.CharField(max_length=50)

    def __str__(self):
        return  'Dr ' + self.Name

class Patient(models.Model):
    Name = models.CharField(max_length=45)
    Gender = models.CharField(max_length=7)
    Mobile_No = models.CharField(max_length=11)
    address =models.TextField()

    def __str__(self):
        return self.Name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    

