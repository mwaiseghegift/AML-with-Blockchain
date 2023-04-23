from django import forms
from requests import request
from .models import *
# import authenicate
from django.contrib.auth import authenticate, login
from django.contrib import messages


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email*', 
                                                    'class':'form-control', 'id':'pass'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password*',
                                                    'class':'form-control border-right-0', 'data-toggle': 'password'}))

    fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            user = User.objects.filter(email=email)
            if not user:
                raise forms.ValidationError("Invalid email")
        return email

    def clean_password(self):
        # passeord length must be greater than 6 characters
        password = self.cleaned_data.get('password')
    
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long")
        return password

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid email or password")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return self.cleaned_data

class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name*', 
                                                    'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name*', 
                                                    'class':'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Email'}))
    phone_number = forms.CharField(label='Phone No', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone No'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border-right-0', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border-right-0', 'placeholder': 'Confirm Password'}))

    fields = ['email', 'phone_number', 'password', 'confirm_password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('Email already taken')
        if not email:
            raise forms.ValidationError('Email is required')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError('Phone No is required')
        return phone_number

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Password is required')
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long")
        return password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')

        if not confirm_password:
            raise forms.ValidationError('Confirm Password is required')

        elif password != confirm_password:
                raise forms.ValidationError('Passwords do not match')
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long")
        return confirm_password

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        # name validation
        if first_name and last_name:
            if not first_name.isalpha() or not last_name.isalpha():
                raise forms.ValidationError('Name must be characters only')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')

        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('Email already exists')
        
        # pick last 9 digits of phone no
        phone_number = "254"+str(phone_number[-9:])
        
        # create user without username field
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email, 
            phone_number=phone_number,
            )
        user.set_password(password)
        user.save()
        return user
