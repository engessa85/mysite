from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import user_service

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    whatsapp_number = forms.IntegerField()

    class meta:
        model = User
        fields = ['username','email' ,'password1','password2','whatsapp_number']


class AddingRequest(forms.ModelForm):
    class Meta:
        model = user_service
        fields = ['title','services','subject','delivery_date','file']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add title to your request.'}),
            'subject': forms.Textarea(attrs={'placeholder': 'Write a brief description about your request.'}),
            'delivery_date': forms.TextInput(attrs={'placeholder': 'Year-Month-Day'})

        }
