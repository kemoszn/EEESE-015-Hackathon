from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    index=forms.CharField()
    dept = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)