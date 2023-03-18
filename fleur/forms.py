from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


# Create your forms here.

CHOICES =(
    ("none", "---SELECT FROM BELOW OPTIONS---"),
    ("rom", "ROMS"),
    ("mod", "MODS"),
)

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class Upload(forms.Form):
    upload=forms.ChoiceField(choices=CHOICES,help_text='What do You want to Upload Please Select..!')

        
class Upload_mod(forms.Form):
    class Meta:
        model = Mod
        fields = "__all__"
        
        