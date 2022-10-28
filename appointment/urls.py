from django.urls import path
from . import views

app_name = "appointment"

urlpatterns = [
    #path("doctor/", views.DoctorListView, name="doctor_list_view"),
    path("doctor/", views.DoctorListView.as_view(), name="doctor_list_view"),
    path('appointment/<str:id>/', views.AppointmentDetailView.as_view(), name='appointment_detail_view'),
    path('appointment-create/<str:doctor_id>/', views.AppointmentCreateView.as_view(), name='appointment_create_view'),
    # path('my-blog/', views.MyBlogListView.as_view(), name='my_blog_list_view'),

    path('ajax/load-time-slot/', views.loadTimeSlotView, name='load_time_slot_view'), # AJAX
]