from django.db import models
from job.models import *

from datetime import datetime  

# Create your models here.

class ApplicationStatus(models.Model):
	status = models.CharField(max_length = 100, blank = False)

	def __str__(self):
		return self.status

class Application(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	job = models.ForeignKey(Job,on_delete=models.CASCADE)
	application_on = models.DateTimeField(default=datetime.now)
	status = models.ForeignKey(ApplicationStatus,on_delete=models.CASCADE)
	subject = models.CharField(max_length = 100, blank = False)
	message = models.TextField(max_length = 1000, blank = False)
	resume = models.FileField(upload_to='resumes/')

	def get_absolute_url(self):
		return reverse('apply', kwargs={'pk': self.pk})

class SaveJob(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	job = models.ForeignKey(Job,on_delete=models.CASCADE)
	title = models.CharField(max_length = 100, blank = False)
	saved_on = models.DateTimeField(default=datetime.now)

class Message(models.Model):
	sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='JobOwner')
	receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Applicant')
	job = models.ForeignKey(Job,on_delete=models.CASCADE)
	subject = models.CharField(max_length = 100, blank = False)
	message = models.TextField(max_length = 1000, blank = False)
	sent_on = models.DateTimeField(default=datetime.now)