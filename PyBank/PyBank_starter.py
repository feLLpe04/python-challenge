import pandas as pd 
# CSV file path
csv_path = "Resources/budget_data.csv"
# Load the CSV file into a dataframe
data = pd.read_csv(csv_path)
# Getting total number of months into the dataframe with nunique to have the total 
total_months = data["Date"].nunique()
# Print the total number of months included into the dataframe
print("total number of months: ", total_months)
# Calculate the net total amount of Profit/Losses over the entire period
net_total = data["Profit/Losses"].sum()
# Print the net total amount of Profit/Losses over the entire period into the dataframe Profit/Losses
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
# Print the greatest increase in profits (date and amount) over the entire period
print(f"greatest Increase in Profits: {greatest_increase_date} ($ {greatest_increase})")
# Calculate the greatest decrease in losses (date and amount) over the entire period
greatest_decrease = data['change'].min()
greatest_decrease_date = data['Date'][data['change'].idxmin()]
# Print the greatest decrease in losses (date and amount) over the entire period
print(f"greatest Decrease in Profits: {greatest_decrease_date} ($ {greatest_decrease})")

with open ("PyBank_analysis.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("--------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${round(average_change, 2)}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
    text_file.write("--------------------\n")

