from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django  import forms
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))

    #  

    def clean_username(self):
        username = self.clean_data.get('username')
        qs = User.objects.filter(username_iexacvt=username)
        if not qs.exists():
            raise forms.ValidationError("this is an invalid user")
        return username