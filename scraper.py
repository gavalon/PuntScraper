import urllib
import re
from urllib import urlopen

#Find the link to every box score from 2013
season_data = urllib.urlopen('http://www.pro-football-reference.com/years/2013/games.htm')
words_1 = season_data.read().decode('utf-8')
all_box_scores = re.findall('/boxscores/(.+)\.htm', words_1)

#Iterate over the links, finding the data from before and after a punt
for i in all_box_scores:
    full_link = 'http://www.pro-football-reference.com/boxscores/%s.htm'%(i)
    game_data = urllib.urlopen(full_link)
    words_2 = game_data.read().decode('utf-8')
    all_punts = re.findall('<td align="left"  csk="0">(.+)</td>', words_2)
    print all_punts
