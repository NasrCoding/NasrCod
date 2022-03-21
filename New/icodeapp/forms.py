from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username=forms.CharField(label='username',required=True, widget=forms.TextInput())
    fullName = forms.CharField(label='fullName',required=True, widget=forms.TextInput())
    email = forms.EmailField(label='email',required=True, widget=forms.TextInput())
    password1 = forms.CharField(label='parol',required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(label='repeatPassword',required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        
        fields = ("username", "fullName", "email", "password1", "password2" )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        user.fullName = self.cleaned_data["fullName"]
 
        if commit:
            user.save()
            return user

    