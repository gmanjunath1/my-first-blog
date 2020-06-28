from django.http import HttpResponse
from django.utils import timezone
from .models import skillSummary, Education, WorkExperience, AchieveAccomplish, memberships, Projects
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import skillsForm

# Create your views here.
def cv_sectionList(request):
    return render(request, 'cv/cv_sectionList.html')

def skillsSummaryPage(request):
    skills = skillSummary.objects.all()
    return render(request, 'cv/summarySkillsPage.html', {'skills' : skills[0]})

def skills_detail(request, pk):
    #Post.objects.get(pk=pk)
    #skills = get_object_or_404(skillSummary, pk=pk)
    skills = skillSummary.objects.all()
    return render(request, 'cv/skill_Entry_Detail.html', {'skills': skills[0]})

@login_required
def skills_edit(request, pk):
    skills = get_object_or_404(skillSummary, pk=pk)
    if request.method == "POST":
        form = skillsForm(request.POST, instance=skills)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.author = request.user
            #post.published_date = timezone.now()
            skills.save()
            return redirect('skills_detail', pk=skills.pk)
    else:
        form = skillsForm(instance=skills)
    return render(request, 'cv/skills_edit.html', {'form': form})

def educationPage(request):
	gcses = Education.objects.filter(edu_type='GCSE')
	AS = Education.objects.filter(edu_type='AS-Level')
	A = Education.objects.filter(edu_type='A-Level')
	uni = Education.objects.filter(edu_type='Degree')
	return render(request, 'cv/EducationPage.html', {'gcses' : gcses, 'AS_Levels' : AS, 'A_Levels' : A, 'uni' : uni})

def workExperiencePage(request):
	experiences = WorkExperience.objects.order_by('-startDate')
	return render(request, 'cv/workExperiencePage.html', {'experiences' : experiences})

def achieveAccomplish(request):
    achievements = AchieveAccomplish.objects.order_by('-dateAchieved')
    return render(request, 'cv/achievementsPage.html', {'achievements' : achievements})


def Memberships(request):
    membs = memberships.objects.order_by('-dateMembership')
    return render(request, 'cv/membershipsPage.html', {'membs' : membs})

def projects(request):
    proj = Projects.objects.order_by('-projectDate')
    return render(request, 'cv/projectsPage.html', {'projects' : proj})

