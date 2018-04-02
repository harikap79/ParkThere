from django.contrib.auth.forms import UserCreationForm
from home.models import User, RecordedParkingLot
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

class SaveLotForm(forms.ModelForm):
        
        class Meta:
                model = RecordedParkingLot
                fields = ('carParkName','carParkLot','carParkLevel','carParkZone')
                
        def __init__(self, *args, **kwargs):
                super(forms.ModelForm, self).__init__(*args, **kwargs)
                
        def save(self, commit = True):
                print('debug save lot form')
                print('debug commit 1 = '+str(commit))
                cpl = super(forms.ModelForm, self).save(commit=False)
                cpl.carParkName= self.cleaned_data['carParkName']
                cpl.carParkLevel= self.cleaned_data['carParkLevel']
                cpl.carParkZone= self.cleaned_data['carParkZone']
                cpl.carParkLot= self.cleaned_data['carParkLot']
                print('debug commit 2 = '+str(commit))
                if commit:
                        cpl.user = self.user
                        cpl.save()
                        print('debug form saved')
                        print('debug carpark name: '+cpl.carParkName)
                        print('debug user name: '+cpl.user.email)
                return cpl
