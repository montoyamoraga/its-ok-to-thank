# its-ok-to-thank
# by aaron montoya-moraga
# project part of my nyu itp thesis
# python script to automate sending thank you emails
# original version april 2017
# revised november 2017
# v1.0.0

# instructions

# install virtualenv on the machine
# pip install virtualenv env

# instantiate a virtual environment
# virtualenv env

# activate the instance of the virtual environment
# source env/binc/activate

# install selenium
# pip install selenium

# to deactivate the virtual environment
# deactivate

# import sys, time, string, json modules
import sys
import time
import string
import json

# import selenium module for web automation
# include webdriver for using chrome and eys for using keyboard commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# global variables for waiting time
waitTime = 1
waitTimeLong = 20

# main function declaration

def main():

    json_file = "./" + sys.argv[1]

    print "read json file for mails"

    # read json file
    json_data = open(json_file).read()

    # load json file to data
    data = json.loads(json_data)

    print "parse info from file mails.json"

    # parse email subject
    subjectEnglish = data["subject"]["english"]
    subjectSpanish = data["subject"]["spanish"]

    # parse email greeting
    greetingEnglish = data["greeting"]["english"]
    greetingSpanish = data["greeting"]["spanish"]

    # parse email body
    bodyEnglish = data["body"]["english"]
    bodySpanish = data["body"]["spanish"]

    print "open google chrome"

    # new driver using google chrome
    driver = webdriver.Chrome()

    # set the window size of the driver
    driver.set_window_size(900, 600)

    print "go to gmail"

    # url
    url = "http://www.gmail.com"

    # go to the url
    driver.get(url)

    # wait
    time.sleep(waitTime)

    # wait
    time.sleep(waitTimeLong)

    print "parse people from file mails.json"

    # parse people
    people = data["people"]

    print "number of people to thank: " + str(len(people))

    # go through every person in people
    for person in people:

        try:
            print "parse name, mail and language"
            # parse name, mail, language
            name = data["people"][person]["name"]
            mail = data["people"][person]["mail"]
            language = data["people"][person]["language"]

            #make name capital letters
            name = name.upper()

            print "retrieve compose button"

            # retrieve compose button
            compose = driver.find_element_by_xpath("//div[@class='z0']/div")

            # wait
            time.sleep(waitTime)

            print "click on compose button"

            # click on compose
            compose.click()

            # wait
            time.sleep(waitTime)

            print "retrieve to element"

            # retrieve to input
            inputTo = driver.find_element_by_name("to")

            print "write mail on to element"

            # write name on to input
            inputTo.send_keys(mail)

            # wait
            time.sleep(waitTime)

            print "hit enter"

            # hit enter
            inputTo.send_keys(Keys.ENTER)

            print "retrieve subject element"

            # retrieve subject input
            inputSubject = driver.find_element_by_name("subjectbox")

            print "write subject on subject element"

            # write subject on subject input
            if language == "english":
                inputSubject.send_keys(subjectEnglish)
            elif (language == "spanish"):
                inputSubject.send_keys(subjectSpanish)

            print "hit enter"

            # hit enter
            inputSubject.send_keys(Keys.ENTER)

            print "retrieve body element"

            # retrieve body input
            inputBody = driver.find_element_by_css_selector(
                "div[aria-label='Message Body']")

            # wait
            time.sleep(waitTime)

            print "write body on body element"

            # write body on body input
            if (language == "english"):
                inputBody.send_keys(greetingEnglish)
                inputBody.send_keys(name)
                inputBody.send_keys(",")
                inputBody.send_keys(Keys.ENTER)
                inputBody.send_keys(bodyEnglish)
            elif (language == "spanish"):
                inputBody.send_keys(greetingSpanish)
                inputBody.send_keys(name)
                inputBody.send_keys(",")
                inputBody.send_keys(Keys.ENTER)
                inputBody.send_keys(bodySpanish)

            # wait
            time.sleep(waitTime)

            sendButton = driver.find_element_by_xpath("//div[text()='Send']")
            sendButton.click()

            # wait
            time.sleep(waitTime)

            # wait
            time.sleep(waitTime)
        except Exception as e:
            print "this mail failed:" + name


    print "thanks! ok bye"

    # to close the browser window
    driver.quit()


# execute main
main()
