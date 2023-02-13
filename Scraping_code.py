#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#The scraping code


# In[ ]:


# This is the url you will scrape 
url = 'https://www.timeanddate.com/moon/phases/?year=2022'

# usamos requests para extraer el HTML

html=req.get(url).content   # o .text
soup = bs(html, "html.parser")
html[:1000]


# In[ ]:


soup = bs(html, "html.parser")


# In[ ]:


cookies = driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()


# In[ ]:


x = driver.find_elements(By.CLASS_NAME, 'head')
headers = [i.text for i in x]


# In[ ]:


x1 = driver.find_elements(By.CLASS_NAME, 'tr')
body = [i.text for i in x1]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




