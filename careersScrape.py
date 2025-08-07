import pandas as pd
import time
from pathlib import Path

#Scrapes NFL draft class career stats from Pro FootBall Reference and saves each year's data as a CSV into a folder.
#Combines the data into a single CSV and cleans it.
years = [2000]
for i in range(1,21):
    years.append(years[0] + i)

url_template = "https://www.pro-football-reference.com/years/{}/draft.htm"
csv_template = "{}_draft_career_stats.csv"
data_frames = []

folder_path = Path("separate_career_files")
folder_path.mkdir(exist_ok=True)

for year in years:
    url = url_template.format(year)
    try:
        #Using the second row for column headers (real headers start on the second row)
        #Selects only the first table from the page (main draft data)
        df = pd.read_html(url,header=1)[0]
        df["Year"] = year
        data_frames.append(df)
        df.to_csv(folder_path / csv_template.format(year), sep="\t", encoding="utf-8", index=False)
        time.sleep(2)  #Pauses for 2 seconds so domain doesnt block requests
    except Exception as e:
        print(f"Failed to process {year}: {e}")

combined_df = pd.concat(data_frames, ignore_index=True)
combined_df = combined_df[combined_df["Rnd"] != "Rnd"] #Removes repeat header
combined_df = combined_df.drop(columns=["Unnamed: 28"]) #Drops column with links to college stats
combined_df.to_csv("combined_career_data.csv", sep="\t", encoding="utf-8", index=False)
