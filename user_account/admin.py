from django.contrib import admin
from .models import CustomUser,LoginAttempt,PasswordReset
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','is_staff','is_active','is_superuser']
    list_filter = ['is_staff','is_active','is_superuser']
    search_fields = ['id','username','first_name','last_name']

    fieldsets = (
        (None,{'fields':('username','email','password')}),
        ('personal information',{'fields':('first_name','last_name','birth_date','country','city','phone_number')}),
        ('permessions',{'fields':('is_active','is_staff','is_superuser','is_emailVerified')})
    )

    add_fieldsets = (
        (None,{'classes':('wide',),
               'fields':('email','first_name','last_name','phone_number','password','is_staff','is_active','is_superuser')})
    )

@admin.register(LoginAttempt)
class LoginAttempAdmin(admin.ModelAdmin):
    list_display = ['id','username','ip_address']

@admin.register(PasswordReset)
class PassResetAdmin(admin.ModelAdmin):
    list_display = ['id','email','token']