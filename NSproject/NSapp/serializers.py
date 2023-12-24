from .models import Course, Instructor
from rest_framework import serializers

class CourseSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = '__all__'