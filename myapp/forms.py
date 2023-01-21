from django import forms
from .models import *

subjects = (
        
        ('django Web Application', 'Double Bed Room'),
        ('django Web Application', 'Singel Bed Room'),
        ('django Web Application', 'Master Bed Room'),
        ('django Web Application', 'Stander Room'),

    )

gender = (
        
        ('django Web Application', 'male'),
        ('django Web Application', 'Fimale'),
        ('django Web Application', 'Others'),
        
    )

class Contacts (forms.ModelForm):
    Name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Name" }))

    Email = forms.EmailField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Email" }))

    Phone = forms.IntegerField(widget= forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Phone Number" }))
    
    Massege = forms.CharField(widget= forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder' : "Massage" }))

    class Meta:
        model = Contact
        fields = '__all__'

class OrderRoom (forms.ModelForm):
    full_name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Full Name" }))
    
    
    email = forms.EmailField(widget= forms.EmailInput(attrs ={
        'class': 'form-control', 'placeholder':"Your Email" }))


    birthday = forms.CharField(widget= forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Birth Day", 'type':"Date"}))


    phone = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Phone Number" }))

    nid = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your NID Number" }))

    st_date = forms.CharField(widget= forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder' : "Start Date", 'type':"Date" }))
    
    end_date = forms.CharField(widget= forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder' : "End Date", 'type':"Date" }))

    class Meta:
        model = RoomOrder
        fields = '__all__'

