from store.models.customer import Customer
from django import forms
from django.forms.forms import Form

class Custum(forms.Form):
    name = forms.CharField()
    phone_no = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


        