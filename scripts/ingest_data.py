import os
import pandas as pd
from src.telegram_scraper import scrape_channel
from src.preprocessing import clean_text
from dotenv import load_dotenv

load_dotenv()

# Load channels from the same Excel (or hard-code the first five)
import pandas as pd
channels = pd.read_excel("channels_to_crawl.xlsx", engine="openpyxl").iloc[:5, 0].tolist()

def main():
    dfs = []
    for ch in channels:
        df = scrape_channel(ch, limit=500)
        df["cleaned"] = df["raw"].apply(clean_text)
        dfs.append(df)
    full = pd.concat(dfs, ignore_index=True)
    os.makedirs("data/raw", exist_ok=True)
    full.to_csv("data/raw/telegram_data.csv", index=False)
    print(f" Saved {len(full)} rows to data/raw/telegram_data.csv")

if __name__ == "__main__":
    main()
