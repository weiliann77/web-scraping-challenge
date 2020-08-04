
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import pymongo

def scrape():
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    results= soup.find_all('div', class_='content_title')
    #first data
    latest_headline=results[0].a.text
    results2 = soup.find_all('div', class_='rollover_description_inner')
    #second data
    latest_inner=results2[0].text
    #first dictionary
    headline_dict={'Headline':latest_headline,'Inner_Text':latest_inner}
    executable_path = {'executable_path': "\\Users\Brodie\Downloads\chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('Mars')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results=[]
    results =soup.find_all('img',class_='fancybox-image')
    #third data
    print(results[0].get('src'))
    jpl_image = "https://www.jpl.nasa.gov/"+results[0].get('src')
    #jpl dict
    jpl_dict={'Jpl_image':jpl_image}
    url = 'https://twitter.com/marswxreport'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results=soup.find_all('span')
    #fourth data
    tweet=results[42].text
    tweet_dict ={'Tweet':tweet}
    url='https://space-facts.com/mars/'
    tables = pd.read_html(url)
    #fith data
    df=tables[0]

    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    Mars_H=['Cerberus Hemisphere','Schiaparelli Hemisphere','Syrtis Major Hemisphere','Valles Marineris Hemisphere']
    Mars_Dict={}
    hemisphere_image_urls=[]
    #sixth data
    for Hems in Mars_H:
        browser.click_link_by_partial_text(Hems)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        results=soup.find_all('a', href=True)
        Mars_Dict.update({'title_' + Hems : Hems, 'img_url_' + Hems : results[4]['href']})
        hemisphere_image_urls.append(Mars_Dict)
        browser.visit(url)

    Main_Dict=[headline_dict,jpl_dict,tweet_dict,df_new[0],hemisphere_image_urls[0]]
    return Main_Dict



