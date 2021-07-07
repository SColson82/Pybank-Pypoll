# Import Dependencies
import csv

# Name Variables
total_votes = 0
candidates = []
candidate_dict={}

# Set and open the path to read the file
with open("Resources/election_data.csv", "r") as election_data:
    election_reader=csv.reader(election_data)
    # Skip Headings
    row = next(election_reader)
 
    for row in election_reader:
        # Gather candidates who received votes
        candidate=row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_dict[candidate]=0  
            #print(candidate_dict) to get the candidate names

        # Total number of votes cast
        total_votes +=1
        
        # Count votes (dictionary value) per candidate (dictionary key) and 
        # Calculate percentage votes for each candidate 
        if row[2] == "Khan":
            candidate_dict['Khan'] += 1
            khan_percent = ((candidate_dict['Khan'])/total_votes)*100
        elif row[2] == "Correy":
            candidate_dict['Correy'] += 1
            correy_percent = ((candidate_dict['Correy'])/total_votes)*100
        elif row[2] == "Li":
            candidate_dict['Li']+= 1
            li_percent=((candidate_dict['Li'])/total_votes)*100
        else:
            candidate_dict["O'Tooley"] += 1
            otooley_percent=((candidate_dict["O'Tooley"])/total_votes)*100

        # Winner by popular vote (call the Key with the Max Value in Candidate_Dict)
        max_key=max(candidate_dict,key=candidate_dict.get)

# Print results to terminal
election_results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {khan_percent:.3f}% ({candidate_dict['Khan']})
Correy: {correy_percent:.3f}% ({candidate_dict['Correy']})
Li: {li_percent:.3f}% ({candidate_dict['Li']})
O'Tooley: {otooley_percent:.3f}% ({candidate_dict["O'Tooley"]})
-------------------------
Winner: {max_key}
-------------------------""" 

print(election_results)

# Export results to txt file.
with open("Analysis/election_data.txt", "w") as election_analysis:
    election_analysis.write(election_results)