from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import *


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    def clean_email(self):
        email = self.cleaned_data['email']
        if '@walchandsangli.ac.in' not in email:
            raise  ValidationError("Please enter valid walchand email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    class Meta:
            model=User
            fields=['username','first_name','last_name','email']
            labels={'email':'Email'}

class ImageUpload(forms.ModelForm):
    photo = forms.ImageField(allow_empty_file=True)
    class Meta:
        model = Images
        fields = ['photo']


class AddProject(forms.ModelForm):

    # guide = forms.ModelChoiceField(queryset=Guide.objects.all(), widget= ListTextWidget())
    # guide = forms.Data
    class Meta:
        # guide = forms.ModelChoiceField()
        model = Project
        # guide = forms.ChoiceField(choices= l1)
        fields = ['name','tag_line','photo','year','domain','inspiration','what_it_does','how_we_build','challenges','accomplishment','we_learned','whats_next','github','hosted']
        labels = { 'year':'Year of developement','what_it_does':'What it does','how_we_build':'How we build it','challenges':'Challenges we ran into','accomplishment':'Accomplishment that we are proud of','we_learned':'What we learnt','whats_next':'Whats next','github':'Github link of project','hosted':'Hosted Link'}
        
