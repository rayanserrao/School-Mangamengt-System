from django import forms
from django.contrib.auth.models import User
from app_users.models import User_profile
from django.contrib.auth.forms import UserCreationForm
 

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        labels = {
            'passsord1':'Password',
            'password2': 'Confirm_ Password'
        }


class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    profile_pic = forms.ImageField(required=False)


    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_types = [
        (student,'student'),
        (parent,'parent'),
    ]

    user_type= forms.ChoiceField(required=True,choices=user_types)

    class Meta():
        model = User_profile
        fields = ['bio','profile_pic','user_type']