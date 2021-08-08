#!/usr/bin/env python
# coding: utf-8

# In[25]:


# 爬取ig關鍵字圖片
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os 
import wget #網路下載東西


# In[26]:


PATH = "C:/Users/jerryold/Desktop/Selenum/chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")


# In[27]:


username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username")) #根據網頁出現username的欄位才會執行
)

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))#根據網頁出現password的欄位才會執行
)

login=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')#取得登入按鈕xpath

username.clear()
password.clear()
username.send_keys('jerry860602') #輸入ig帳號
password.send_keys('***********') #輸入ig密碼
login.click()#按下登入按鈕


search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))#根據網頁出現password的欄位才會執行
)
keyword='#nba'
search.send_keys(keyword)#輸入關鍵字
time.sleep(1)
search.send_keys(Keys.RETURN)#按下ENTER鍵
time.sleep(1)
search.send_keys(Keys.RETURN)#按下ENTER鍵



# In[28]:


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))#根據網頁class_name>>FFVAD
)
for i in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")#執行javascript程式碼,滑動滾輪到底
    time.sleep(5)
    
imgs=driver.find_elements_by_class_name("FFVAD")#ig圖片共通點為class_name>>FFVAD

filepath=os.path.join(keyword) #創建資料夾
os.mkdir(filepath)

count=0
for img in imgs:
    save_as=os.path.join(filepath,keyword+str(count)+'.jpg')
#   print(img.get_attribute("src"))#取得圖片src屬性
    wget.download(img.get_attribute("src"),save_as)
    count+=1
    

