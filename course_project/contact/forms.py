from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Ad, Soyad')
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('Email')
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': _('Mətn'),
        'rows': '4',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Telefon')
    }))

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message', 'phone_number']
