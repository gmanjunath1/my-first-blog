from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_sectionList, name='cv_sectionList'),
    path('SkillSummary/', views.skillsSummaryPage, name='summarySkillsPage'),
    path('SkillSummary/<int:pk>/', views.skills_detail, name='skills_detail'),
    path('SkillSummary/<int:pk>/edit/', views.skills_edit, name='skills_edit'),
    path('Education', views.educationPage, name='EducationPage'),
    path('WorkExperience', views.workExperiencePage, name='workExperiencePage'),
    path('Achievements', views.achieveAccomplish, name='achievementsPage'),
    path('Memberships', views.Memberships, name='membershipsPage'),
    path('Projects', views.projects, name='projectsPage'),
    path('Projects/<int:pk>/', views.projects_detail, name='projects_detail'),
    path('Projects/new/', views.projects_new, name='projects_new'),
    path('Projects/<int:pk>/edit/', views.projects_edit, name='projects_edit'),
    path('Projects/<pk>/remove/', views.projects_remove, name='projects_remove'),
]

