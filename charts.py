import pandas as pd

filepath = "may2021/TN/all_candidates.csv"

data = pd.read_csv(filepath)

# print(data)

winners = data[data["Position"] == 1]

# print(winners)

winners.to_csv("winners.csv", index=False)
