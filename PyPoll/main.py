# Import Dependencies
import csv

# Name Variables
total_votes = 0
candidates = []
candidate_dict={}
percentage_dict={}

# Set and open the path to read the file
with open("Resources/election_data.csv", "r") as election_data:
    election_reader=csv.reader(election_data)
    # Skip Headings
    row = next(election_reader)
 
    for row in election_reader:
        # Set the candidates variable
        candidate=row[2]
    
        # Total number of votes cast
        total_votes +=1
        
        # Count votes per candidate and 
        # Calculate percentage votes for each candidate 
        if candidate in candidate_dict.keys():
            candidate_dict[candidate]+=1
            percentage_dict[candidate]=candidate_dict[candidate]/total_votes*100
        else:
            candidate_dict[candidate]=1
            percentage_dict[candidate]=candidate_dict[candidate]/total_votes*100

        # Winner by popular vote (call the Key with the Max Value in Candidate_Dict)
        max_key=max(candidate_dict,key=candidate_dict.get)

# Print results to terminal
election_results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {percentage_dict["Khan"]:.3f}% ({candidate_dict['Khan']})
Correy: {percentage_dict["Correy"]:.3f}% ({candidate_dict['Correy']})
Li: {percentage_dict["Li"]:.3f}% ({candidate_dict['Li']})
O'Tooley: {percentage_dict["O'Tooley"]:.3f}% ({candidate_dict["O'Tooley"]})
-------------------------
Winner: {max_key}
-------------------------""" 

print(election_results)

# Export results to txt file.
with open("Analysis/election_data.txt", "w") as election_analysis:
    election_analysis.write(election_results)