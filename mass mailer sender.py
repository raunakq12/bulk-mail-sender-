from selenium import webdriver
import pyautogui

#please change the chromedriver location to your location

chromedriver_location="/Users/Desktop/chromedriver"

from_name='//*[@id="fromname"]'
from_email='//*[@id="from"]'
subject='//*[@id="subject"]'
to='//*[@id="rcpt"]'
body='//*[@id="text"]'
submit='//*[@id="sendfrm"]/table[3]/tbody/tr[4]/td[2]/input[2]'

# range for sending the mails

numbers=int(input("enter the number of mails to be sent -"))
fromname=pyautogui.prompt('Enter the name to be displayed on the mail -')
fromemail=pyautogui.prompt('Enter the email id from the mail to be sent -')
To=pyautogui.prompt('Enter the recievers mail id -')
sub=pyautogui.prompt('Enter the subject -')
Body=pyautogui.prompt('Enter the body')



driver=webdriver.Chrome(chromedriver_location)
for i in range(numbers):
    driver.get('https://emkei.cz/')

    # enter all the information
    driver.find_element_by_xpath(from_name).send_keys(fromname)
    driver.find_element_by_xpath(from_email).send_keys(fromemail)
    driver.find_element_by_xpath(to).send_keys(To)
    driver.find_element_by_xpath(subject).send_keys(sub)
    driver.find_element_by_xpath(body).send_keys(Body)
    driver.find_element_by_xpath(submit).click()