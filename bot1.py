"""Bot 1 para automatizacion de ingreso de actividades"""

import math
import random
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('./chromedriver')

def login():

    sleep(random.uniform(2.0,3.0))
    browser.set_window_size(1500, 1000)
    sleep(random.uniform(2.0,3.0))

    browser.get('http://192.168.1.3:8080/login')
    sleep(random.uniform(3.0,5.0))

    mail = browser.find_element_by_xpath('//input[@id="email"]')
    sleep(random.uniform(0.5,1.0))
    mail.click()
    sleep(random.uniform(0.5,1.0))
    mail.send_keys('driquelme@esri.cl')
    sleep(random.uniform(1.0,2.0))

    passw = browser.find_element_by_xpath('//input[@id="password"]')
    sleep(random.uniform(0.5,1.0))
    passw.click()
    sleep(random.uniform(0.5,1.0))
    passw.send_keys('123')
    sleep(random.uniform(1.0,2.0))

    login = browser.find_element_by_xpath('//input[@type="submit"]')
    sleep(random.uniform(0.5,1.0))
    login.click()
    sleep(random.uniform(0.5,1.0))

    #________________________________________________________________

    browser.get('http://192.168.1.3:8080/tarea')
    sleep(random.uniform(3.0,5.0))

    semana = browser.find_element_by_xpath('//button[@class="fc-timeGridWeek-button btn btn-primary"]')
    sleep(random.uniform(0.5,1.0))
    semana.click()
    sleep(5)

login()


#####_____________________________________________________________

lista = [ (2) ,(3) ,(4) ,(5) ,(6)]

def data():

    indice = 0
    while indice < len(lista):
        print(lista[indice])


        selectDay = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[3]/table/tbody/tr/td[{}]'.format(lista[indice]))
        sleep(random.uniform(0.5,1.0))
        selectDay.click()
        sleep(5)
        indice+=1

data()

def browserClose():
    browser.close() 
browserClose()


"""/html/body/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[3]/table/tbody/tr/td[2]


        data-time

        08:30:00"""