#convert json files in data folder to csv files
import os
import json
import csv
from pathlib import Path

cwd = Path.cwd()
root = cwd.parent.absolute()

team_game_logs_path = root / 'data' / '2023_24_team_game_logs.json'
team_rtgs_path = root / 'data' / '2023_24_team_rtgs.json'



#convert team traditional stat game logs to csv
with open(team_game_logs_path) as file:
	data = json.loads(file.read())

col_names = data['resultSets'][0]['headers']
player_stats = data['resultSets'][0]['rowSet']

data_path = root / 'data' / '2023_24_team_game_logs.csv'
with open(data_path, 'w') as file:
	writer = csv.writer(file)
	writer.writerow(col_names)
	for entry in player_stats:
		writer.writerow(entry)


#convert team advanced stat game logs to csv
with open(team_rtgs_path) as file:
	data = json.loads(file.read())

col_names = data['resultSets'][0]['headers']
player_stats = data['resultSets'][0]['rowSet']

data_path = root / 'data' / '2023_24_team_rtgs.csv'
with open(data_path, 'w') as file:
	writer = csv.writer(file)
	writer.writerow(col_names)
	for entry in player_stats:
		writer.writerow(entry)


