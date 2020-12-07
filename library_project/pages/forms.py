from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StudentRecords

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = StudentRecords
        fields = UserCreationForm.Meta.fields + ('rollNo', 'yearOfAdmission', 'name', 'branch','rollNo', 'book1', 'book2', 'book3',)

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = StudentRecords
        fields = UserChangeForm.Meta.fields
