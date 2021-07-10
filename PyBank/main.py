# Import Dependencies
import csv

# Name variables:
total_months=0
revenue=0
change=[]
greatest_profit_increase=0
greatest_profit_decrease=0

#Set and open the path to the read file
with open("Resources/budget_data.csv",'r') as budget_data:
    budget_reader=csv.reader(budget_data)
    #Rotate through the rows
    next(budget_reader)  
    # Skip Headings
    row = next(budget_reader)
    
    # Set up initial starting points
    previous_row=int(row[1])
    total_months += 1
    revenue += int(row[1])

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
    
        # Greatest increase in profit (date and amount)
        if changes > greatest_profit_increase:
            greatest_profit_increase = changes
            greatest_profit_inc_mo = row[0]

        # Find the greatest decrease in loss (date and amount)
        if changes < greatest_profit_decrease:
            greatest_profit_decrease = changes
            greatest_profit_dec_mo = row[0]

#  Print the analysis in Terminal
financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${revenue:.2f}
Average  Change: ${ave_rev_change:.2f}
Greatest Increase in Profits: {greatest_profit_inc_mo} (${greatest_profit_increase:.2f})
Greatest Decrease in Profits: {greatest_profit_dec_mo} (${greatest_profit_decrease:.2f})"""

print(financial_analysis)

# Export text file
with open("Analysis/budget_data.txt","w") as budget_analysis:
    budget_analysis.write(financial_analysis)