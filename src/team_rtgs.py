import numpy as np
import statistics
import matplotlib.pyplot as plt
import pandas as pd
import math
from pathlib import Path
import scipy.stats

"""
Testing offensive and defensive ratings
"""

cwd = Path.cwd()
root = cwd.parent.absolute()

team_game_logs = pd.read_csv(root / 'data' / '2023_24_team_rtgs.csv')

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
	game_date=int(game_date[5:7]+game_date[8:10])
	game_date_num=0
	game_date_num+=game_date%100
	game_date=int(game_date/100)
	while game_date!=1:
		game_date_num+=months[game_date-2]
		game_date-=1
	return game_date_num

b2b_drtg = []
b2b_ortg = []
non_b2b_drtg = []
non_b2b_ortg = []

b2b_drtg_sum_squares = 0
b2b_ortg_sum_squares = 0

non_b2b_drtg_sum_squares = 0
non_b2b_ortg_sum_squares = 0

b2b_game_data = []
non_b2b_game_data = []

for team in nba_teams:
	game_logs=team_game_logs[team_game_logs['TEAM_NAME']==team]
	total_games=len(game_logs['GAME_DATE'])
	non_b2b_drtg.append(game_logs.iloc[total_games-1,12])
	non_b2b_ortg.append(game_logs.iloc[total_games-1,10])
	non_b2b_game_data.append(game_logs.iloc[total_games-1])
	for i in range(total_games-1):
		game_date=game_logs.iloc[i,5]
		gdn_1 = date_to_num(game_date)
		game_date=game_logs.iloc[i+1,5]
		gdn_2 = date_to_num(game_date)
		if (gdn_1-1==gdn_2%366):
			b2b_game_data.append(game_logs.iloc[i])
			b2b_drtg.append(game_logs.iloc[i,12])
			b2b_ortg.append(game_logs.iloc[i,10])
		else:
			non_b2b_game_data.append(game_logs.iloc[i])
			non_b2b_drtg.append(game_logs.iloc[i,12])
			non_b2b_ortg.append(game_logs.iloc[i,10])


total_b2bs = len(b2b_drtg)

avg_b2b_drtg = sum(b2b_drtg)/total_b2bs
avg_b2b_ortg = sum(b2b_ortg)/total_b2bs

total_non_b2bs = len(non_b2b_drtg)

avg_non_b2b_drtg = sum(non_b2b_drtg)/total_non_b2bs
avg_non_b2b_ortg = sum(non_b2b_ortg)/total_non_b2bs

print('avg defensive rating (dRTG) of teams on back-to-backs: ', avg_b2b_drtg)
print('avg offensive rating (oRTG) of teams on back-to-backs: ', avg_b2b_ortg)

print('avg non back-to-back drtg: ', avg_non_b2b_drtg)
print('avg non back-to-back ortg: ', avg_non_b2b_ortg)

for i in range(total_b2bs):
	b2b_drtg_sum_squares += (b2b_drtg[i]-avg_b2b_drtg)**2
	b2b_ortg_sum_squares += (b2b_ortg[i]-avg_b2b_ortg)**2

b2b_drtg_s2 = b2b_drtg_sum_squares/(total_b2bs-1)
b2b_ortg_s2 = b2b_ortg_sum_squares/(total_b2bs-1)

print('back-to-back drtg variance: ', b2b_drtg_s2)
print('back-to-back ortg variance: ', b2b_ortg_s2)

for j in range(total_non_b2bs):
	non_b2b_drtg_sum_squares += (non_b2b_drtg[j]-avg_non_b2b_drtg)**2
	non_b2b_ortg_sum_squares += (non_b2b_ortg[j]-avg_non_b2b_ortg)**2

non_b2b_drtg_s2 = non_b2b_drtg_sum_squares/(total_non_b2bs-1)
non_b2b_ortg_s2 = non_b2b_ortg_sum_squares/(total_non_b2bs-1)

print('non back-to-back drtg variance: ', non_b2b_drtg_s2)
print('non back-to-back ortg variance: ', non_b2b_ortg_s2)


"""
Hypothesis test
"""

n1 = total_b2bs
n2 = total_non_b2bs


drtg_x1 = avg_b2b_drtg
drtg_x2 = avg_non_b2b_drtg
drtg_s1 = b2b_drtg_s2
drtg_s2 = non_b2b_drtg_s2

ortg_x1 = avg_b2b_ortg
ortg_x2 = avg_non_b2b_ortg
ortg_s1 = b2b_ortg_s2
ortg_s2 = non_b2b_ortg_s2

drtg_z = (drtg_x1-drtg_x2)/math.sqrt(drtg_s1/n1+drtg_s2/n2)
ortg_z = (ortg_x1-ortg_x2)/math.sqrt(ortg_s1/n1+ortg_s2/n2)

print('dRTG z= ', drtg_z)
print('oRTG z= ', ortg_z)


drtg_p_val = scipy.stats.norm.sf(abs(drtg_z)) 
ortg_p_val = scipy.stats.norm.sf(abs(ortg_z))
print('dRTG p-value= ', drtg_p_val)
print('oRTG p-value= ', ortg_p_val)


b2b_game_df = pd.DataFrame(b2b_game_data)
b2b_game_df.columns = game_logs.columns
b2b_game_df.to_csv(root / 'data' / 'result' / 'b2bs_rtgs_2023_24.csv', index=False)

non_b2b_game_df = pd.DataFrame(non_b2b_game_data)
non_b2b_game_df.columns = game_logs.columns
non_b2b_game_df.to_csv(root / 'data' / 'result' / 'non_b2bs_rtgs_2023_24.csv', index=False)

