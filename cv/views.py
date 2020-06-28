from django.http import HttpResponse
from django.utils import timezone
from .models import skillSummary, Education, WorkExperience, AchieveAccomplish, memberships, Projects
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import skillsForm, projectForm, experienceForm, achievementForm

# Create your views here.
def cv_sectionList(request):
    return render(request, 'cv/cv_sectionList.html')

def skillsSummaryPage(request):
    skills = skillSummary.objects.all()
    return render(request, 'cv/skills_main.html', {'skills' : skills[0]})

@login_required
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




def projects(request):
    proj = Projects.objects.order_by('-projectDate')
    return render(request, 'cv/projects_main.html', {'projects' : proj})

@login_required
def projects_detail(request, pk):
    proj = get_object_or_404(Projects, pk=pk)
    return render(request, 'cv/projects_Entry_Detail.html', {'proj': proj})

@login_required
def projects_edit(request, pk):
    proj = get_object_or_404(Projects, pk=pk)
    if request.method == "POST":
        form = projectForm(request.POST, instance=proj)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.author = request.user
            proj.save()
            return redirect('projects_detail', pk=proj.pk)
    else:
        form = projectForm(instance=proj)
    return render(request, 'cv/projects_edit.html', {'form': form})


@login_required
def projects_new(request):
    if request.method == "POST":
        form = projectForm(request.POST)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.author = request.user
            proj.save()
            return redirect('projects_detail', pk=proj.pk)
    else:
        form = projectForm()
    return render(request, 'cv/projects_edit.html', {'form': form})


@login_required
def projects_remove(request, pk):
    proj = get_object_or_404(Projects, pk=pk)
    proj.delete()
    return redirect('projectsPage')



def workExperiencePage(request):
    experiences = WorkExperience.objects.order_by('-startDate')
    return render(request, 'cv/workExperience_main.html', {'experiences' : experiences})

@login_required
def WorkExperience_detail(request, pk):
    experiences = get_object_or_404(WorkExperience, pk=pk)
    return render(request, 'cv/workExperience_Entry_Detail.html', {'experiences': experiences})

@login_required
def WorkExperience_edit(request, pk):
    experiences = get_object_or_404(WorkExperience, pk=pk)
    if request.method == "POST":
        form = experienceForm(request.POST, instance=experiences)
        if form.is_valid():
            experiences = form.save(commit=False)
            experiences.author = request.user
            experiences.save()
            return redirect('WorkExperience_detail', pk=experiences.pk)
    else:
        form = experienceForm(instance=experiences)
    return render(request, 'cv/workExperience_edit.html', {'form': form})


@login_required
def WorkExperience_new(request):
    if request.method == "POST":
        form = experienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.author = request.user
            experience.save()
            return redirect('WorkExperience_detail', pk=experience.pk)
    else:
        form = experienceForm()
    return render(request, 'cv/workExperience_edit.html', {'form': form})


@login_required
def WorkExperience_remove(request, pk):
    experience = get_object_or_404(WorkExperience, pk=pk)
    experience.delete()
    return redirect('workExperiencePage')




def achieveAccomplish(request):
    achievements = AchieveAccomplish.objects.order_by('-dateAchieved')
    return render(request, 'cv/achievements_main.html', {'achievements' : achievements})

@login_required
def achieve_detail(request, pk):
    achieve = get_object_or_404(AchieveAccomplish, pk=pk)
    return render(request, 'cv/achievement_Entry_detail.html', {'achievements': achieve})

@login_required
def achieve_edit(request, pk):
    achievements = get_object_or_404(AchieveAccomplish, pk=pk)
    if request.method == "POST":
        form = achievementForm(request.POST, instance=achievements)
        if form.is_valid():
            achievements = form.save(commit=False)
            achievements.author = request.user
            achievements.save()
            return redirect('achievement_detail', pk=achievements.pk)
    else:
        form = achievementForm(instance=achievements)
    return render(request, 'cv/achievement_edit.html', {'form': form})


@login_required
def achieve_new(request):
    if request.method == "POST":
        form = achievementForm(request.POST)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.author = request.user
            achievement.save()
            return redirect('achievement_detail', pk=achievement.pk)
    else:
        form = achievementForm()
    return render(request, 'cv/achievement_edit.html', {'form': form})


@login_required
def achieve_remove(request, pk):
    achievement = get_object_or_404(AchieveAccomplish, pk=pk)
    achievement.delete()
    return redirect('achievementsPage')




def educationPage(request):
	gcses = Education.objects.filter(edu_type='GCSE')
	AS = Education.objects.filter(edu_type='AS-Level')
	A = Education.objects.filter(edu_type='A-Level')
	uni = Education.objects.filter(edu_type='Degree')
	return render(request, 'cv/Education_main.html', {'gcses' : gcses, 'AS_Levels' : AS, 'A_Levels' : A, 'uni' : uni})


def Memberships(request):
    membs = memberships.objects.order_by('-dateMembership')
    return render(request, 'cv/memberships_main.html', {'membs' : membs})



