from django.contrib.auth.admin import UserAdmin
from .models import user as USER

from django.contrib import admin

# Register your models here.
@admin.register(USER)
class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.set_password(obj.password)
        super().save_model(request, obj, form, change)
    list_display=['id','email','role','is_staff']
    