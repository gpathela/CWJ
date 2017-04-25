"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from user import views as user
from job.views import JobCreate, JobUpdate, JobDelete, JobList,JobDetails
from application.views import ApplicationCreate,applications,saveJob, applicationDetails,MessageForm,statusUpdate

from django.conf import settings
#from programming_database import settings
#from django.views.generic.simple import direct_to_template



urlpatterns = [
	url(r'^$', JobList.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', JobDetails.as_view(), name='detail'),
	url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^home/', user.profile, name='home'),
    url(r'^job/add/$', JobCreate.as_view(), name='job-add'),
    url(r'^job/(?P<pk>[0-9]+)/$', JobUpdate.as_view(), name='job-update'),
    url(r'^job/(?P<pk>[0-9]+)/delete/$', JobDelete.as_view(), name='job-delete'),
    url(r'^user/basic/(?P<pk>[0-9]+)/$', user.BasicUpdate.as_view(), name='user-basic'),
    url(r'^(?P<pk>[0-9]+)/apply/$', ApplicationCreate.as_view(), name='apply'),
    url(r'^recruit/$', user.recruit, name='recruit'),
    url(r'^recruit/(?P<pk>[0-9]+)/$', user.Employer.as_view(), name='employer-details'),
    url(r'^job/(?P<pk>[0-9]+)/applications/$', applications, name='job-applications'),
    url(r'^(?P<pk>[0-9]+)/save/$', saveJob, name='save-job'),
    url(r'^application/(?P<pk>[0-9]+)/$', applicationDetails, name='application-details'),
    url(r'^application/status/(?P<job>[0-9]+)/(?P<status>[0-9]+)/$', statusUpdate, name='application-status-update'),
    url(r'^contact/(?P<receiver>[0-9]+)/(?P<job>[0-9]+)/$', MessageForm.as_view(), name = 'contact'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
