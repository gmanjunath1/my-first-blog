from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_sectionList, name='cv_sectionList'),
    path('SkillSummary', views.skillsSummaryPage, name='summarySkillsPage'),
    path('Education', views.educationPage, name='EducationPage'),
    path('WorkExperience', views.workExperiencePage, name='workExperiencePage'),
    path('Achievements', views.achieveAccomplish, name='achievementsPage'),
    path('Memberships', views.Memberships, name='membershipsPage'),
    path('Projects', views.projects, name='projectsPage'),
]

