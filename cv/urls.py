from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_sectionList, name='cv_sectionList'),
    path('SkillSummary/', views.skillsSummaryPage, name='summarySkillsPage'),
    path('SkillSummary/<int:pk>/', views.skills_detail, name='skills_detail'),
    path('SkillSummary/<int:pk>/edit/', views.skills_edit, name='skills_edit'),
    path('Education', views.educationPage, name='EducationPage'),
    path('WorkExperience', views.workExperiencePage, name='workExperiencePage'),
    path('WorkExperience/<int:pk>/', views.WorkExperience_detail, name='WorkExperience_detail'),
    path('WorkExperience/new/', views.WorkExperience_new, name='WorkExperience_new'),
    path('WorkExperience/<int:pk>/edit/', views.WorkExperience_edit, name='WorkExperience_edit'),
    path('WorkExperience/<pk>/remove/', views.WorkExperience_remove, name='WorkExperience_remove'),
    path('Achievements', views.achieveAccomplish, name='achievementsPage'),
    path('Achievements/<int:pk>/', views.achieve_detail, name='achievement_detail'),
    path('Achievements/new/', views.achieve_new, name='achievement_new'),
    path('Achievements/<int:pk>/edit/', views.achieve_edit, name='achieve_edit'),
    path('Achievements/<pk>/remove/', views.achieve_remove, name='achieve_remove'),
    path('Memberships', views.Memberships, name='membershipsPage'),
    path('Memberships/<int:pk>/', views.membership_detail, name='membership_detail'),
    path('Memberships/new/', views.membership_new, name='membership_new'),
    path('Memberships/<int:pk>/edit/', views.membership_edit, name='membership_edit'),
    path('Memberships/<pk>/remove/', views.membership_remove, name='membership_remove'),
    path('Projects', views.projects, name='projectsPage'),
    path('Projects/<int:pk>/', views.projects_detail, name='projects_detail'),
    path('Projects/new/', views.projects_new, name='projects_new'),
    path('Projects/<int:pk>/edit/', views.projects_edit, name='projects_edit'),
    path('Projects/<pk>/remove/', views.projects_remove, name='projects_remove'),
]

