# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "Analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        # print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1  # Count total votes

        # Get the candidate's name from the row
        candidate = row[2]  # Get the candidate's name

        # If the candidate is not already in the candidate list, add them
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1

        # Add a vote to the candidate's count
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

# Save the winning candidate summary to the text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
