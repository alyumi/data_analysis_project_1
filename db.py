import pandas as pd
import numpy as np
import os
import json
import typing


class DF():
    # Read from json file
    def __init__(self, path: str) -> None:
        self.path = path
        data = json.load(open(path, encoding="UTF-8"))
        self.df = pd.DataFrame(data["data"])


    # Convert DataFrame to Excel
    def save_excel(self, file: str, sheet_name: str) -> None:
        try:
            with pd.ExcelWriter(file, mode='w') as writer: 
                self.df.to_excel(writer, sheet_name=sheet_name)  
        except Exception as e:
            print(e)


    # Convert DataFrame to csv
    def save_csv(self, file: str):
        try:
            self.df.to_csv(file, index=False)  
        except Exception as e:
            print(e)

    # Delete unnecesary colums
    # columns can be string, list of strings
    def clear_table(self, columns):
        try:
            self.df = self.df.drop(columns, axis=1)
        except Exception as e:
            print(e) 

    # Return count of unique instances in columns for plot
    # column can be string, list of strings
    def count(self, columns):
        try:
            ans = self.df[columns].value_counts()
            return ans
        except Exception as e:
            print(e)


    # Return count of unique instances in columns for plot
    # column can be string, list of strings
    # with query
    def query_count(self, query, column):
        try:
            ans = self.df.query(query)[column].value_counts()
            return ans
        except Exception as e:
            print(e)
            
            
    # Divide animeSeason column into season and year columns
    def anime_season(self):
        season = self.df["animeSeason"]
        temp1 = []
        temp2 = []
        for item in season:
            temp1.append(item["season"])
            temp2.append(item["year"])

        sson = pd.Series(temp1)
        year = pd.Series(temp2)

        self.df.insert(3, "season", sson)
        self.df.insert(4, "year", year)


    # REFACTOR TABLE
    def refactor_table(self):
        self.clear_table(columns=["sources", "picture", "thumbnail", "relations"])
        self.anime_season()
        self.clear_table(columns="animeSeason")


    # Return DataFrame
    def get_df(self):
        return self.df