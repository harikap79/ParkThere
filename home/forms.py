from django.contrib.auth.forms import UserCreationForm
from home.models import User
from django import forms

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = ('email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['password2'].help_text = None
		self.fields['password1'].help_text = "<p>Your password must be of at least 8 characters, and must not be entirely numeric</p>"
	def save(self, commit = True):        
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()

		return user

class SaveLotForm(forms.Form):
        print('debug save lot form')
        carpark_name= forms.CharField(label='CarPark Name')
        carpark_level= forms.CharField(label='CarPark Level')
        carpark_zone= forms.CharField(label='CarPark Zone')
        carpark_lot= forms.CharField(label='CarPark Lot Number')
