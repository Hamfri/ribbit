from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from ribbit_app.models import Ribbit

class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}))
	username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
	password1 = forms.CharField(widget=forms.widgets.passwordInput(attr={'placeholder': 'Password'}))
	password12 = forms.CharField(widget=forms.widgets.passwordInput(attrs={'placeholder': 'Password Confirmation'}))

	def is_valid(self):
		form super(UserCreateForm,self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form

	class Meta:
		fields = ['email', 'username', 'first_name', last_name, password1, password2]

		model = User