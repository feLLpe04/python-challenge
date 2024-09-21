import pandas as pd 
csv_path = "Resources/budget_data.csv"
data = pd.read_csv(csv_path)
total_months = data["Date"].nunique()
print("total number of months: ", total_months)
