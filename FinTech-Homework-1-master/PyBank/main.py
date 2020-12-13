'''
Instructions:

Your task is to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset.

* The net total amount of Profit/Losses over the entire period.

* The average of the changes in Profit/Losses over the entire period.

* The greatest increase in profits (date and amount) over the entire period.

* The greatest decrease in losses (date and amount) over the entire period.

Your resulting analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
'''

from pathlib import Path
import csv

MAX_VAL = 100000
MIN_VAL = 0
CSV_FILE = Path("Resources/budget_data.csv")

# declare variables
total_num_of_months = 0
net_total_amount = 0
avg_changes = 0
trade_history = []
max_increase = ["date",  MIN_VAL]
max_decrease = ["date", MAX_VAL]


with open(CSV_FILE, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for log in csv_reader:
        
        total_num_of_months += 1
        net_gain = float(log["Profit/Losses"])
        net_total_amount += net_gain
        trade_history.append(net_gain)
        
        if net_gain > max_increase[1]:
            max_increase[0] = log["Date"]
            max_increase[1] = net_gain

        if net_gain < max_decrease[1]:
            max_decrease[0] = log["Date"]
            max_decrease[1] = net_gain

for i in range(1, len(trade_history)):
    avg_changes += trade_history[i] - trade_history[i-1]

avg_changes = avg_changes / total_num_of_months

# Print result
print(f"Financial Analysis \n"
      f"---------------------------- \n"
      f"Total Months: {total_num_of_months} \n" 
      f"Total: ${net_total_amount} \n"
      f"Average Change: ${avg_changes: .2f} \n"
      f"Greatest Increase in Profits: {max_increase[0]}(${max_increase[1]}) \n"
      f"Greatest Decrease in Profits: {max_decrease[0]}(${max_decrease[1]}) \n"
      )
