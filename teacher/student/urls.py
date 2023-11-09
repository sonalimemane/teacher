# In appname/urls.py

from django.urls import path
from . import views
app_name = 'student'

urlpatterns = [
    path('teacher/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_student/', views.add_student, name='add_student'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('verify_certificate/<int:certificate_id>/', views.verify_certificate, name='verify_certificate'),

]
