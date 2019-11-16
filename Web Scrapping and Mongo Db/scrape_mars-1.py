#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


# # Title an News

# In[2]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'


# In[3]:


# Retrieve page with the requests module
response = requests.get(url)


# In[4]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[5]:


#collect the latest News Title 
news_title =soup.title.text.strip()
print(news_title)


# In[6]:


#Paragraph Text
paragraphs = soup.find_all('p')
for news_paragraph in paragraphs:
    print(news_paragraph.text)


# # JPL Mars Space Images - Featured Image

# In[11]:


#setting up for splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


#visit the website

url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_jpl)


# In[13]:


#browse the image
full_image_button=browser.find_by_id('full_image')
full_image_button.click()


# In[14]:


#browse the full image
more_info=browser.find_link_by_partial_text('more info')
more_info.click()


# In[15]:


#get the image link from HTML
html =browser.html
soup =bs(html, 'html.parser')
image = soup.find('img', class_ = 'main_image')['src']
image


# In[16]:


# get the link of the featured image
featured_image_url = "https://www.jpl.nasa.gov" + image
print(f"Mars Featured Image URL : {featured_image_url}")


# # Mars Weather

# In[17]:


#URL for twitter account page
tweet_url= 'https://twitter.com/marswxreport?lang=en'


# In[18]:


#get request
response_tweet = requests.get(tweet_url)


# In[19]:


#parse the data
soup_tweet = bs(response_tweet.text, 'html.parser')


# In[20]:


# 1st Method to get the tweet, via tag, class


# In[21]:


all_tweets = []
timeline =soup_tweet.select('#timeline li.stream-item')
for tweet in timeline:
    tweet_text = tweet.select('p.tweet-text')[0].get_text()
    all_tweets.append(tweet_text)


# In[22]:


mars_weather =all_tweets[0]
mars_weather


# In[23]:


# 2nd Method, via try and except


# In[24]:


tweet_results = soup_tweet.find_all('li', class_="stream-item")


# In[25]:


number = 0
# Loop through returned results
for result in tweet_results:
    # Error handling
    if number ==1:
        break
    try:
        # Identify and return tweet
        mars_weather = result.find('p', class_="tweet-text").text
        number += 1
        print (mars_weather)
    except:
        print ("This is an error message!")


# # Mars Facts

# In[26]:


# Mars fact URL
fact_url = "https://space-facts.com/mars/"


# In[27]:


#Read the HTML table
mars_table = pd.read_html(fact_url)


# In[28]:


#Display the required table data
mars_df = mars_table[0]
mars_df.columns = ['description', 'value']
mars_df = mars_df.set_index('description')
mars_df.head(10)


# In[30]:


# conver the table to HTML 
mars_facts = mars_df.to_html()
print(mars_facts)


# # Mars Hemispheres

# In[31]:


#setting up for splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[32]:


# define the URL and open it via splinter 
hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemisphere_url)


# In[33]:


#get the image link from HTML
html =browser.html
soup =bs(html, 'html.parser')


# In[34]:


#display the parsed and selected section, from where the navigation is required
hemispheres =soup.find_all("div", class_="item")
hemispheres


# In[35]:


# generate a loop to get the name and the URL , append the data in a dictionary 
mars_hemisphere = []
for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.strip("Enhanced")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup = bs(html, 'html.parser')
    image = soup.find('img', class_ = 'wide-image')['src']
    image_url = "https://astrogeology.usgs.gov" + image
    mars_hemisphere.append({"title": title,"img_url": image_url})
mars_hemisphere


# In[36]:


#converting this jupyter notebook in python script
get_ipython().system('jupyter nbconvert --to script mission_to_mars.ipynb')


# In[ ]:




