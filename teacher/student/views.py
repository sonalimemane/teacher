# In appname/views.py
##from django.shortcuts import render
from .forms import TeacherStudentPairForm
from .models import Certificate
import jwt
from django.http import JsonResponse
from .models import Student, Teacher
from django.shortcuts import render, redirect
from .forms import TeacherForm, StudentForm

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail')  # Redirect to the list of teachers or another appropriate page
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_detail')  # Redirect to the list of students or another appropriate page
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def teacher_detail(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    students = teacher.students.all()
    return render(request, 'teacher_detail.html', {'teacher': teacher, 'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    teachers = student.teachers.all()
    return render(request, 'student_detail.html', {'student': student, 'teachers': teachers})


def generate_certificate(request):
    if request.method == 'POST':
        form = TeacherStudentPairForm(request.POST)
        if form.is_valid():
            teacher = form.cleaned_data['teacher']
            student = form.cleaned_data['student']
            content = form.cleaned_data['content']
            certificate = Certificate.objects.create(teacher=teacher, student=student, content=content)
            # You can create the certificate content as needed
            return redirect('certificate_detail', certificate_id=certificate.id)
    else:
        form = TeacherStudentPairForm()
    
    return render(request, 'generate_certificate.html', {'form': form})


def verify_certificate(request, certificate_id):
    certificate = Certificate.objects.get(id=certificate_id)
    
    # Verify the JWT token
    try:
        jwt.decode(certificate.content, 'your-secret-key', algorithms=['HS256'])
        return JsonResponse({'valid': True, 'student': certificate.student.name, 'teacher': certificate.teacher.name})
    except jwt.ExpiredSignatureError:
        return JsonResponse({'valid': False, 'error': 'Certificate has expired'})
    except jwt.DecodeError:
        return JsonResponse({'valid': False, 'error': 'Certificate is invalid'})


