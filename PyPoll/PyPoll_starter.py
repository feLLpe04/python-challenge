import pandas as pd
# CSV file path
csv_path = "Resources/election_data.csv"
#Load the CSV file into a dataframe saving it as dataframe = df 
df = pd.read_csv(csv_path)
# Counting the total votes from the dataframe df
total_votes = len(df)
#Counting from the dataframe the Candidates the total votes
vote_count_df = df['Candidate'].value_counts().reset_index()
vote_count_df.columns = ['Candidate', 'Vote Count']
# Votes for each candidate from the df Vote_Count and Total Votes multiply by 100 to get %
vote_count_df['Percentage'] = (vote_count_df['Vote Count'] / total_votes) * 100
# Determine the winner based on the candidate with the most votes on the dataframe Vote_Count
winner = vote_count_df.loc[vote_count_df['Vote Count'].idxmax(), 'Candidate']
# Display the total votes, the dataframe with vote count and % , the winner too
print("Election Results")
print(vote_count_df)
print("Total Votes:", total_votes)
print("Winner:", winner)
with open("Pypoll_analysis.txt", "w") as text_file:
       text_file.write("Election Results\n")
# Step 5: Identify the winner
winner = vote_count_df.loc[vote_count_df['Vote Count'].idxmax(), 'Candidate']

# Results to a text file
with open("PyPoll_analysis.txt", "w") as text_file:
    text_file.write(f"Total Votes: {total_votes}\n")
    for index, row in vote_count_df.iterrows():
        text_file.write(f"{row['Candidate']}: {row['Percentage']:.3f}% ({row['Vote Count']})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")
