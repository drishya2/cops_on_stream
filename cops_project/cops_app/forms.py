from django import forms
from .models import Police,My_User,Case
class CopsEditForm(forms.ModelForm):
    class Meta:
        model=Police
        fields=['name','rank','badge_number','age','email','phone','service_years','pic']


class UserForm(forms.ModelForm):
    class Meta:
        model=Case
        fields=['type','date','place','culprit','describe']

class UserEditForm(forms.ModelForm):
    class Meta:
        model=My_User
        fields=['first_name','last_name','username','phone','email','address','password','pic']


