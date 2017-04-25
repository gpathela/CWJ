from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy,reverse
from job.models import Job
from application.models import Application, ApplicationStatus,SaveJob,Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

@method_decorator(login_required, name='dispatch')
class ApplicationCreate(CreateView):
	
	model = Application
	fields = ['subject', 'message', 'resume']
	success_url = '/'


	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.job_id = self.kwargs['pk']
		statusId = ApplicationStatus.objects.get(status="Applied")
		form.instance.status_id = statusId.id
		return super(ApplicationCreate, self).form_valid(form)

@login_required
def applications(request,pk):
	context = {}
	job = Job.objects.get(pk = pk)
	if (job.user == request.user):
		obj = Application.objects.filter(job = pk)
		if len(obj) > 0:
			context['applications'] = obj
		else:
			context['message'] = "No applications yet"

	else:
		context['message'] = "Not your opening"

	return render(request,"application/applications.html",context)


@login_required
def saveJob(request,pk):
	obj = Job.objects.get(pk = pk)
	saver = SaveJob.objects.create(job = obj, user=request.user, title = obj.title)
	saver.save()
	messages.add_message(request, messages.success, 'Job Saved')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def applicationDetails(request,pk):
	context = {}
	try:
		obj = Application.objects.get(pk = pk)

		context['application'] = obj
	except:
		context['message'] = "Some problem."

	return render(request,"application/details.html",context)


@method_decorator(login_required, name='dispatch')
class MessageForm(CreateView):
	
	model = Message
	fields = ['subject', 'message']
	success_url = '/recruit/'

	def get_initial(self):
		jobObj = Job.objects.get(pk =self.kwargs.get('job'))
		receiverObj = User.objects.get(pk =self.kwargs.get('receiver'))
		return {
            'job':jobObj,
            'receiver':receiverObj,
        }


	def form_valid(self, form):
		form.instance.sender = self.request.user
		form.instance.receiver_id = self.kwargs['receiver']
		form.instance.job_id = self.kwargs['job']
		return super(MessageForm, self).form_valid(form)


@login_required
def statusUpdate(request,job,status):
	jobObj = get_object_or_404(Job, pk = job)
	jobObj.status = status
	jobObj.save()




	
		