from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import user_service

class RegisterForm(UserCreationForm):



    class meta:
        model = User
        fields = ['username','password1','password2']


class AddingRequest(forms.ModelForm):
    class Meta:
        model = user_service
        fields = ['title','services','subject','email', 'whatsapp_number','country','delivery_date','file']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add title to your request.'}),
            'subject': forms.Textarea(attrs={'placeholder': 'Write a brief description about your request.'}),
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'Example:-> 00965 - 94964095'}),
            'delivery_date': forms.TextInput(attrs={'placeholder': 'Year-Month-Day'})
        }
