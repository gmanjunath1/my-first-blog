from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from cv.views import cv_menu  

class CVTest(TestCase):

    def test_root_url_resolves_to_CV_menu_view(self):
        found = resolve('/cv')  
        self.assertEqual(found.func, cv_menu)


    def test_CV_menu_returns_correct_html(self):
        request = HttpRequest()  
        response = cv_menu(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn("<title>Gautam's CV</title>", html)  
        self.assertTrue(html.endswith('</html>'))