import pandas as pd

# Read in the data from the CSV file
df = pd.read_csv("NFL_stats.csv")

# Group the data by conference and calculate the mean stats for each team
mean_stats = df.groupby("Conference").mean()

# Sort the teams by their win percentage and store the top two from each conference
nfc_winners = mean_stats.sort_values("Win Percentage", ascending=False).head(2)
afc_winners = mean_stats.sort_values("Win Percentage", ascending=False).tail(2)

# Print the predicted Super Bowl matchup
print("Super Bowl Matchup:")
print("NFC:", nfc_winners.index[0], "vs.", afc_winners.index[1])
print("AFC:", nfc_winners.index[1], "vs.", afc_winners.index[0])
