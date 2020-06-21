from selenium import webdriver

browser = webdriver.Edge()
browser.get('http://127.0.0.1:8000')

assert 'Gautam' in browser.title 