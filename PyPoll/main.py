# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

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
        print(". ", end="")

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


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")

    # Write the total vote count to the text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(f"Total Votes: {total_votes}\n")

    # Initialize variables for vote percentages and winner
    winning_candidate = ""
    winning_count = 0
    candidate_percentages = {}

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_votes.items():

        # Get the vote count and calculate the percentage
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate] = percentage

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        with open(file_to_output, "a") as txt_file:
            txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")


    # Generate and print the winning candidate summary
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {candidate_percentages[winning_candidate]:.3f}%\n"
        f"-------------------------\n"
    )

    print(winning_summary)

    # Save the winning candidate summary to the text file
    with open(file_to_output, "a") as txt_file:
        txt_file.write(winning_summary)
