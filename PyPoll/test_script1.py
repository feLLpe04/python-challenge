import pandas as pd
csv_path = "Resources/election_data.csv"
data = pd.read_csv(csv_path)
total_votes = data["Ballot ID"].nunique()
print("total_votes: ", total_votes)



