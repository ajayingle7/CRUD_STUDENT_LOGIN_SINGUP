from django import forms
from .models import Student,Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        labels = {'sid':'Student ID','fname':'First Name','lname':'Last Name','mno':'Mobile NO','city':'City'}

    def clean_sid(self):
        data = self.cleaned_data['sid']

        if data<1:
            raise forms.ValidationError('id should positive')
        return data







class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

