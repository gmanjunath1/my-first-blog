from django import forms
from .models import skillSummary, Projects

class skillsForm(forms.ModelForm):

    class Meta:
        model = skillSummary
        fields = ('text',)


class projectForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ('projectName', 'projectDate', 'description',) 

