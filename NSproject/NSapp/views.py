from django.shortcuts import render
from rest_framework import generics
from .serializers import InstructorSerializer
from .serializers import CourseSerilizer
from .models import Instructor
from .models import Course
from rest_framework .permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework .authentication import BasicAuthentication,TokenAuthentication
# Create your views here.

class WriteByAdminOnlyPerminssion(BasePermission):
    def has_object_permission(self, request, view):
        print('insidnde has permission',request.user)
        user = request.user
        if request.method =='GET':
            return True
        if request.method =='POST' or request.method == "PUT" or request.method == "DELETE":
            if user.is_superuser:
                return True
        return False


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset =    Instructor.objects.all()


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset =    Instructor.objects.all() 

class CourseListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,WriteByAdminOnlyPerminssion]
    serializer_class = CourseSerilizer
    queryset = Course.objects.all()

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerilizer
    queryset = Course.objects.all()