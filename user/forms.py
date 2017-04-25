from django.forms import ModelForm
from user.models import UserDetails


class SignupForm(ModelForm):
	class Meta:
		model = UserDetails
		fields = ['facebook_profile', 'google_profile', 'linkedin_profile']

	def signup(self, request, user):
		pass