from bs4 import BeautifulSoup
import urllib
from urllib import urlopen
import re

#find box scores for every game of the 2013 nfl season
url = 'http://www.pro-football-reference.com/years/2013/games.htm'
season_data = urllib.urlopen(url)
words_1 = season_data.read().decode('utf-8')
all_box_scores = re.findall('/boxscores/(.+)\.htm', words_1)

#find every table row in the box score
for i in all_box_scores:
    full_link = 'http://www.pro-football-reference.com/boxscores/%s.htm'%(i)
    page = urllib.urlopen(full_link)
    soup = BeautifulSoup(page.read())
    all_rows = soup.findAll('tr')
    table_rows = [] #stores every row as a string
    table_cells = [] #stores a list of list of cells by row
    all_plays = [] #stores only rows that are plays
    #turn each row into a strong and add to list
    for x in all_rows:
        table_rows.append(str(x))
    #find each cell in the row, returning a list per row.     
    for i in table_rows:
        row_cells = re.findall('<td(.+)</td>', i)
        table_cells.append(row_cells) #this creates a list of the info for each play
    for j in table_cells:
        if (len(j) == 11): #check if table row contains a cell
            all_plays.append(j)
    for k in range (0, len(all_plays)):      
        curr_play = all_plays[k]
        if (k < len(all_plays)-1):
            next_play = all_plays[k+1]
        if ('punts' in curr_play[5]):    #check if play is a punt
            punt_info = [] #punt_info contains the yard line before and after the punt, as well as the play summary
            start_yard = curr_play[4]
            end_yard = next_play[4]
            summary = curr_play[5]
            punt_info.append(start_yard)
            punt_info.append(end_yard)
            punt_info.append(summary)
            print punt_info #will need cleaning
