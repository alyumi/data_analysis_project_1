import pandas as pd
import numpy as np
import os
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import typing

import db


# Method to show different plots
def analyse(figure: int, df: db.DF) -> None:
	if figure == 1:
		status = df.count(columns="status")
		f1 = plt.figure(1)
		plt.bar(status.index, status.values)
		plt.title("Anime Status Count")
		plt.xlabel("Status")
		plt.ylabel("Count")
		plt.show()

	elif figure == 2: 
		tp = df.count(columns="type")
		f2 = plt.figure(2)
		plt.bar(tp.index, tp.values)
		plt.title("Anime Types Count")
		plt.xlabel("Type")
		plt.ylabel("Count")
		plt.show()

	elif figure == 3:
		years = df.query_count(query="(`year` != None) & (`year` >= 1910) & (`year` < 2022)", column="year")
		years = years.sort_index(ascending=True)
		f3 = plt.figure(3)
		plt.plot(years.index, years.values)
		plt.title("Anime by Years")
		plt.xlabel("Year")
		plt.ylabel("Count")
		plt.show()


# Console menu
def menu(df: db.DF) -> None:
	graphs = ["Anime Status Count", "Anime Types Count", "Anime Count by Years"]
	print("Choose graph to show:")
	print("1:", graphs[0])
	print("2:", graphs[1])
	print("3:", graphs[2])
	print("0: Close app")

	choice = -123
	while(True):
		choice = int(input())
		if choice == 1:
				analyse(figure=1, df=df)
		elif choice == 2:
				analyse(figure=2, df=df)
		elif choice == 3:
				analyse(figure=3, df=df)
		elif choice == 0:
			break


def main() -> None:
	df = db.DF('D:/projects/python/shiki_app/shiki/anime-offline-database/anime-offline-database.json')
	df.refactor_table()
 
	menu(df)
 
	# df.save_excel('answer.xlsx', 'anime')


if __name__ == "__main__":
	main()	