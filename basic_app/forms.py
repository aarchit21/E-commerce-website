from django import forms
from django.contrib.auth.forms import UserCreationForm
from basic_app.models import CustProfileInfo,VendorProfileInfo,User

class customer_profile:
    class UserForm(forms.ModelForm):
        password=forms.CharField(widget=forms.PasswordInput())
        class Meta():
            model = User
            fields=('username','email','password')

    class UserProfileInfoForm(forms.ModelForm):
        class Meta():
            model = CustProfileInfo
            fields=('Name','Phone','Address','Zipcode')


class vendor_profile:
    class UserForm(forms.ModelForm):
        password=forms.CharField(widget=forms.PasswordInput())
        class Meta():
            model = User
            fields=('username','email','password')
    class UserProfileInfoForm(forms.ModelForm):
        class Meta():
            model = VendorProfileInfo
            fields=('Name','Phone','Shop_Name')
