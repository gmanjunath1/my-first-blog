from django import forms
from .models import skillSummary, Projects, WorkExperience

class skillsForm(forms.ModelForm):

    class Meta:
        model = skillSummary
        fields = ('text',)


class projectForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ('projectName', 'projectDate', 'description',) 


class experienceForm(forms.ModelForm):

    class Meta:
        model = WorkExperience
        fields = ('companyName', 'location', 'duration', 'startDate', 'extraInfo',) 
