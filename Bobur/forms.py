from django import forms
from django.core.exceptions import ValidationError
# from django.forms import ModelForm

from Bobur.models import User, Post




class UserRegisterModelForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    def save(self, commit=True):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1==password2:
            user1 = super().save(commit)
            # user1.set_password(password1)
            # user1.save()
        else:
            return ValidationError("Password must match")

    class Meta:
        model = User
        fields = ["username",  "email", "first_name", "last_name", "password1", "password2"]


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)  


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'avatar']