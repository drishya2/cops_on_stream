from django import forms
from .models import CustomUser,Case
class CopsEditForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','rank','badge_number','age','email','phone','service_years','pic']


class UserForm(forms.ModelForm):
    class Meta:
        model=Case
        fields=['type','date','place','culprit','describe']

class UserEditForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','phone','email','address','password','pic']
class StatusEditForm(forms.ModelForm):
    class Meta:
        model=Case
        fields=['status']



