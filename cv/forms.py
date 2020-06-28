from django import forms
from .models import skillSummary

class skillsForm(forms.ModelForm):

    class Meta:
        model = skillSummary
        fields = ('text',)