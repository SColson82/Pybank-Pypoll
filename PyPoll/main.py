# Import Dependencies
import csv

# Name Variables
total_votes = 0
khan=0
correy=0
li=0
otooley=0
candidates = []

# Set and open the path to read the file
with open("Resources/election_data.csv", "r") as election_data:
    election_reader=csv.reader(election_data)
    # Skip Headings
    row = next(election_reader)
 
    for row in election_reader:
        # Candidates who received votes
        candidate=row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            #print(candidates) #to get and confirm list

        # Total number of votes cast
        total_votes +=1
        
        # Count votes per candidate
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li":
            li+=1
        else:
            otooley += 1
            #print(khan) #to confirm  
           
        # Retrieve vote percentage
        khan_percent=(khan/total_votes)*100
        correy_percent=(correy/total_votes)*100
        li_percent=(li/total_votes)*100
        otooley_percent=(otooley/total_votes)*100
        # print(khan_percent) #to confirm 

        # Winner by popular vote
        winner = max(khan, correy, li, otooley)
        if winner == khan:
            winner_name = "Khan"
        elif winner == correy:
            winner_name = "Correy"
        elif winner == li:
            winner_name = "Li"
        else:
            winner_name = "O'Tooley"

election_results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {khan_percent:.3f}% ({khan})
Correy: {correy_percent:.3f}% ({correy})
Li: {li_percent:.3f}% ({li})
O'Tooley: {otooley_percent:.3f}% ({otooley})
-------------------------
Winner: {winner_name}
-------------------------""" 

print(election_results)

with open("Analysis/election_data.txt", "w") as election_analysis:
    election_analysis.write(election_results)