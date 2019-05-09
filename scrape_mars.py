from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
# get_ipython().system('which chromedriver')

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

    # browser = webdriver.Chrome('/usr/local/bin/chromedriver')

def scrape():
    browser = init_browser()
    mars_data = {}
   
    # Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    for x in range(1):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.find_all('div', class_='content_title')

        for title in titles:
            article_title = title.text


    for x in range(1):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        articles = soup.find_all('div', class_='article_teaser_body')

        for article in articles:
            article_body = article.text

    # Mars Image
    jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl)

    browser.click_link_by_id('full_image')

    image = soup.find('img')['src']

    featured_image_url = "https://www.jpl.nasa.gov" + image

    # Mars Weather
    marsweather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(marsweather)

    for x in range(1):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        content = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    # Mars Facts
    marsFacts = 'https://space-facts.com/mars/'
    browser.visit(marsFacts)

    tables = pd.read_html(marsFacts)

    df = tables[0]
    df.columns = ['Fact', 'Data']

    html_table = df.to_html()
    html_table = html_table.replace('\n', '')

    # Mars Hemispheres
    marsHemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(marsHemispheres)

    browser.click_link_by_partial_text('Cerberus')

    for x in range(1):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        cerberus_enhanced = "https://astrogeology.usgs.gov/" + soup.find('img', class_="wide-image")['src']
        cerberus_title = soup.find('h2', class_="title").text

    browser.click_link_by_partial_text('Enhanced')

    for x in range(1):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        valles_marineris_enhanced = "https://astrogeology.usgs.gov/" + soup.find('img', class_="wide-image")['src']
        valles_marineris_title = soup.find('h2', class_="title").text

    browser.click_link_by_partial_text('Enhanced')

    for x in range(1):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        syrtis_major_enhanced = "https://astrogeology.usgs.gov/" + soup.find('img', class_="wide-image")['src']
        syrtis_major_title = soup.find('h2', class_="title").text

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    for x in range(1):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        schiaparelli_enhanced = "https://astrogeology.usgs.gov/" + soup.find('img', class_="wide-image")['src']
        schiaparelli_title = soup.find('h2', class_="title").text

    schiaparelli_dict = {
        "title" : schiaparelli_title,
        "img_url" : schiaparelli_enhanced
    }

    syrtis_major_dict = {
        "title" : syrtis_major_title,
        "img_url" : syrtis_major_enhanced
    }

    valles_marineris_dict = {
        "title" : valles_marineris_title,
        "img_url" : valles_marineris_enhanced
    }

    cerberus_dict = {
        "title" : cerberus_title,
        "img_url" : cerberus_enhanced
    }

    mars_hemi_data = []
    mars_hemi_data.append(cerberus_dict)
    mars_hemi_data.append(valles_marineris_dict)
    mars_hemi_data.append(syrtis_major_dict)
    mars_hemi_data.append(schiaparelli_dict)


    mars_data["headline"] = article_title
    mars_data["article"] = article_body
    mars_data["featured_image"] = featured_image_url
    mars_data["weather"] = content
    mars_data["facts"] = html_table
    mars_data["hemispheres"] = mars_hemi_data
    
    return mars_data
