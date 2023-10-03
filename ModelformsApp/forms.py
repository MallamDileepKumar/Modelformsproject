from django import forms
from .models import Register

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widgets = {'Password': forms.PasswordInput(),'ConfirmPassword': forms.PasswordInput()}


class LogForm(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(max_length=15,widget=forms.PasswordInput())

