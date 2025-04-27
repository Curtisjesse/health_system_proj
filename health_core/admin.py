# from django.contrib import admin

# # Register your models here.
from django.contrib import admin
from .models import Program, Client, Enrollment

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'contact_number')
    search_fields = ('first_name', 'last_name', 'contact_number')
    list_filter = ('gender',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'program', 'enrollment_date', 'status')
    list_filter = ('program', 'status', 'enrollment_date')
    search_fields = ('client__first_name', 'client__last_name', 'program__name')