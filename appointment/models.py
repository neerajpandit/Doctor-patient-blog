from django.db import models
from taskapp.models import User
import datetime
from django.utils.translation import gettext as _

class Appointment(models.Model):

    TIME_SLOT_CHOICES = (
        ('1', '9:00 to 9:45'),
        ('2', '9:45 to 10:30'),
        ('3', '10:30 to 11:15'),
        ('4', '11:15 to 12:00'),
        ('5', '2:00 to 2:45'),
        ('6', '2:45 to 3:30'),
        ('7', '3:30 to 4:15'),
        ('8', '4:15 to 5:00'),
    )

    doctor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'appointment_doctor')
    patient = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'appointment_patient')
    required_speciality = models.CharField(max_length=30)
    date = models.DateField()
    time_slot = models.CharField(max_length = 20, choices = TIME_SLOT_CHOICES )

    def __str__(self):
        return str(self.id)

