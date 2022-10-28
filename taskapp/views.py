from django.shortcuts import render,redirect
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test


def home_view(request):
    return render(request,'taskapp/index.html')



def doctorclick_view(request):
    return render(request,'taskapp/doctorclick.html')


def patientclick_view(request):
    return render(request,'taskapp/patientclick.html')


def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'taskapp/doctorsignup.html',context=mydict)


def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request,'taskapp/patientsignup.html',context=mydict)




def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


def afterlogin_view(request):
    if is_doctor(request.user):
        return redirect('doctor-dashboard')    
    elif is_patient(request.user):
        return redirect('patient-dashboard')
        

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    doctors=models.Doctor.objects.all().order_by('-id')
    mydict={
    'doctors':doctors, 
    }
    return render(request,'taskapp/doctor_dashboard.html',context=mydict)


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patients=models.Patient.objects.all().order_by('-id')
    mydict={
    'patient':patients,
    }
    return render(request,'taskapp/patient_dashboard.html',context=mydict)

def doctor_list_view(request):
    doctors=models.Doctor.objects.all().order_by('-id')
    mydict={
    'doctors':doctors, 
    }
    return render(request,'taskapp/doctor_list.html',context=mydict)



