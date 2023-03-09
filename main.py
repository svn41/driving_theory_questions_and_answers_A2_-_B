################################################ Necessary Libraries ##################################
import os, random, sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import requests

####################################################### configure chrome driver #########################

browser =  webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.instagram.com/accounts/login')
browser.maximize_window()