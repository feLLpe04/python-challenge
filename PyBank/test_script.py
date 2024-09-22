import pandas as pd 
# Path to collect data from the Resources folder
csv_path = "Resources/budget_data.csv"
# Read in the CSV file
data = pd.read_csv(csv_path)
# Calculate the total number of months included in the dataset
total_months = data["Date"].nunique()
# Print the total number of months included in the dataset
print("total number of months: ", total_months)
# Calculate the net total amount of Profit/Losses over the entire period
net_total = data["Profit/Losses"].sum()
# Print the net total amount of Profit/Losses over the entire period
print("net_total ammount of Profit/Losses: $", net_total)
# Calculate the average of the changes in Profit/Losses over the entire period
data['change'] = data["Profit/Losses"].diff()
# Calculate the average of the changes in Profit/Losses over the entire period
average_change = data["change"].mean()
# Print the average of the changes in Profit/Losses over the entire period
print("average of the changes in Profit/Losses: $", round(average_change, 2))
# Calculate the greatest increase in profits (date and amount) over the entire period
greatest_increase = data['change'].max()
greatest_increase_date = data['Date'][data['change'].idxmax()]
print(f"greatest Increase in Profits: {greatest_increase_date} ($ {greatest_increase})")





