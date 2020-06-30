from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from cv.views import cv_sectionList  
from cv.models import skillSummary, Education, WorkExperience, AchieveAccomplish, memberships, Projects
import datetime
from django.contrib.auth.models import User

class CV_menuSecionTest(TestCase):

    def test_CV_section_page_uses_correct_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv_sectionList.html')

class CV_educationSecionTest(TestCase):

    def test_Education_page_uses_correct_template(self):
        response = self.client.get('/cv/Education')
        self.assertTemplateUsed(response, 'cv/Education_main.html')

class CV_skillsSecionTest(TestCase):

    def test_Skills_page_uses_correct_template(self):
        response = self.client.get('/cv/SkillSummary')
        self.assertTemplateUsed(response, 'cv/skills_main.html')

class CV_WorkExperienceSecionTest(TestCase):

    def test_WorkExperience_page_uses_correct_template(self):
        response = self.client.get('/cv/WorkExperience')
        self.assertTemplateUsed(response, 'cv/workExperience_main.html')

class CV_projectsSecionTest(TestCase):

    def test_Projects_page_uses_correct_template(self):
        response = self.client.get('/cv/Projects')
        self.assertTemplateUsed(response, 'cv/projects_main.html')

class CV_achievementsSecionTest(TestCase):

    def test_Achievements_page_uses_correct_template(self):
        response = self.client.get('/cv/Achievements')
        self.assertTemplateUsed(response, 'cv/achievements_main.html')

class CV_membershipSecionTest(TestCase):

    def test_Memberships_page_uses_correct_template(self):
        response = self.client.get('/cv/Memberships')
        self.assertTemplateUsed(response, 'cv/memberships_main.html')

class TestSkillsSummaryModel(TestCase):

    def test_saving_and_retrieving_SkillSummary(self):

        user = User.objects.create_superuser('myuser', 'myemail@text.com', 'Testing789')
        summary = skillSummary()
        summary.author = user
        summary.text = "This is my summary of skills!"
        summary.save()

        saved_items = skillSummary.objects.all()
        self.assertEqual(saved_items.count(), 1)

        test_summary = saved_items[0]
        self.assertEqual(test_summary.text, "This is my summary of skills!")

class TestEducationModel(TestCase):

    def test_saving_and_retrieving_Different_Education(self):

        user = User.objects.create_superuser('myuser', 'myemail@text.com', 'Testing789')
        gcse1 = Education()
        gcse1.author = user
        gcse1.edu_type = 'GCSE' 
        gcse1.subject = "Mathematics"
        gcse1.gradeAchieved = 'A*'
        gcse1.dateAchieved = "2016-01-01"
        gcse1.extraInfo = "This is the first GCSE!"
        gcse1.save()

        saved_items = Education.objects.all()
        self.assertEqual(saved_items.count(), 1)

        test_gcse = saved_items[0]
        self.assertEqual(test_gcse.edu_type, 'GCSE')
        self.assertEqual(test_gcse.subject, 'Mathematics')
        self.assertEqual(test_gcse.gradeAchieved, 'A*')
        self.assertEqual(test_gcse.dateAchieved, datetime.date(2016, 1, 1))
        self.assertEqual(test_gcse.extraInfo, 'This is the first GCSE!')

        AS1 = Education()
        AS1.author = user
        AS1.edu_type = 'AS-Level' 
        AS1.subject = "Physics"
        AS1.gradeAchieved = 'A'
        AS1.dateAchieved = "2017-09-01"
        AS1.extraInfo = "This is the first AS-Level!"
        AS1.save()

        saved_items = Education.objects.all()
        self.assertEqual(saved_items.count(), 2)

        test_AS = saved_items[1]
        self.assertEqual(test_AS.edu_type, 'AS-Level')
        self.assertEqual(test_AS.subject, 'Physics')
        self.assertEqual(test_AS.gradeAchieved, 'A')
        self.assertEqual(test_AS.dateAchieved, datetime.date(2017, 9, 1))
        self.assertEqual(test_AS.extraInfo, 'This is the first AS-Level!')

        A1 = Education()
        A1.author = user
        A1.edu_type = 'A-Level' 
        A1.subject = "English Literature"
        A1.gradeAchieved = 'C'
        A1.dateAchieved = "2018-10-01"
        A1.extraInfo = "This is the first A-Level!"
        A1.save()

        saved_items = Education.objects.all()
        self.assertEqual(saved_items.count(), 3)

        test_A = saved_items[2]
        self.assertEqual(test_A.edu_type, 'A-Level')
        self.assertEqual(test_A.subject, 'English Literature')
        self.assertEqual(test_A.gradeAchieved, 'C')
        self.assertEqual(test_A.dateAchieved, datetime.date(2018, 10, 1))
        self.assertEqual(test_A.extraInfo, 'This is the first A-Level!')

        btec = Education()
        btec.author = user
        btec.edu_type = 'BTEC' 
        btec.subject = "Mechanical Engineering"
        btec.gradeAchieved = 'Pass'
        btec.dateAchieved = "2019-02-17"
        btec.extraInfo = "This is the first BTEC!"
        btec.save()

        saved_items = Education.objects.all()
        self.assertEqual(saved_items.count(), 4)

        test_btec = saved_items[3]
        self.assertEqual(test_btec.edu_type, 'BTEC')
        self.assertEqual(test_btec.subject, 'Mechanical Engineering')
        self.assertEqual(test_btec.gradeAchieved, 'Pass')
        self.assertEqual(test_btec.dateAchieved, datetime.date(2019, 2, 17))
        self.assertEqual(test_btec.extraInfo, 'This is the first BTEC!')

        degree = Education()
        degree.author = user
        degree.edu_type = 'Degree' 
        degree.subject = "Computer Science"
        degree.gradeAchieved = 'Current Studies'
        degree.dateAchieved = "2022-07-17"
        degree.extraInfo = "This is the first Degree!"
        degree.save()

        saved_items = Education.objects.all()
        self.assertEqual(saved_items.count(), 5)

        test_degree = saved_items[4]
        self.assertEqual(test_degree.edu_type, 'Degree')
        self.assertEqual(test_degree.subject, 'Computer Science')
        self.assertEqual(test_degree.gradeAchieved, 'Current Studies')
        self.assertEqual(test_degree.dateAchieved, datetime.date(2022, 7, 17))
        self.assertEqual(test_degree.extraInfo, 'This is the first Degree!')

