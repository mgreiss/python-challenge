# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open and read the csv
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        total_votes += 1  # Count total votes
        candidate = row[2]  # Get the candidate's name

        # Track votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Generate the output summary
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)