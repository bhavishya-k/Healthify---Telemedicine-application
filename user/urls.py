from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/doctor/', views.DoctorTokenView.as_view(),name='token_obtain_pair_doctor'),
    path('login/patient/', views.PatientTokenView.as_view(),name='token_obtain_pair_patient'),
    path('login/hospital/', views.HospitalTokenView.as_view(),name='token_obtain_pair_hospital'),
    path('login/pharmacy/', views.PharmacyTokenView.as_view(),name='token_obtain_pair_pharmacy'),
    path('login/ambulance/', views.AmbulanceTokenView.as_view(),name='token_obtain_pair_ambulance'),
    path('login/bloodbank/', views.BloodbankTokenView.as_view(),name='token_obtain_pair_bloodbank'),
    path('login/lab/', views.LabTokenView.as_view(),name='token_obtain_pair_lab'),
    path('info/', views.UserView.as_view(), name='info'),
    path('update/', views.UpdateUserView.as_view(), name='update'),
    path('auth/', include('rest_framework.urls')),
]
