from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register-student', views.register_student, name="register_student"),
    path('register-teacher', views.register_teacher, name="register_teacher"),
    path('get-user-details', views.get_user_details, name="get-user-details"),
    path('get-students', views.get_students, name="get-students"),
    path('get-announcements', views.get_announcements, name="get-announcements"),
    path('get-timetable', views.get_timetable, name="get-timetable"),
    path('mark_attendance', views.mark_attendance_api, name="mark-attendance"),
]