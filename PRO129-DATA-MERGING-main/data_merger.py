import pandas as pd
import csv

brightest_star_file = 'brightest_star-scraped_data.csv'
dwarf_star_file = 'dwarf_stars-scraped_data.csv'

brightest_star_list = []
dwarf_star_list = []

with open(brightest_star_file, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        brightest_star_list.append(row)
        
with open(dwarf_star_file, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dwarf_star_list.append(row)

starBright = brightest_star_list[0]
starDwarf = dwarf_star_list[0]

brightest_star_list = brightest_star_list[1:]
dwarf_star_list = dwarf_star_list[1:]

mergedData = [starBright] + [starDwarf]

array =[]

for i in brightest_star_list:
    array.append(i)
for j in dwarf_star_list:
    array.append(j)
    
with open("MergedData.csv", 'w', encoding='utf8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(mergedData)
    csvwriter.writerows(array)

mergedData = pd.read_csv('MergedData.csv')
print('Data of brightest_star_scraper.py and dwarf_star_scraper.py merged successfully!')