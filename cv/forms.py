from django import forms
from .models import skillSummary, Projects, WorkExperience, AchieveAccomplish, memberships

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


class achievementForm(forms.ModelForm):

    class Meta:
        model = AchieveAccomplish
        fields = ('titleAch', 'dateAchieved', 'description',) 


class membershipForm(forms.ModelForm):

    class Meta:
        model = memberships
        fields = ('membershipName', 'dateMembership', 'description',) 
