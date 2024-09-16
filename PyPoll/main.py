##PyPoll Challenge

#Dependencies
import os
import csv


# Files for load and output result
data_path = os.path.join("Resources", "election_data.csv")
files_to_output = os.path.join("Analysis", "Results.txt")

# Variables
total_votes = 0
candidates = {}
winner = ""

# Read csv into a list
with open(data_path, mode='r') as election_data:
    reader = csv.reader(election_data)
    header = next(reader)  # Skip the header row

    # Count total votes and votes per candidate
    for row in reader:
        total_votes += 1
        candidate = row[2]  # Using number 2 because it actually implies the third column

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate recieved 
vote_percentage = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Determine the winner based on the popular vote
winner = max(candidates, key=candidates.get)

# Output the results 
output = (
    f"Election Results\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")

for candidate, votes in candidates.items():
    output += f"{candidate}: {vote_percentage[candidate]:.3f}% ({votes})\n"

output += f"-------------------------\n"
output += f"Winner: {winner}\n"
output += f"-------------------------\n"

print(output)

# Output to a text file
with open(files_to_output, "w") as txt_file:
    txt_file.write(output)