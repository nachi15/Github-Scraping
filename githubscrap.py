import selenium
from selenium import webdriver
import csv

max_page_num = 1 
max_page_dig = ['c++','java','html','javascript','python','ruby','scala']
max_time_dig = ['daily','weekly','monthly']

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#url = 'https://github.com/trending?since=monthly'
#driver.get(url)
csv_file = open("GitHub_Scraping.csv",'w', encoding='utf-8')
csv_writer = csv.writer(csv_file) #initializing the CSV file for writing 
csv_writer.writerow(['Username','Description','PullReq','Ratings']) #Naming the heading as Company Name

for w in max_page_dig:
    url = 'https://github.com/trending/' + w + '?since='
    for z in max_time_dig:
        newurl = url + z
        driver.get(newurl)
        articles = driver.find_elements_by_xpath('//article[@class="Box-row"]')
        for article in articles:
            try:
                username = article.find_element_by_xpath('.//h1[@class="h3 lh-condensed"]').text 
            except:
                username = 'none'
            try:
                description = article.find_element_by_xpath('.//p[@class="col-9 text-gray my-1 pr-4"]').text
            except:
                description ='none'
            try:
                pullreq = article.find_element_by_xpath('.//a[@class="muted-link d-inline-block mr-3"]').text
            except:
                pullreq = 'none'
            try:
                ratings = article.find_element_by_xpath('.//span[@class="d-inline-block float-sm-right"]').text
            except:
                ratings = 'none'
            print(username)
            print(description)
            print(pullreq)
            print(ratings)
            csv_writer.writerow([username,description,pullreq,ratings])
