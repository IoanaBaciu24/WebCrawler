# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:02:07 2020

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from win10toast import ToastNotifier

def load_u_and_pass():
    f = open("login.txt", "r")
    uname = f.readline()
    passw = f.readline()
    
    f.close()
    
    return uname,passw

def load_logs():
    f = open("logs.txt", "r")
    line =f.readline()
    logs = int(line)
    
    f.close()
    
    return logs
    

def save_logs(log):
    f = open("logs.txt", "w")
    f.write(str(log))
    f.close()    



def set_up_driver():

    chrome_options = Options()
    #chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\\Users\\papuci\\Documents\\chromedriver.exe")
    return driver


def trim_arr(arr):
    res = []
    for el in arr:
        if len(el.text) >= 30:
            res.append(el)
    
    return res


def print_nicely(arr):
    for el in arr:
        print(el.text)
        
        
        
def log_in(driver):
    
    u,p = load_u_and_pass()
    
    elements = driver.find_elements_by_name("_user")
    username = elements[0]
    username.clear()
    user_name = u
    username.send_keys(user_name)
    elements = driver.find_elements_by_name("_pass")
    print(len(elements))
    password = elements[0]
    print(password.text)
    password.clear()
    print(password.text)
    pas = p
    password.send_keys(pas)

    elements = driver.find_elements_by_id("rcmloginsubmit")
    submit = elements[0]
    submit.click()

    time.sleep(5)
    
def log_out(driver):
    logout = driver.find_element_by_class_name("button-logout")
    logout.click()
        
        

    
        

def start_notifying():
    
    
    driver = set_up_driver()
    
    url = "https://www.scs.ubbcluj.ro/webmail/"
    driver.get(url)
    time.sleep(3)
    
    trs = driver.find_elements(By.TAG_NAME, "tr") 
    trs = trim_arr(trs)
        
    toaster = ToastNotifier()
    while True:
        leng = load_logs()
        log_in(driver)
        trs = driver.find_elements(By.TAG_NAME, "tr") 
        trs = trim_arr(trs)
        
        print(len(trs))
        print("a step is done")
        if leng !=len(trs):
            if len(trs)!=0:
                leng = len(trs)
                print("ai primit un mail")
                print(trs[0].text)
                toaster.show_toast("You got mail!",trs[0].text)
                save_logs(leng)
                
    
        log_out(driver)
        time.sleep(3)
        
        
start_notifying()
        
























