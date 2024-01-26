from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'autofocus': True, 'placeholder': 'Email'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))



class EditUserProfileForm(UserChangeForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    email = forms.EmailField(disabled=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_password(self):
        password = self.cleaned_data.get("password")
        user = self.instance
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password.")
        return password



class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs['user']
        self.fields['username'] = forms.EmailField(initial=self.user.email, disabled=True)

    class Meta:
        model = User
