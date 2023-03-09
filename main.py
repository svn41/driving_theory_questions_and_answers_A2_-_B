import os, random, sys, time
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
from datetime import date
from datetime import datetime
import numpy as np
import wget

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from deepface import DeepFace

import cv2
from PIL import Image
import requests
from io import BytesIO

from PIL import Image
from numpy import asarray

import random