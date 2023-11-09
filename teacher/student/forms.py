from django import forms
from .models import Teacher, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']


class TeacherStudentPairForm(forms.Form):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    content = forms.CharField(widget=forms.Textarea)
