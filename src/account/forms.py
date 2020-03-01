
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from account.models import User,Customer
from django.contrib.auth import authenticate
from django import forms
import datetime

class UserForm(ModelForm):
	password1=forms.CharField(label="Hasło",widget=forms.PasswordInput,help_text="Hasło musi być dłuższe niż 6 znaków")
	password2=forms.CharField(label="Powtórz Hasło",widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'email','password1','password2')
		labels = {
			'username': 'Login',
			'email': 'Email',
		}
		help_texts = {
            'username': None,
        }

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('address','city','phonenumber')
		labels = {
			'address': 'Adres',
			'city': 'Miasto',
			'phonenumber': 'Numer Telefonu',
		}


class AccountAuthenticationForm(forms.Form):
	username=forms.CharField(label="Login")
	password=forms.CharField(label="Hasło",widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=('username','password')


		def clean(self):
			username=self.cleaned_data['username']
			password=self.cleaned_data['password']
			if not authenticate(username=username,password=password):
				raise forms.ValidationErrors("Invalid login")
