#!/usr/bin/env python
# coding: utf-8

# In[29]:


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# In[30]:


PATH = "C:/Users/jerryold/Desktop/Selenum/chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://tsj.tw/")


# In[31]:


button=driver.find_element_by_id("click")
button_press_count=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]') #根據該欄位xpath來索取資訊
items=[]
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))

prices=[]
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))
print(button_press_count.text)


actions=ActionChains(driver)
#動作設定
actions.click(button)

for i in range(10000):
    #動作執行
    actions.perform()
    count=int(button_press_count.text.replace("您目前擁有","").replace("技術點",""))
    for j in range(3):
        price=int(prices[j].text.replace("技術點",""))
        if price<=count:
            upgrade_actions=ActionChains(driver)#新增另一個動作
            upgrade_actions.move_to_element(items[j])#移動至items上
            upgrade_actions.click()
            upgrade_actions.perform()
            break #買到東西要break掉
        


# In[ ]:




