from django import forms
from .models import Contact, User


class ContactForm(forms.ModelForm):
    """
    Contact form using HTML attributes.
    """
    class Meta:
        model = Contact
        fields = [
            'contact_title',
            'contact_body',
            'contact_email'
        ]

    contact_title = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        })
    )
    contact_body = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Body'
        })
    )
    contact_email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email'
        })
    )
