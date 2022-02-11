import pandas as pd
import numpy as np
import os
import json
import typing

# Read from json file
def read() -> pd.DataFrame:
	path = 'D:/projects/python/shiki_app/shiki/anime-offline-database/anime-offline-database.json'
	data = json.load(open(path, encoding="UTF-8"))

	df = pd.DataFrame(data["data"])
	return df



# Convert DataFrame to Excel
def to_excel(df: pd.DataFrame) -> None:
	try:
		with pd.ExcelWriter('answer.xlsx', mode='w') as writer: 
			df.to_excel(writer, sheet_name='anime')  
	except Exception as e:
		print(e)


# Convert DataFrame to csv
def to_csv(df: pd.DataFrame) -> None:
	try:
		df.to_csv('out.csv', index=False)  
	except Exception as e:
		print(e)


# Delete unnecesary colums
# columns can be string, list of strings
def del_unn_col(columns, df: pd.DataFrame) -> pd.DataFrame:
	try:
		df = df.drop(columns, axis=1)
		return df
	except Exception as e:
		print(e)	


# Return count of unique instances in columns for plot
# column can be string, list of strings
def count(columns, df: pd.DataFrame) -> pd.Series:
	try:
		ans = df[columns].value_counts()
		return ans
	except Exception as e:
		print(e)


def qcount(df: pd.DataFrame, query: str, column: str) -> pd.Series:
	try:
		ans = df.query(query)[column].value_counts()
		return ans
	except Exception as e:
		print(e)

# Divide animeSeason column into season and year columns
def anime_season(df: pd.DataFrame) -> pd.DataFrame:
	season = df["animeSeason"]
	temp1 = []
	temp2 = []
	for item in season:
		temp1.append(item["season"])
		temp2.append(item["year"])

	sson = pd.Series(temp1)
	year = pd.Series(temp2)

	df.insert(3, "season", sson)
	df.insert(4, "year", year)

	return df


# REFACTOR TABLE
def refactor_table(df: pd.DataFrame) -> pd.DataFrame:
	ans = del_unn_col(columns=["sources", "picture", "thumbnail", "relations"], df=df)
	ans = anime_season(ans)
	ans = del_unn_col(columns="animeSeason", df=ans)

	return ans


