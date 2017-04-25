from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from job.models import Job
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render





class JobList(ListView):
    model = Job
    queryset = Job.objects.order_by('-activate_date')
    template_name = 'index.html'

class JobDetails(DetailView):
    model = Job
    template_name = 'details.html'
    


#def index(request):
	#jobs = Job.objects.all
	#context = {'jobs': jobs}
	#return render(request,"profile.html",context)


@method_decorator(login_required, name='dispatch')
class JobCreate(CreateView):
    model = Job
    fields = ['title', 'details', 'location', 'remuneration', 'start_date', 'activate_date']
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class JobUpdate(UpdateView):
    model = Job
    fields = ['title', 'details', 'location', 'remuneration', 'start_date', 'activate_date', 'post_date']


@method_decorator(login_required, name='dispatch')
class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('job-list')

@method_decorator(login_required, name='dispatch')
class PublisherList(ListView):
    model = Job
    template_name = 'profile.html'


