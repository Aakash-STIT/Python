from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('firstName', 'lastName', 'age',
                  'qualification', 'university', 'email', 'password')
        widgets = {'password': forms.PasswordInput()}

    def __init__(self, *args, **kwrds):
        super(StudentForm, self).__init__(*args, **kwrds)
        self.fields['university'].empty_label = "Select"

