from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from taskapp import views
from taskapp.models import User,Doctor
from .forms import AppointmentForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Appointment
import datetime
from . import models
from django.http import JsonResponse


# def DoctorListView(request):
#     doctors=models.Doctor.objects.all()
#     mydict={
#     'doctors':doctors, 
#     }
#     return render(request,'taskapp/doctor_list.html',context=mydict)

class DoctorListView(ListView):
     model = User
     #model = Doctor
#     # model={
#     # 'Doctor':Doctor,
#     # 'User':User 
#     # }
     template_name = 'taskapp/doctor_list.html'
     context_object_name = 'doctorlist'

     def get_queryset(self):
         return User.objects.filter()

class AppointmentCreateView(CreateView):
    template_name = 'taskapp/appointment_create.html'
    form_class = AppointmentForm
    context_object_name = 'doctor_id'
    # initial = {"time_slot": "2"}

    def form_valid(self, form):
        form.instance.doctor = User.objects.get(id=self.kwargs['doctor_id'])
        form.instance.patient = self.request.user
        return super(AppointmentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('appointment:appointment_detail_view', kwargs={'id':self.object.id})

    def get_context_data(self, **kwargs):
        kwargs = super(AppointmentCreateView, self).get_context_data(**kwargs)
        kwargs['doctor_id'] = self.kwargs.get('doctor_id')
        return kwargs

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'taskapp/appointment_detail.html'
    context_object_name = 'appointment'
    slug_field = 'id'
    slug_url_kwarg = 'id'

def loadTimeSlotView(request):
    date = request.GET.get('date')
    doctor_id = request.GET.get('doctor_id')
    appointments = Appointment.objects.filter(date=date, doctor=doctor_id)
    TIME_SLOT= {
        '1' : '9:00 to 9:45',
        '2' : '9:45 to 10:30',
        '3' : '10:30 to 11:15',
        '4' : '11:15 to 12:00',
        '5' : '2:00 to 2:45',
        '6' : '2:45 to 3:30',
        '7' : '3:30 to 4:15',
        '8' : '4:15 to 5:00',
    }
    for appointment in appointments:
        del TIME_SLOT[appointment.time_slot]
    return JsonResponse(list(TIME_SLOT.items()), safe=False)
