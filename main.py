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

####################################################### configure chrome driver #########################

browser =  webdriver.Chrome(ChromeDriverManager().install())
browser.get(website)
browser.maximize_window()