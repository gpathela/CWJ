from django.db import models
from job.models import *

# Create your models here.

class UserDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobile = models.IntegerField(blank = True)
	pic = models.URLField()	
	facebook_profile = models.URLField()
	google_profile = models.URLField()
	linkedin_profile = models.URLField()
	

	

class EmployerDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	company = models.CharField(max_length = 150, blank = False)
	company_url = models.URLField()
	official_email = models.EmailField()
	company_facebook_page = models.URLField()
	company_google_page = models.URLField()
	company_linkedin_page = models.URLField()
	

	