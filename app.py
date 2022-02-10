import pandas as pd
import numpy as np
import os
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import typing

import json_db


# Method to show different plots
def analyse(figure: int, df: pd.DataFrame) -> None:
	if figure == 1:
		status = json_db.count(columns="status", df=df)
		f1 = plt.figure(1)
		plt.bar(status.index, status.values)
		plt.title("Anime Status Count")
		plt.xlabel("Status")
		plt.ylabel("Count")
		plt.show()

	elif figure == 2: 
		tp = json_db.count(columns="type", df=df)
		f2 = plt.figure(2)
		plt.bar(tp.index, tp.values)
		plt.title("Anime Types Count")
		plt.xlabel("Type")
		plt.ylabel("Count")
		plt.show()

	elif figure == 3:
		years = json_db.qcount(df=df, query="(`year` != None) & (`year` >= 1910) & (`year` < 2022)", column="year")
		years = years.sort_index(ascending=True)
		f3 = plt.figure(3)
		plt.plot(years.index, years.values)
		plt.title("Anime by Years")
		plt.xlabel("Year")
		plt.ylabel("Count")
		plt.show()


# Console menu
def menu(df: pd.DataFrame) -> None:
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
	df = json_db.read()
	df = json_db.refactor_table(df)

	menu(df)

	# json_db.to_excel(df)


if __name__ == "__main__":
	main()	