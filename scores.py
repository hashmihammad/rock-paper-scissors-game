import pandas as pd
import os

CSV_FILE = "high_scores.csv"

def save_score(name, score, date, time):
    new_entry = pd.DataFrame([[name, score, date, time]], columns=["Name", "Score", "Date", "Time"])

    if os.path.exists(CSV_FILE):
        existing = pd.read_csv(CSV_FILE)
        existing.columns = existing.columns.str.strip()
        existing = existing[["Name", "Score", "Date", "Time"]]
        data = pd.concat([existing, new_entry], ignore_index=True)
    else:
        data = new_entry

    data.to_csv(CSV_FILE, index=False)

def show_high_scores():
    if not os.path.exists(CSV_FILE):
        print("\nNo scores yet. Be the first to play!\n")
        return

    data = pd.read_csv(CSV_FILE)
    data.columns = data.columns.str.strip()
    data = data[["Name", "Score", "Date", "Time"]]

    if data.empty:
        print("\nNo scores yet. Be the first to play!\n")
        return

    top_scores = data.sort_values(by="Score", ascending=False).reset_index(drop=True)
    top_scores.insert(0, "Rank", range(1, len(top_scores) + 1))

    print("\nTop 5 High Scores:\n")
    print(top_scores.head(5).to_string(index=False))
