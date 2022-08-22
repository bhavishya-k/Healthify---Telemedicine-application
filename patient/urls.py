from django.urls import path,include
from .views import PatientView

urlpatterns = [
    path('info/',PatientView,name='patient info'),
    path('add/',PatientView,name='add patient'),
    path('update/',PatientView,name='update patient'),
    path('delete/',PatientView,name='delete patient'),
]
