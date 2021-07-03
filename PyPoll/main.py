# Warning: this is copy from PyBank. Don't get confused and think this is ready to go.

import csv
total_months = 0
with open("Resources/budget_data.csv", "r") as budget_data:
    budget_reader=csv.reader(budget_data)
    column_names=next(budget_reader)
    for row in budget_reader:
#        print(row)
        total_months += 1

financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)""" 

print(financial_analysis)

with open("Analysis/budget_data.txt", "w") as budget_analysis:
    budget_analysis.write(financial_analysis)