#!/usr/bin/env python
# coding: utf-8

# In[43]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys #讓selenium使用按鍵
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# In[44]:


PATH="C:/Users/jerryold/Desktop/Selenum/chromedriver.exe" #瀏覽器所放置的位置(根據想要使用的去下載)
driver=webdriver.Chrome(PATH)        #選擇selenium要使用的路徑
driver.get("https://www.dcard.tw/f") #控制selenium要前往的網址
print(driver.title) #取得網頁title


# In[45]:


search=driver.find_element_by_name("query") #尋找dcard搜尋欄,其name為query
search.clear()#避免預設文字
search.send_keys("台積電")
search.send_keys(Keys.RETURN)#按下Enter

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-1vxpqp0-0")) #等待瀏覽器10秒鐘,根據看板class_name出現為止
    )

titles=driver.find_elements_by_class_name("tgn9uw-3")
for title in titles:
    print(title.text)
    
time.sleep(5)
# driver.quit() #網頁關掉


# In[46]:


link=driver.find_element_by_link_text("詢問台積電資料審核中")#搜尋第一篇文件名稱
link.click()#按下按鈕
driver.back()#回到上一頁
driver.forward()#回到下一頁

