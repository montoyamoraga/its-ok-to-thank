# its ok to thank
# by aaron montoya-moraga
# project part of my nyu itp thesis
# python script to automate sending thank you emails
# april 2017
# v0.0.1

# dependencies
# install chromedriver on the machine
# it can be installed with homebrew on mac os x

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
# include webdriver for using chrome and Keys for using keyboard commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# global variables for waiting time
waitTime = 1
waitTimeLong = 6

# main function declaration


def main():

    print "read json file"

    # read json file
    json_data = open("./mails.json").read()

    # load json file to data
    data = json.loads(json_data)

    print "parse info from file mails.json"

    # parse my_mail info
    myMail = data["my_info"]["mail"]
    myPass = data["my_info"]["pass"]

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
    driver.set_window_size(1200, 800)

    print "go to gmail"

    # url
    url = "http://www.gmail.com"

    # go to the url
    driver.get(url)

    # wait
    time.sleep(waitTimeLong)

    print "find input box for mail"

    # retrieve input for mail
    inputMail = driver.find_element_by_id("Email")

    print "write mail"

    # write email on input
    inputMail.send_keys(myMail)

    print "hit enter"

    # hit enter
    inputMail.send_keys(Keys.ENTER)

    # wait
    time.sleep(waitTime)

    print "find input box for password"

    # retrieve input for mail
    inputPass = driver.find_element_by_id("Passwd")

    # wait
    time.sleep(waitTime)

    print "write password"

    # write password on input
    inputPass.send_keys(myPass)

    print "hit enter"

    # hit enter
    inputPass.send_keys(Keys.ENTER)

    # wait
    time.sleep(waitTime)

    print "parse people from file mails.json"

    # parse people
    people = data["people"]

    print "number of people to thank: " + str(len(people))

    # go through every person in people
    for person in people:
        print "parse name, mail and language"
        # parse name, mail, language
        name = data["people"][person]["name"]
        mail = data["people"][person]["mail"]
        language = data["people"][person]["language"]

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

    # to close the browser window
    driver.quit()


# execute main
main()
