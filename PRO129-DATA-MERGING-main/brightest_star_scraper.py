from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("E:/Setup/chromedriver_win32/chromedriver.exe") #Change Drive accordingly
browser.get(START_URL)

time.sleep(10)

scarped_data = []

def scrape():
               
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # <table> Tag
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        
    # <tbody> Tag
    table_body = bright_star_table.find('tbody')

    # <tr> Tag
    table_rows = table_body.find_all('tr')

    # Data extraction from <td> Tag
    for row in table_rows:
        table_cols = row.find_all('td')
        # print(table_cols)
            
        temp_list = []

        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)

        scarped_data.append(temp_list)

scrape()

stars_data = []

for i in range(0,len(scarped_data)):
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Luminosity = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Luminosity]
    stars_data.append(required_data)

# Define Header
headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

# Define pandas DataFrame
brightest_star = pd.DataFrame(stars_data, columns=headers)
print(brightest_star)

# Convert to CSV
brightest_star.to_csv('brightest_star-scraped_data.csv', index = True, index_label = "id")
print("CSV file created successfully!")