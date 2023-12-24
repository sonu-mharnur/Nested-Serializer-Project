from django.contrib import admin
from. models import Course,Instructor
# Register your models here.

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display=('name','email')

admin.site.register(Course)