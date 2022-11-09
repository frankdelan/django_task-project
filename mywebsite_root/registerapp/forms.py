from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': "form-field",
                                                                                      'placeholder': "Login"}))

    password = forms.CharField(label='', widget=(forms.PasswordInput(attrs={'class': "form-field",
                                                                            'placeholder': "Password"})))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password")
        help_texts = {
            'password': None
        }


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': "form-field",
                                                                                        'placeholder': "First Name"}))

    second_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': "form-field",
                                                                                         'placeholder': "Second Name"}))

    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': "form-field",
                                                                                      'placeholder': "Username"}))

    password1 = forms.CharField(label='', widget=(forms.PasswordInput(attrs={'class': "form-field",
                                                                             'placeholder': "Password"})))

    password2 = forms.CharField(label='', widget=(forms.PasswordInput(attrs={'class': "form-field",
                                                                             'placeholder': "Password Confirmation"})))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "second_name", "username", "password1", "password2")
        help_texts = {
            'password': None
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']