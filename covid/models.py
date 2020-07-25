from django.db import models

class Hospital(models.Model):
    hospital_name = models.CharField(max_length = 50)
    hospital_addr = models.CharField(max_length = 200)
    hospital_contact = models.CharField(max_length = 15)

class Patient(models.Model):
    patient_name = models.CharField(max_length = 50)
    hospital_name = models.CharField(max_length = 50)
    hospital_addr = models.CharField(max_length = 200, default = ' ')
    