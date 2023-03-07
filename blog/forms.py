from django import forms
from .models import Aplication

class StudentForm(forms.ModelForm):
    name= forms.CharField(widget=forms.TextInput(attrs={'class': 'input my-2'}), label="Name:")
    email= forms.CharField(widget=forms.EmailInput(attrs={'class': 'input my-2'}), label="Email:")
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input my-2'}), label="Password:")
    
    class Meta:
        model=Aplication
        fields=['name', 'email', 'password']
