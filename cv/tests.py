from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from cv.views import cv_sectionList  

class CVTest(TestCase):

    def test_CV_section_page_uses_correct_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_sectionList.html')

    def test_Education_page_uses_correct_template(self):
        response = self.client.get('/cv/Education')
        self.assertTemplateUsed(response, 'cv/Education_main.html')

    def test_Skills_page_uses_correct_template(self):
        response = self.client.get('/cv/SkillSummary')
        self.assertTemplateUsed(response, 'cv/skills_main.html')

    def test_WorkExperience_page_uses_correct_template(self):
        response = self.client.get('/cv/WorkExperience')
        self.assertTemplateUsed(response, 'cv/workExperience_main.html')

    def test_Projects_page_uses_correct_template(self):
        response = self.client.get('/cv/Projects')
        self.assertTemplateUsed(response, 'cv/projects_main.html')

    def test_Achievements_page_uses_correct_template(self):
        response = self.client.get('/cv/Achievements')
        self.assertTemplateUsed(response, 'cv/achievements_main.html')

    def test_Memberships_page_uses_correct_template(self):
        response = self.client.get('/cv/Memberships')
        self.assertTemplateUsed(response, 'cv/memberships_main.html')