import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_summary_table = pd.DataFrame(squirrel_data.groupby("Primary Fur Color")["Primary Fur Color"].count())

print(squirrel_summary_table)