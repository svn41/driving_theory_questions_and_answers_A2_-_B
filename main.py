################################################ Necessary Libraries ##################################
import os, random, sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import requests

################################################## read credentials  from saved file #######################################

file = open("c:/Users/SVN41/Google Drive/Paython 3/driving_theory_questions_and_answers_A2_-_B/credentials.txt")
lines = file.readlines()
username = lines[0]
password = lines[1]
website = lines[2]
lerning_page = lines[3]
practice_by_topic_page = lines[4]

####################################################### configure chrome driver ##########################################

browser =  webdriver.Chrome(ChromeDriverManager().install())
browser.get(lerning_page)
browser.maximize_window()
time.sleep(4)

##################################################### Login ################################################################

elementID = browser.find_element_by_xpath("//*[@id='frmLogin']/div[5]/input")
elementID.send_keys(username)

elementID = browser.find_element_by_xpath("//*[@id='frmLogin']/div[6]/input")
elementID.send_keys(password)
elementID.submit()
time.sleep(4)

################################################ navigate to desired page##################################################

'''
write code that takes you to your desired page  ex. practice by topic
'''



############################################## Get all chapter name #######################################################
