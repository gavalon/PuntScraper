from bs4 import BeautifulSoup
import urllib
from urllib import urlopen
import re

#find box score for every nfl game in the 2013 season
url = 'http://www.pro-football-reference.com/boxscores/201410190ram.htm'
season_data = urllib.urlopen(url)
words_1 = season_data.read().decode('utf-8')
all_box_scores = re.findall('/boxscores/(.+)\.htm', words_1)

#iterate over this to find all of the info in tables
for i in all_box_scores:
    full_link = 'http://www.pro-football-reference.com/boxscores/%s.htm'%(i)
    page = urllib.urlopen(full_link)
    soup = BeautifulSoup(page.read())
    all_rows = soup.findAll('tr')
    table_rows = []
    table_cells = []
    #turn each table row into a string and add to list
    for x in all_rows:
        table_rows.append(str(x))
    #find each cell in the row, returning a list per row.     
    for i in table_rows:
        row_cells = re.findall('<td(.+)</td>', i)
        table_cells.append(row_cells) #this creates a list of the info for each play
    for j in range (0, len(table_cells)):
        if j < len(table_cells)-1:
            next_play = table_cells[j+1]
        curr_play = table_cells[j] 
        if (len(curr_play) == 11 and 'punts' in curr_play[5]):
            punt_info = [] #punt_info contains the starting and ending yards for the punt, as well as the play summary
            start_yard = curr_play[4]
            end_yard = next_play[4]
            summary = curr_play[5]
            punt_info.append(start_yard)
            punt_info.append(end_yard)
            punt_info.append(summary) 
            print punt_info #contains partial tags, must clean later
