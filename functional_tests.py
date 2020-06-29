from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class CV(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Edge()

    def tearDown(self):  
        self.browser.quit()

    def test_guest_can_get_to_CV_section_list_page(self):  

    	#Test to see if user can access the CV Sections Page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.assertIn('CV', self.browser.title) 

        #Test to see if user can see all the correct sections in the CV section page
        CVSections = self.browser.find_elements_by_tag_name('h2')
        self.assertTrue(any(CVSection.text == 'Summary of Skills' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Education History' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Projects' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Work Experience & Professional Courses' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Achievements & Accomplishments' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Memberships & Extra-Curricular' for CVSection in CVSections))

    def test_admin_can_log_in(self):

    	#Tests whether user can login
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.browser.find_element_by_css_selector('span.glyphicon-lock').click()
        self.assertIn('Login', self.browser.title) 
        time.sleep(2)
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        time.sleep(10)
        self.assertIn('Blog', self.browser.title) 

    def test_admin_can_edit_skills_page(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.browser.find_element_by_id('skills_button').click()
        self.browser.find_element_by_id('skills_summary_detail').click()
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()
        skillsText = self.browser.find_element_by_id('id_text')
        skillsText.clear()
        skillsText.send_keys("This is a summary of my skills!")
        self.browser.find_element_by_class_name('save').submit()
        potentialSkills = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is a summary of my skills!" in potentialSkill.text for potentialSkill in potentialSkills)
        )

    def test_admin_can_edit_education_page(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.browser.find_element_by_id('edu_button').click()
        self.browser.find_element_by_id('degree_detail').click()
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()
        subjectName = self.browser.find_element_by_id('id_subject')
        subjectName.clear()
        subjectName.send_keys("Computer Science BSc")

        grade = self.browser.find_element_by_id('id_gradeAchieved')
        for option in grade.find_elements_by_tag_name('option'):
            if option.text == 'First Class':
                option.click() 
                break

        date = self.browser.find_element_by_id('id_dateAchieved')
        date.clear()
        date.send_keys("2020-07-01")

        extraInfo = self.browser.find_element_by_id('id_extraInfo')
        extraInfo.clear()
        extraInfo.send_keys("Graduated UoB with a First Class!")

        self.browser.find_element_by_class_name('save').submit()
        potentialDegrees = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("Graduated UoB with a First Class!" in potentialDegree.text for potentialDegree in potentialDegrees)
        )


    def test_admin_can_edit_add_delete_project_page(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.browser.find_element_by_id('proj_button').click()
        self.browser.find_element_by_id('proj_detail').click()
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        projectName = self.browser.find_element_by_id('id_projectName')
        projectName.clear()
        projectName.send_keys("Team Project - Alien8")

        date = self.browser.find_element_by_id('id_projectDate')
        date.clear()
        date.send_keys("2020-07-01")

        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("This is the description to our alien8 team project!")

        self.browser.find_element_by_class_name('save').submit()
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is the description to our alien8 team project!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        self.browser.get('http://127.0.0.1:8000/cv/Projects')
        self.browser.find_element_by_css_selector('span.glyphicon-plus').click()

        projectName = self.browser.find_element_by_id('id_projectName')
        projectName.clear()
        projectName.send_keys("My brand nw 2020 project!")

        date = self.browser.find_element_by_id('id_projectDate')
        date.clear()
        date.send_keys("2020-10-10")

        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("This is my new project that I have been working on during lockdown.")

        self.browser.find_element_by_class_name('save').submit()
        self.browser.get('http://127.0.0.1:8000/cv/Projects')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is my new project that I have been working on during lockdown." in potentialDesc.text for potentialDesc in potentialDescs)
        )
        self.browser.find_element_by_id('proj_detail').click()
        self.browser.find_element_by_css_selector('span.glyphicon-remove').click()

        self.browser.get('http://127.0.0.1:8000/cv/Projects')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
            any("This is my new project that I have been working on during lockdown." in potentialDesc.text for potentialDesc in potentialDescs)
        )

    def test_admin_can_edit_add_delete_workExperience_page(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.browser.find_element_by_id('work_button').click()
        self.browser.find_element_by_id('work_detail').click()
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        companyName = self.browser.find_element_by_id('id_companyName')
        companyName.clear()
        companyName.send_keys("Barclays Bank")

        startdate = self.browser.find_element_by_id('id_startDate')
        startdate.clear()
        startdate.send_keys("2020-07-01")

        location = self.browser.find_element_by_id('id_location')
        location.clear()
        location.send_keys("Glasgow, Scotland")

        duration = self.browser.find_element_by_id('id_duration')
        duration.clear()
        duration.send_keys("6 Weeks")

        extraInfo = self.browser.find_element_by_id('id_extraInfo')
        extraInfo.clear()
        extraInfo.send_keys("This is the description to my internship at Barclays, Glasgow as a Summer Developer!")

        self.browser.find_element_by_class_name('save').submit()
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is the description to my internship at Barclays, Glasgow as a Summer Developer!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        self.browser.get('http://127.0.0.1:8000/cv/WorkExperience')
        self.browser.find_element_by_css_selector('span.glyphicon-plus').click()

        companyName = self.browser.find_element_by_id('id_companyName')
        companyName.clear()
        companyName.send_keys("Morgan Stanley")

        startdate = self.browser.find_element_by_id('id_startDate')
        startdate.clear()
        startdate.send_keys("2022-07-01")

        location = self.browser.find_element_by_id('id_location')
        location.clear()
        location.send_keys("London, England")

        duration = self.browser.find_element_by_id('id_duration')
        duration.clear()
        duration.send_keys("10 Weeks")

        extraInfo = self.browser.find_element_by_id('id_extraInfo')
        extraInfo.clear()
        extraInfo.send_keys("This is the description to my internship at Morgan Stanley as a Summer Developer!")

        self.browser.find_element_by_class_name('save').submit()
        self.browser.get('http://127.0.0.1:8000/cv/WorkExperience')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is the description to my internship at Morgan Stanley as a Summer Developer!" in potentialDesc.text for potentialDesc in potentialDescs)
        )
        self.browser.find_element_by_id('work_detail').click()
        self.browser.find_element_by_css_selector('span.glyphicon-remove').click()

        self.browser.get('http://127.0.0.1:8000/cv/WorkExperience')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
            any("This is the description to my internship at Morgan Stanley as a Summer Developer!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

    def test_admin_can_edit_add_delete_achievements_page(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.browser.find_element_by_id('achievement_button').click()
        self.browser.find_element_by_id('achievement_detail').click()
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        titleAch = self.browser.find_element_by_id('id_titleAch')
        titleAch.clear()
        titleAch.send_keys("This is the updated achievement")

        dateAch = self.browser.find_element_by_id('id_dateAchieved')
        dateAch.clear()
        dateAch.send_keys("2019-07-01")

        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("This is the new updated achievement!")

        self.browser.find_element_by_class_name('save').submit()
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is the new updated achievement!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        self.browser.get('http://127.0.0.1:8000/cv/Achievements')
        self.browser.find_element_by_css_selector('span.glyphicon-plus').click()

        titleAch = self.browser.find_element_by_id('id_titleAch')
        titleAch.clear()
        titleAch.send_keys("New Achievement!!!")

        dateAch = self.browser.find_element_by_id('id_dateAchieved')
        dateAch.clear()
        dateAch.send_keys("2020-07-01")

        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("WOW! Look I got a new achievement!")

        self.browser.find_element_by_class_name('save').submit()
        self.browser.get('http://127.0.0.1:8000/cv/Achievements')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("WOW! Look I got a new achievement!" in potentialDesc.text for potentialDesc in potentialDescs)
        )
        self.browser.find_element_by_id('achievement_detail').click()
        self.browser.find_element_by_css_selector('span.glyphicon-remove').click()

        self.browser.get('http://127.0.0.1:8000/cv/Achievements')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
            any("WOW! Look I got a new achievement!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

    def test_admin_can_edit_add_delete_memberships_page(self):
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.browser.find_element_by_id('membership_button').click()
        self.browser.find_element_by_id('membership_detail').click()
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        membershipName = self.browser.find_element_by_id('id_membershipName')
        membershipName.clear()
        membershipName.send_keys("This is the updated membership")

        dateMembership = self.browser.find_element_by_id('id_dateMembership')
        dateMembership.clear()
        dateMembership.send_keys("2019-07-01")

        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("This is my updated membership description - hope you enjoy!")

        self.browser.find_element_by_class_name('save').submit()
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is my updated membership description - hope you enjoy!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        self.browser.get('http://127.0.0.1:8000/cv/Memberships')
        self.browser.find_element_by_css_selector('span.glyphicon-plus').click()

        membershipName = self.browser.find_element_by_id('id_membershipName')
        membershipName.clear()
        membershipName.send_keys("This is the new membership")

        dateMembership = self.browser.find_element_by_id('id_dateMembership')
        dateMembership.clear()
        dateMembership.send_keys("2020-07-01")

        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("WOW! Look I got a new membership!")

        self.browser.find_element_by_class_name('save').submit()
        self.browser.get('http://127.0.0.1:8000/cv/Memberships')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("WOW! Look I got a new membership!" in potentialDesc.text for potentialDesc in potentialDescs)
        )
        self.browser.find_element_by_id('membership_detail').click()
        self.browser.find_element_by_css_selector('span.glyphicon-remove').click()

        self.browser.get('http://127.0.0.1:8000/cv/Memberships')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
            any("WOW! Look I got a new membership!" in potentialDesc.text for potentialDesc in potentialDescs)
        )


    def test_admin_can_log_in_and_log_out(self):

    	#Tests whether user can login
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.browser.find_element_by_css_selector('span.glyphicon-lock').click()
        self.assertIn('Login', self.browser.title) 
        time.sleep(1)
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        time.sleep(1)
        menuBar = self.browser.find_element_by_tag_name('p')
        self.assertIn("Logged in:", menuBar.text)
        self.assertIn('Blog', self.browser.title) 
        self.browser.find_element_by_css_selector('span.glyphicon-log-out').click()
        menuBars = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
             any("Logged in:" in menuBar.text for menuBar in menuBars)
         )
        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')