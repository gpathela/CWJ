from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
import datetime


# Create your models here.
class JobStatus(models.Model):
	status = models.CharField(max_length = 100, blank = False)

	def __str__(self):
		return self.status

class Job(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length = 100, blank = False)
	details = models.TextField(max_length = 1000, blank = False)
	location = models.CharField(max_length = 100, blank = False)
	remuneration = models.CharField(max_length = 100, blank = False)
	start_date = models.DateField(default=datetime.date.today)
	activate_date = models.DateField(default=datetime.date.today)
	post_date = models.DateField(default=datetime.date.today)

	def get_absolute_url(self):
		return reverse('job-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title



