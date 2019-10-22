# Homework 2 Yutong Liu

# 1 . (1 points) Write a python reads creates a dataframe from a URL
# that points to a CSV file such as the pronto data or CSVs in data.gov.

import pandas as pd


def read(url):
	#  create data frame
	df = pd.read_csv(url)
	return df

def test_create_dateframe(df, columnsName):
	df_col = list(df.columns)

	if df_col == columnsName:
		condition_1 = 1
	else:
		condition_1 = 0

	for i in df_col:
		if df[i].dtype:
		 	condition_2 = 1
		else:
			condition_2 = 0


	numOfRows = df.count(axis='rows')
	for i in numOfRows:
		if int(i) > 10:
			condition_3 = 1
		else:
			condition_3 = 0

	if condition_1 and condition_2 and condition_3:
		print('True')
		return True
	else:
		print('False')
		return False

url= 'https://inventory.data.gov/dataset/9b8df339-a659-4f7a-b6f0-de8e17964f68/resource/583cf78f-2508-4d21-a55d-3e3cb1dfff16/download/userssharedsdfteachingamericanhistory2010applicants.csv'
df = read(url)
columnsName = ['Project Title', 'City', 'State', 'ZIP', 'Award', 'Location']
test_create_dateframe(df, columnsName)
