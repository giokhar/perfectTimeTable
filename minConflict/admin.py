from django.contrib import admin
from .models import Course, Student

# Register your models here.
admin.register(Course, Student)(admin.ModelAdmin)