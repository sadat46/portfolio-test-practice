from django import forms
from . models import User_Signup,UserProfileInfo
from django.contrib.auth.models import User


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User_Signup
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ("username","email","password")
        # exclude = ["firstname", "lastname"]
        # include = ["username","email","password"]

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")
        # fields = '__all__'