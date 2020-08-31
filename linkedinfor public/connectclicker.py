from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from secrets import email, password
from time import sleep
browser = webdriver.Firefox()
class LinkedInBot():

    def csvwork(self):
        import csv
        # f = open('friends.csv')
        # csv_f = csv.reader(f)
        # for row in csv_f:
        #     print row[1]


    def commenceClicking2(self):
            # browser = webdriver.Chrome(executable_path="C:\\Users\\James\\Documents\\PythonScripts\\chromedriver.exe")
            import re
            anames = []
            with open("friends.csv",'r') as readeri:
                for line in readeri:
                    anames.append(line)
                # print(anames)
            url = "https://www.google.com"
            # # browser.get(url)


            browser.maximize_window()
        # browser = webdriver.Firefox()
            browser.get(url)
            search = browser.find_element_by_name('q')
            search.send_keys("Linkedin ",anames[1])
            search.send_keys(Keys.RETURN) # hit return after you enter search text
            sleep(5)
            browser.find_element_by_tag_name('h3').click()
            sleep(5)
            browser.get('https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fin%2Fspencer-taylor-76431344&fromSignIn=true&trk=public_authwall_profile-login-link')
            sleep(2)
            browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input').send_keys("", email)

            browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input').send_keys("", password, Keys.ENTER)
            sleep(5)
            for i in anames:
                browser.maximize_window()
            # browser = webdriver.Firefox()
                browser.get(url)
                search = browser.find_element_by_name('q')
                search.send_keys("Linkedin ",i)
                search.send_keys(Keys.RETURN) # hit return after you enter search text
                sleep(3)
                browser.find_element_by_tag_name('h3').click()
                sleep(3)
                try:
                    try:
                        connectbuttons = browser.find_elements_by_tag_name('span')
                        for x in range(0, len(connectbuttons)):
                            if connectbuttons[x].is_displayed():
                                if connectbuttons[x].get_property('innerText') == "Connect":
                                    connectbuttons[x].click()
                                    sleep(1)
                    except StaleElementReferenceException:
                        sleep(5)
                except:
                    sleep(3)
                    print(aname[i])


    def login(self):
        browser.get('https://linkedin.com')

        sign_in = browser.find_element_by_xpath('/html/body/nav/a[3]')
        sign_in.click()

        browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input').send_keys("", email)

        browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input').send_keys("", password, Keys.ENTER)

    def commenceClicking(self):

            browser.maximize_window()
            browser.find_element_by_xpath('//*[@id="mynetwork-tab-icon"]').click()

            sleep(5)


            while True:
                try:
                    connectbuttons = browser.find_elements_by_tag_name('span')
                    for x in range(0, len(connectbuttons)):
                        if connectbuttons[x].is_displayed():
                            if connectbuttons[x].get_property('innerText') == "Connect":
                                connectbuttons[x].click()
                                sleep(0.5)
                except StaleElementReferenceException:
                    sleep(10)
            else:
               for x in range(0, len(connectbuttons)):
                    if connectbuttons[x].is_displayed():
                        if connectbuttons[x].get_property('innerText') == "Connect":
                            connectbuttons[x].click()
                            sleep(0.5)
