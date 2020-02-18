from django import forms
from voting.models import *

class UserForm(forms.ModelForm):
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password')


class VoterForm(forms.ModelForm):
    class Meta:
        model=Voter
        fields=('constituency',)

class ConstForm(forms.ModelForm):
    class Meta:
        model=Constituency
        fields="__all__"