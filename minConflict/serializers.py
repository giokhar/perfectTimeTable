from rest_framework import serializers
from minConflict.models import Course as CourseModel, Student as StudentModel, Major as MajorModel

class MajorSerializer(serializers.ModelSerializer):

	class Meta:
		model = MajorModel
		fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = CourseModel
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentModel
		fields = '__all__'