from django import forms


class SendToMail(forms.Form):
    firstName = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-input'}))
    lastName = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))