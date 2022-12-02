from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SendToMail(forms.Form):
    firstName = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-input'}))
    lastName = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-input'}), label="Email (for feedback)")
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Password", widget=forms.TextInput(attrs={'class': 'form-input'}))
