from django import forms


class SendToMail(forms.Form):
    firstName = forms.CharField(max_length=40)
    lastName = forms.CharField(max_length=40)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))