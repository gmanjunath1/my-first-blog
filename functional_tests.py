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

    	#Test to see if a guest user can access the CV Sections Page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()
        self.assertIn('CV', self.browser.title) 

        #Test to see if guest user can see all the correct sections in the CV section page
        CVSections = self.browser.find_elements_by_tag_name('h2')
        self.assertTrue(any(CVSection.text == 'Summary of Skills' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Education History' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Projects' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Work Experience & Professional Courses' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Achievements & Accomplishments' for CVSection in CVSections))
        self.assertTrue(any(CVSection.text == 'Memberships & Extra-Curricular' for CVSection in CVSections))

    def test_admin_can_log_in_and_log_out(self):

    	#Admin goes to CV page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()

        #Admin looks for login button
        self.browser.find_element_by_css_selector('span.glyphicon-lock').click()

        #Checks whether login page is returned
        self.assertIn('Login', self.browser.title) 
        time.sleep(1)

        #Admin enters credentials
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()
        time.sleep(1)

        #Finds top menu bar and sees whether it says that user is logged in
        menuBar = self.browser.find_element_by_tag_name('p')
        self.assertIn("Logged in:", menuBar.text)

        #Checks the user is returned to home-blog page after logging in
        self.assertIn('Blog', self.browser.title) 

        #Admin looks for logout button
        self.browser.find_element_by_css_selector('span.glyphicon-log-out').click()

        #Finds top menu bar and checks that it no longer says that user is logged in
        menuBars = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
             any("Logged in:" in menuBar.text for menuBar in menuBars)
         )

    def test_admin_can_edit_skills_page(self):

    	#Admin goes to main CV page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()

        #Finds the Skills section link and clicks it
        self.browser.find_element_by_id('skills_button').click()

        #Finds the skill summary header and clicks it to see the details
        self.browser.find_element_by_id('skills_summary_detail').click()

        #Should now ask user to login, and user enters credentials
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()

        #User wants to edit this section, so finds the edit button
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        #Finds the form for Skills, and clears the current entry
        skillsText = self.browser.find_element_by_id('id_text')
        skillsText.clear()

        #Enters the text "This is a summary of my skills!" into the text box and saves
        skillsText.send_keys("This is a summary of my skills!")
        self.browser.find_element_by_class_name('save').submit()

        #Checks that the form has been updated, and the Skills Section is showing the updated text
        potentialSkills = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is a summary of my skills!" in potentialSkill.text for potentialSkill in potentialSkills)
        )

    def test_admin_can_edit_education_page(self):

    	#User goes to main CV page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()

        #User finds the Education link in the CV section menu
        self.browser.find_element_by_id('edu_button').click()

        #User finds the degree post and wants to edit it - they click the link
        self.browser.find_element_by_id('degree_detail').click()

        #User is asked to enter login details, so they enter their credentials
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()

        #User finds and clicks the edit button
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        #User edits the degree subject in the form - they clear the current entry and enter "Computer Science BSc"
        subjectName = self.browser.find_element_by_id('id_subject')
        subjectName.clear()
        subjectName.send_keys("Computer Science BSc")

        #User edits the degree grade in the form - they clear the current entry and choose "First Class" from the drop down menu
        grade = self.browser.find_element_by_id('id_gradeAchieved')
        for option in grade.find_elements_by_tag_name('option'):
            if option.text == 'First Class':
                option.click() 
                break

        #User edits the date achieved in the form - they clear the current entry and enter 1st July 2020
        date = self.browser.find_element_by_id('id_dateAchieved')
        date.clear()
        date.send_keys("2020-07-01")

        #User edits the extraInfo in the form - they clear the current entry and enter "Graduated UoB with a First Class!"
        extraInfo = self.browser.find_element_by_id('id_extraInfo')
        extraInfo.clear()
        extraInfo.send_keys("Graduated UoB with a First Class!")

        #The form is saved
        self.browser.find_element_by_class_name('save').submit()

        #Checks that the form has been updated bu checking the extraInfo shown on the degree in the Education section of the CV page
        potentialDegrees = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("Graduated UoB with a First Class!" in potentialDegree.text for potentialDegree in potentialDegrees)
        )


    def test_admin_can_edit_add_delete_project_page(self):

    	#User goes to the main CV page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()

        #User finds the link to the projects page in the CV menu and clicks it
        self.browser.find_element_by_id('proj_button').click()

        #User finds the project that they want to edit and clicks the link
        self.browser.find_element_by_id('proj_detail').click()

        #User is asked to login so they enter the credentials
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()

        #User sees the edit button and clicks it
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        #User finds the entry form for the project name and clears it - enter "Team Project - Alien8"
        projectName = self.browser.find_element_by_id('id_projectName')
        projectName.clear()
        projectName.send_keys("Team Project - Alien8")

        #User finds the entry form for the project date and clears it - enters July 1st 2020
        date = self.browser.find_element_by_id('id_projectDate')
        date.clear()
        date.send_keys("2020-07-01")

        #User finds the entry form for the project description and clears it - enters "This is the description to our alien8 team project!"
        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("This is the description to our alien8 team project!")

        #Saves the updated form
        self.browser.find_element_by_class_name('save').submit()

        #Checks the projects page to see if the descritpion has been updated
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is the description to our alien8 team project!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        #User now goes to the projects page
        self.browser.get('http://127.0.0.1:8000/cv/Projects')

        #User wants to add a new project post so clicks the add button
        self.browser.find_element_by_css_selector('span.glyphicon-plus').click()


        #User enters the project name "My brand new 2020 project!"
        projectName = self.browser.find_element_by_id('id_projectName')
        projectName.clear()
        projectName.send_keys("My brand nw 2020 project!")

        #User enters the project date as 10th October 2020
        date = self.browser.find_element_by_id('id_projectDate')
        date.clear()
        date.send_keys("2020-10-10")

        #User enters the proejct description as "This is my new project that I have been working on during lockdown."
        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("This is my new project that I have been working on during lockdown.")

        #User saves the new project post
        self.browser.find_element_by_class_name('save').submit()

        #User then goes back to the projects page and checks if the new post has been added
        self.browser.get('http://127.0.0.1:8000/cv/Projects')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is my new project that I have been working on during lockdown." in potentialDesc.text for potentialDesc in potentialDescs)
        )

        #User now wants to remove this post that they have just added, so they find the remove button and click it
        self.browser.find_element_by_id('proj_detail').click()
        self.browser.find_element_by_css_selector('span.glyphicon-remove').click()

        #User goes back to the project page to see if the new post they added has been successfully removed
        self.browser.get('http://127.0.0.1:8000/cv/Projects')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
            any("This is my new project that I have been working on during lockdown." in potentialDesc.text for potentialDesc in potentialDescs)
        )

    def test_admin_can_edit_add_delete_workExperience_page(self):

    	#User goes to main CV page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()

        #User finds the link to the Work Experience page through thr CV menu
        self.browser.find_element_by_id('work_button').click()

        #User clicks a work experience post to see the details
        self.browser.find_element_by_id('work_detail').click()

        #User is asked to login so they enter the correct credentials
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()

        #User wants to edit this current Work Experience post so they click the edit button
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        #User finds the entry for the company name and clears the contents - they change it to "Barclays Bank"
        companyName = self.browser.find_element_by_id('id_companyName')
        companyName.clear()
        companyName.send_keys("Barclays Bank")

        #User finds the entry for the start date and clears the contents - they change it to 1st July 2020
        startdate = self.browser.find_element_by_id('id_startDate')
        startdate.clear()
        startdate.send_keys("2020-07-01")

        #user finds the entry for the location and clears the contents - they change it to Glasgow, Scotland
        location = self.browser.find_element_by_id('id_location')
        location.clear()
        location.send_keys("Glasgow, Scotland")

        #user finds the entry for the duration and clears the contents - they change it to 6 weeks
        duration = self.browser.find_element_by_id('id_duration')
        duration.clear()
        duration.send_keys("6 Weeks")

        # User finds the entry for the extra information and clears the contents - they change
        # it to "This is the description to my internship at Barclays, Glasgow as a Summer Developer!"
        extraInfo = self.browser.find_element_by_id('id_extraInfo')
        extraInfo.clear()
        extraInfo.send_keys("This is the description to my internship at Barclays, Glasgow as a Summer Developer!")

        # user saves the updated form
        self.browser.find_element_by_class_name('save').submit()

        #user goes and checks that the form has been updated on the Work Experience page
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is the description to my internship at Barclays, Glasgow as a Summer Developer!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        #User goes to the work experience page and wants to add a new work experience - they find and click the plus icon
        self.browser.get('http://127.0.0.1:8000/cv/WorkExperience')
        self.browser.find_element_by_css_selector('span.glyphicon-plus').click()

        #User enters company name Morgan Stanley
        companyName = self.browser.find_element_by_id('id_companyName')
        companyName.clear()
        companyName.send_keys("Morgan Stanley")

        # User enters start date July 1st 2022
        startdate = self.browser.find_element_by_id('id_startDate')
        startdate.clear()
        startdate.send_keys("2022-07-01")

        #User enters location London, England
        location = self.browser.find_element_by_id('id_location')
        location.clear()
        location.send_keys("London, England")

        #User enters the duration as 10 weeks
        duration = self.browser.find_element_by_id('id_duration')
        duration.clear()
        duration.send_keys("10 Weeks")

        #user enters the description of the work experience
        extraInfo = self.browser.find_element_by_id('id_extraInfo')
        extraInfo.clear()
        extraInfo.send_keys("This is the description to my internship at Morgan Stanley as a Summer Developer!")

        #User saves the new work experience form
        self.browser.find_element_by_class_name('save').submit()

        #User goes to main cv page to check if the post if visible
        self.browser.get('http://127.0.0.1:8000/cv/WorkExperience')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is the description to my internship at Morgan Stanley as a Summer Developer!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        #User now wnats to delete this new post so they click the post and click the remove button
        self.browser.find_element_by_id('work_detail').click()
        self.browser.find_element_by_css_selector('span.glyphicon-remove').click()

        #user now goes back to the work experience page to see if the post has been removed
        self.browser.get('http://127.0.0.1:8000/cv/WorkExperience')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
            any("This is the description to my internship at Morgan Stanley as a Summer Developer!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

    def test_admin_can_edit_add_delete_achievements_page(self):

    	#User goes to the main cv page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()

        #user clicks the link to the achievements page in the cv menu
        self.browser.find_element_by_id('achievement_button').click()

        #user clicks an achievement on the page to view in detail
        self.browser.find_element_by_id('achievement_detail').click()

        #user is prompted to login so they enter their credentials
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()

        #User wants to edit the post so they click the edit button
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        #User clears the entry for the title and enters a new title
        titleAch = self.browser.find_element_by_id('id_titleAch')
        titleAch.clear()
        titleAch.send_keys("This is the updated achievement")

        #User clears the entry for the date and enters a new date
        dateAch = self.browser.find_element_by_id('id_dateAchieved')
        dateAch.clear()
        dateAch.send_keys("2019-07-01")

        #User clears the entry for description and enters a new description
        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("This is the new updated achievement!")

        #User saves updated post
        self.browser.find_element_by_class_name('save').submit()

        #User then checks if the post has been updated correctly on the achievements page
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is the new updated achievement!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        #User goes to the achievemnts page and wants to add a new achievement
        self.browser.get('http://127.0.0.1:8000/cv/Achievements')
        self.browser.find_element_by_css_selector('span.glyphicon-plus').click()

        #User enters a new title in the title entry form
        titleAch = self.browser.find_element_by_id('id_titleAch')
        titleAch.clear()
        titleAch.send_keys("New Achievement!!!")

        #user enters new date in the date entry form
        dateAch = self.browser.find_element_by_id('id_dateAchieved')
        dateAch.clear()
        dateAch.send_keys("2020-07-01")

        #user enters a new desfription in the description entry form
        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("WOW! Look I got a new achievement!")

        #user saves the new post
        self.browser.find_element_by_class_name('save').submit()

        #user goes to the ahcievements page and checks if the new post is visible
        self.browser.get('http://127.0.0.1:8000/cv/Achievements')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("WOW! Look I got a new achievement!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        #user now wants to remove the new post so they click the post and then click the remove icon
        self.browser.find_element_by_id('achievement_detail').click()
        self.browser.find_element_by_css_selector('span.glyphicon-remove').click()

        #user then goes back to the achievements page to see if the post has been removed
        self.browser.get('http://127.0.0.1:8000/cv/Achievements')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
            any("WOW! Look I got a new achievement!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

    def test_admin_can_edit_add_delete_memberships_page(self):

    	#user goes to main cv page
        self.browser.get('http://127.0.0.1:8000/cv')
        self.browser.maximize_window()

        #user finds and clicks the membership link to the membership page
        self.browser.find_element_by_id('membership_button').click()

        #user clicks the link to view a post in detail
        self.browser.find_element_by_id('membership_detail').click()

        #user is prompted to login so they enter their credentials
        self.browser.find_element_by_id('id_username').send_keys("gautam")
        self.browser.find_element_by_id('id_password').send_keys("Testing789")
        self.browser.find_element_by_tag_name('input').submit()

        #User wants to edit this post so they click the edit button
        self.browser.find_element_by_css_selector('span.glyphicon-pencil').click()

        #They clear the entry form for membership name and enter an updated name
        membershipName = self.browser.find_element_by_id('id_membershipName')
        membershipName.clear()
        membershipName.send_keys("This is the updated membership")

        #user clears the entry form for date and enters an updated date
        dateMembership = self.browser.find_element_by_id('id_dateMembership')
        dateMembership.clear()
        dateMembership.send_keys("2019-07-01")

        #user clears the entry for the description and enters an updated description
        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("This is my updated membership description - hope you enjoy!")

        #user saves updated form
        self.browser.find_element_by_class_name('save').submit()

        #user checks if updates are showing correctly in main page
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("This is my updated membership description - hope you enjoy!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        #user goes to main memberhsips page and wants to add a new membership post - they click the add button
        self.browser.get('http://127.0.0.1:8000/cv/Memberships')
        self.browser.find_element_by_css_selector('span.glyphicon-plus').click()

        #they enter a new name in the name entry box
        membershipName = self.browser.find_element_by_id('id_membershipName')
        membershipName.clear()
        membershipName.send_keys("This is the new membership")

        #they enter a new date in the date entry box
        dateMembership = self.browser.find_element_by_id('id_dateMembership')
        dateMembership.clear()
        dateMembership.send_keys("2020-07-01")

        #they enter a new description in the description entry box
        desc = self.browser.find_element_by_id('id_description')
        desc.clear()
        desc.send_keys("WOW! Look I got a new membership!")

        #user saves new post
        self.browser.find_element_by_class_name('save').submit()

        #user goes back to memberships page to see if new post has been added correctly
        self.browser.get('http://127.0.0.1:8000/cv/Memberships')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertTrue(
            any("WOW! Look I got a new membership!" in potentialDesc.text for potentialDesc in potentialDescs)
        )

        #user now wants to rmeove this post that they just added, so they click the post and click the remove button
        self.browser.find_element_by_id('membership_detail').click()
        self.browser.find_element_by_css_selector('span.glyphicon-remove').click()

        #user then goes back to the memberships page to see if the post has been removed correctly
        self.browser.get('http://127.0.0.1:8000/cv/Memberships')
        potentialDescs = self.browser.find_elements_by_tag_name('p')
        self.assertFalse(
            any("WOW! Look I got a new membership!" in potentialDesc.text for potentialDesc in potentialDescs)
        )
        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')