# PyBank Challenge

# Dependencies
import csv
import os
import sys

# Files for load and output result
files_to_load = os.path.join("Resources", "budget_data.csv")
files_to_output = os.path.join("Analysis", "Results.txt")

# Variables
total_months = 0 
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]  
total_net = 0

# Read csv and convert to dictionary list
with open(files_to_load, mode='r') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header
    header = next(reader) 

    # Extract first row to avoid adding to the net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        # Track total
        total_months += 1
        total_net += int(row[1])

        # Track net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change.append(row[0])

        # Calculate greatest increase 
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate avg net change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Output
output = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months : {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change : ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits : {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease : {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print output
print(output)

# Output to a text file
with open(files_to_output, "w") as txt_file:
    txt_file.write(output)
    