from django.forms import ModelForm, Form, TextInput, PasswordInput, CharField, EmailInput
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import UserProfile
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2')

    username = CharField(
        label="Name",
        required=True,
         widget=TextInput(attrs={'placeholder': 'First Name'})
    )

    email = CharField(
        label="Email Address",
        required=True,
        widget=EmailInput(attrs={'placeholder': 'Email Address'})
    )
    password1 = CharField(
        label="Password",
        required=True,
        widget=PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = CharField(
        label="Confirm Password",
        required=True,
        widget=PasswordInput(attrs={'placeholder': 'Enter the same password as before, for verification'})
    )

        
class LoginForm(Form):
    username = CharField(
        max_length = 55,
        min_length = 4,
        label = 'Username',
        required = True,
        widget=TextInput()
        # widget = EmailInput({
        #         'class': 'form-control'
        #     })
    )

    password = CharField(
        max_length = 25,
        min_length = 4,
        label = 'Password',
        required = True,
        widget= PasswordInput()
        # widget = PasswordInput({
        #         'class': 'form-control'
        #     })
    )


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    profile_picture = forms.ImageField(required=False)
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'age', 'profile_picture']