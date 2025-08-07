import pandas as pd
import time
from pathlib import Path
import numpy as np

#Scrapes NFL combine stats from Pro FootBall Reference and saves each year's data as a CSV into a folder.
#Combines the data into a single CSV and cleans it.
years = [2000]
for i in range(1,21):
    years.append(years[0] + i)

url_template = "https://www.pro-football-reference.com/draft/{}-combine.htm"
csv_template = "{}_draft_combine_stats.csv"
data_frames = []

folder_path = Path("separate_combine_files")
folder_path.mkdir(exist_ok=True)

def height_to_inches(ht):
    try:
        feet, inches = map(int, ht.split('-'))
        return feet * 12 + inches
    except:
        return np.nan

for year in years:
    url = url_template.format(year)
    try:
        #Selects only the first table from the page (main combine data)
        df = pd.read_html(url)[0]
        data_frames.append(df)
        df.to_csv(folder_path / csv_template.format(year), sep="\t", encoding="utf-8", index=False)
        time.sleep(2) #Pauses for 2 seconds so domain doesnt block requests
    except Exception as e:
        print(f"Failed to process {year}: {e}")

combined_df = pd.concat(data_frames, ignore_index=True)
combined_df = combined_df[combined_df["Player"] != "Player"] #Removes repeat header
combined_df = combined_df.drop(columns=["College"]) #Drops column with links to college stats
#Splits up the Drafted (tm/rnd/yr) column into 4 separate columns and drops it
combined_df[["Team", "Round", "Pick", "Year"]] = combined_df["Drafted (tm/rnd/yr)"].str.split(' / ', expand=True)
combined_df = combined_df.drop(columns=["Drafted (tm/rnd/yr)"])
#Extracts the digit from each draft round and pick, turning "6th" to "6" for example
combined_df["Pick"] = combined_df["Pick"].str.extract("(\d+)")
combined_df["Round"] = combined_df["Round"].str.extract("(\d+)")
#Turns the height column into inches
combined_df["Ht"] = combined_df["Ht"].apply(height_to_inches)
combined_df.to_csv("combined_nfl_combine_data.csv", sep="\t", encoding="utf-8", index=False)