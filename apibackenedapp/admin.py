from django.contrib import admin
from .models import Department, Employee
from rest_framework.authtoken.models import Token

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Token)