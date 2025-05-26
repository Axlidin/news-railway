from django.forms import Form, ModelForm
from django import forms
from .models import ContactModel

class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        # fields = ['name', 'email', 'phone', 'message']
        fields = '__all__'