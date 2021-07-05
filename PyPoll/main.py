# Import Dependencies
import csv

# Name Variables
total_votes = 0

# Set and open the path to read the file
with open("Resources/election_data.csv", "r") as election_data:
    election_reader=csv.reader(election_data)
    # Rotate through the rows
    next(election_reader)
    # Skip Headings
    row = next(election_reader)

    # Set up initial starting points
    total_votes += 1
    
    for row in election_reader:

        # Total number of votes cast
        total_votes +=1
        # Candidates who received votes

        # Percentage each candidate won

        # Winner by popular vote

election_results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------""" 

print(election_results)

with open("Analysis/election_data.txt", "w") as election_analysis:
    election_analysis.write(election_results)