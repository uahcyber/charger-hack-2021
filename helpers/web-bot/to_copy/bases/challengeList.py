from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import sys

class Challenge:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',options=opts)
    
    def open_path_with_cookie(self, path, cookie):
        try:
            self.driver.get(self.url + "/404040404")
            browser_cookies = [{'name': k, 'value': v} for k, v in cookie.items()]
            for c in browser_cookies:
                self.driver.add_cookie(c)
            self.driver.get(self.url + path)
        except:
            pass

class ChallengeList:

    challs = []

    def __init__(self,challs=None):
        if challs != None:
            self.challs = challs

    def append(self,chall):
        self.challs.append(chall)
    
    def getFromURL(self,url):
        for c in self.challs:
            if c.url == url:
                return c
        return None
    
    def getFromName(self,name):
        for c in self.challs:
            if c.name == name:
                return c
        return None