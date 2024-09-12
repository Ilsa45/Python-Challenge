import pandas as pd
import os


# Files for load and output result
data_path = os.path.join("Resources", "election_data.csv")
files_to_output = os.path.join("Analysis", "Results.txt")

# Read csv into a DataFrame
election_data = pd.read_csv(data_path)

# Step 2: Calculate the total number of votes cast
total_votes = len(election_data)

# Step 3: Get a complete list of candidates who received votes
candidates = election_data["Candidate"].unique()

# Step 4: Calculate the total number of votes each candidate received
votes_per_candidate = election_data["Candidate"].value_counts()

# Step 5: Calculate the percentage of votes each candidate won
vote_percentage = (votes_per_candidate / total_votes) * 100

# Step 6: Determine the winner based on the popular vote
winner = votes_per_candidate.idxmax()

# Step 7: Output the results in a readable format
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate in votes_per_candidate.index:
    output += f"{candidate}: {vote_percentage[candidate]:.3f}% ({votes_per_candidate[candidate]})\n"

output += f"-------------------------\n"
output += f"Winner: {winner}\n"

print(output)

# Output to a text file
with open(files_to_output, "w") as txt_file:
    txt_file.write(output)
