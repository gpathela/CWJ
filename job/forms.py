from django import forms

from job.models import Job

class JobForm(forms.ModelForm):

	details = forms.CharField(
        label='Details', 
        widget=forms.TextArea(
            attrs={'placeholder': 'Enter all details related to Job'}
        )
    )

    required_date = forms.DateField(
    	widget=forms.CharField(
            attrs={'placeholder': 'Job Start Date'}
        ))

    class Meta:
        model = Job
        fields = ['title', 'details', 'location', 'remuneration', 'required_date', 'activate_date', 'post_date']