class TestEducationModel(TestCase):

    def test_saving_and_retrieving_WorkExperience(self):
        user = User.objects.create_superuser('myuser', 'myemail@text.com', 'Testing789')
        workExp = WorkExperience()
        workExp.author = user
        workExp.companyName = 'Barclays' 
        workExp.location = "Northampton, England"
        workExp.duration = '6 Weeks'
        workExp.startDate = "2020-06-10"
        workExp.extraInfo = "This is my first job!"
        workExp.save()

        saved_items = WorkExperience.objects.all()
        self.assertEqual(saved_items.count(), 1)

        test_summary = saved_items[0]
        self.assertEqual(test_summary.companyName, 'Barclays')
        self.assertEqual(test_summary.location, "Northampton, England")
        self.assertEqual(test_summary.duration, '6 Weeks')
        self.assertEqual(test_summary.startDate, datetime.date(2020, 6, 10))
        self.assertEqual(test_summary.extraInfo, 'This is my first job!')

class TestAccomplishModel(TestCase):

    def test_saving_and_retrieving_Accomplishments(self):
        user = User.objects.create_superuser('myuser', 'myemail@text.com', 'Testing789')
        achieve = AchieveAccomplish()
        achieve.author = user
        achieve.titleAch = 'Keyboard Grade 8' 
        achieve.dateAchieved = "2017-01-19"
        achieve.description = 'Achieved Distinction'
        achieve.save()

        saved_items = AchieveAccomplish.objects.all()
        self.assertEqual(saved_items.count(), 1)

        test_achieve = saved_items[0]
        self.assertEqual(test_achieve.titleAch, 'Keyboard Grade 8' )
        self.assertEqual(test_achieve.dateAchieved, datetime.date(2017, 1, 19))
        self.assertEqual(test_achieve.description, 'Achieved Distinction')

class TestMembershipsModel(TestCase):

    def test_saving_and_retrieving_Memberships(self):
        user = User.objects.create_superuser('myuser', 'myemail@text.com', 'Testing789')
        memb = memberships()
        memb.author = user
        memb.membershipName = 'School football team' 
        memb.dateMembership = "2013-10-28"
        memb.description = 'Played as a defender for 2 years'
        memb.save()

        saved_items = memberships.objects.all()
        self.assertEqual(saved_items.count(), 1)

        test_memb = saved_items[0]
        self.assertEqual(test_memb.membershipName, 'School football team'  )
        self.assertEqual(test_memb.dateMembership, datetime.date(2013, 10, 28))
        self.assertEqual(test_memb.description, 'Played as a defender for 2 years')

class TestProjectsModel(TestCase):

    def test_saving_and_retrieving_Projects(self):
        user = User.objects.create_superuser('myuser', 'myemail@text.com', 'Testing789')
        proj = Projects()
        proj.author = user
        proj.projectName = "2nd Year CS Team Project"
        proj.projectDate = "2020-04-01"
        proj.description = '20 credit module team project of 6 people'
        proj.save()

        saved_items = Projects.objects.all()
        self.assertEqual(saved_items.count(), 1)

        test_proj = saved_items[0]
        self.assertEqual(test_proj.projectName, "2nd Year CS Team Project" )
        self.assertEqual(test_proj.projectDate, datetime.date(2020, 4, 1))
        self.assertEqual(test_proj.description, '20 credit module team project of 6 people')