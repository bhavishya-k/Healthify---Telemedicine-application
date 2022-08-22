from django.contrib import admin
from .models import *

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['Hospital_id','user','name','state']

admin.site.register(HealthcareType)
admin.site.register(Speciality)
admin.site.register(Facilities)
admin.site.register(AyushType)
admin.site.register(MiscellaneousFacilities)
admin.site.register(HospitalAyushtype)
admin.site.register(HospitalSpecialities)
admin.site.register(HospitalFacilities)
admin.site.register(HospitalHealthcare)
admin.site.register(HospitalMFacilies)