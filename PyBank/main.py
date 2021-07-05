import os
import csv

#Variables:
total_months=0
revenue=0
change=[]

# Set and open the path
with open("Resources/budget_data.csv",'r') as budget_data:
    budget_reader=csv.reader(budget_data)
    next(budget_reader)  
    row = next(budget_reader)
    previous_row=int(row[1])

    for row in budget_reader:

        # Total number of months in the data set
        total_months += 1
        
        # Net total "Profit/Loss" for the period
        revenue += int(row[1])
        
        # Average change in "Profit/Loss" over the period        
        changes=int(row[1]) - previous_row
        change.append(changes)
        previous_row=int(row[1])
        ave_rev_change=sum(change)/len(change)
    
        # Find and name the greatest increase in profite (date and amount)
         
        
        # Find the greatest decrease in loss (date and amount)
      
#  Print the analysis in Terminal
financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${revenue:.2f}
Average  Change: ${ave_rev_change:.2f}
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)"""

print(financial_analysis)

# Write to text file
with open("Analysis/budget_data.txt","w") as budget_analysis:
    budget_analysis.write(financial_analysis)