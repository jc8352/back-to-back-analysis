import numpy as np
import statistics
import matplotlib.pyplot as plt
import pandas as pd
import math
from pathlib import Path
import scipy.stats

"""
Testing 3 point percentage on back-to-backs
"""

cwd = Path.cwd()
root = cwd.parent.absolute()

team_game_logs = pd.read_csv(root / 'data' / '2023_24_team_game_logs.csv')

nba_teams= ['Golden State Warriors',
'Atlanta Hawks', 
'Boston Celtics', 
'Brooklyn Nets',
'Charlotte Hornets', 
'Chicago Bulls', 
'Cleveland Cavaliers', 
'Dallas Mavericks', 
'Denver Nuggets', 
'Detroit Pistons',  
'Houston Rockets', 
'Indiana Pacers', 
'LA Clippers', 
'Los Angeles Lakers', 
'Memphis Grizzlies', 
'Miami Heat', 
'Milwaukee Bucks', 
'Minnesota Timberwolves', 
'New Orleans Pelicans', 
'New York Knicks', 
'Oklahoma City Thunder', 
'Orlando Magic', 
'Philadelphia 76ers', 
'Phoenix Suns', 
'Portland Trail Blazers', 
'Sacramento Kings', 
'San Antonio Spurs', 
'Toronto Raptors', 
'Utah Jazz', 
'Washington Wizards']



months=[31,29,31,30,31,30,31,31,30,31,30,31]

def date_to_num(game_date):
	game_date=int(game_date[5:7]+game_date[8:])
	game_date_num=0
	game_date_num+=game_date%100
	game_date=int(game_date/100)
	while game_date!=1:
		game_date_num+=months[game_date-2]
		game_date-=1
	return game_date_num

b2b_3s_made = 0
b2b_3s_attempted = 0
non_b2b_made = 0
non_b2b_attempted = 0
b2b_count = 0
non_b2b_count = 0


for team in nba_teams:
	game_logs=team_game_logs[team_game_logs['TEAM_NAME']==team]
	total_games=len(game_logs['GAME_DATE'])
	non_b2b_made += game_logs.iloc[total_games-1,12]
	non_b2b_attempted += game_logs.iloc[total_games-1,13]
	non_b2b_count += 1
	for i in range(total_games-1):
		game_date=game_logs.iloc[i,5]
		gdn_1 = date_to_num(game_date)
		game_date=game_logs.iloc[i+1,5]
		gdn_2 = date_to_num(game_date)
		if (gdn_1-1==gdn_2%366):
			b2b_count+=1
			b2b_3s_made += game_logs.iloc[i,12]
			b2b_3s_attempted += game_logs.iloc[i,13]
		else:
			non_b2b_count+=1
			non_b2b_made += game_logs.iloc[i,12]
			non_b2b_attempted += game_logs.iloc[i,13]



print('Total 3s attempted on back-to-backs: ', b2b_3s_attempted)
print('Total 3s attempted on non back-to-backs: ', non_b2b_attempted)

print('3pt shooting percentage on back-to-backs: ', b2b_3s_made/b2b_3s_attempted)
print('3pt shooting percentage on non back-to-backs: ', non_b2b_made/non_b2b_attempted)


"""
Hypothesis test
"""

b2b_3_pct = b2b_3s_made/b2b_3s_attempted
non_b2b = non_b2b_made/non_b2b_attempted

p1 = b2b_3_pct
p2 = non_b2b

q1 = 1-p1
q2 = 1-p2

n1 = b2b_3s_attempted
n2 = non_b2b_attempted

z = (p1-p2)/math.sqrt(p1*q1/n1+p2*q2/n2)
print('z= ', z)


p_val = scipy.stats.norm.sf(abs(z))
print('p-value= ', p_val)

