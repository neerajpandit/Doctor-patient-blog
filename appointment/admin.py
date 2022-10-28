from django.contrib import admin
from .models import Appointment
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display= ('doctor', 'patient', 'required_speciality', 'date', 'time_slot')

admin.site.register(Appointment, AppointmentAdmin)
