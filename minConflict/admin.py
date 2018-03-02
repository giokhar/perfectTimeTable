from django.contrib import admin
from .models import Course, Student, Major

# Register your models here.
admin.register(Course, Student, Major)(admin.ModelAdmin)