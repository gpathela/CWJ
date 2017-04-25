from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from job.models import Job
from user.models import UserDetails, EmployerDetails
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@login_required
def profile(request):
	jobs = Job.objects.filter(user=request.user)
	context = {'jobs': jobs}
	if UserDetails.objects.filter(user=request.user).exists():
		obj = UserDetails.objects.filter(user=request.user)
		context['obj'] = obj
	else:
		
		x = request.user.id
		return redirect(reverse('user-basic',kwargs={'pk': x}))

	return render(request,"profile.html",context)

@method_decorator(login_required, name='dispatch')
class BasicCreate(CreateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class BasicUpdate(UpdateView):
	model = User
	template_name = 'user/basic_form.html'
	fields = ['username', 'email', 'first_name', 'last_name', 'staff_status']
	


	def user_passes_test(self, request):
		if request.user.is_authenticated():
			self.object = self.get_object()
			return self.object== request.user
		return False

	def dispatch(self, request, *args, **kwargs):
		if not self.user_passes_test(request):
			return redirect_to_login(request.get_full_path())
		return super(BasicUpdate, self).dispatch(request, *args, **kwargs)

@login_required
def recruit(request):
	if EmployerDetails.objects.filter(user=request.user).exists():
		jobs = Job.objects.filter(user=request.user)
		context = {'jobs': jobs}
		return render(request,"user/employer.html",context)
	else:
		x = request.user.id
		return redirect(reverse('employer-details',kwargs={'pk': x}))

	return render(request,"profile.html",context)

@method_decorator(login_required, name='dispatch')
class Employer(CreateView):
	model = EmployerDetails
	template_name = 'user/employer_form.html'
	fields = ['company', 'company_url', 'official_email', 'company_facebook_page', 'company_google_page', 'company_linkedin_page']
	success_url = '/recruit/'
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(Employer, self).form_valid(form)

@login_required
def statusUpdate(request,job,status):
	jobObj = get_object_or_404(Job, pk = job)
	jobObj.status = status
	jobObj.save()




