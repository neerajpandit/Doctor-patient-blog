from django import forms
from .models import Appointment

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['required_speciality', 'date', 'time_slot']

        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['time_slot'].queryset = Appointment.objects.none()
        # self.fields['time_slot'].initial = "2"

        # if 'date' in self.data:
        #     try:
        #         date = self.data.get('date')
        #         self.fields['time_slot'].queryset = Appointment.objects.filter(date=date)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['time_slot'].queryset = self.instance.date.time_slot_set.all()
