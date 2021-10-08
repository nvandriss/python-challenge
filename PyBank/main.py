#import
import os
import csv

#set path to csv
csvpath = os.path.join("PyBank","Resources","budget_data.csv")

#variables
monthly_change = []
date = []
total_months = 0
net_total = 0
greatest_increase = 0
g_increase_month = 0
greatest_decrease = 0
g_decrease_month = 0
past_price = 0

#open and read csv file
with open(csvpath, newline='') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    row = next(csvreader)

# calculate net total and total months
    past_price = int(row[1])
    total_months = total_months + 1
    net_total = net_total + int(row[1])
    greatest_increase = int(row[1])
    g_increase_month = row[0]

    for row in csvreader:

        total_months = total_months + 1
        net_total = net_total + int(row[1])

# calculate the overall change
        gen_change = int(row[1]) - past_price
        monthly_change.append(gen_change)
        past_price = int(row[1])
        date.append(row[0])
        # find greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            g_increase_month = row[0]
        # find greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            g_decrease_month = row[0]

#Average Change and Date
    average_change = sum(monthly_change)/len(monthly_change)

    high = max(monthly_change)
    low = min(monthly_change)

print("Financial Analysis")
print("--------------------")
print("Total Months:" + str(total_months))
print("Total: $" + str(net_total))
print("Average Change:" + str(average_change))
print("Greatest Increase in Profits:" + str(g_increase_month) + " $" + str(high))
print("Greatest Decrease in Profits:" + str(g_decrease_month) + " $" + str(low))

#create txt file

output_file = os.path.join(".","PyBank", "Analysis", "budget_analysis.txt")

with open(output_file, 'w',) as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------\n")
    txtfile.write("Total Months:" + str(total_months)+"\n")
    txtfile.write("Total: $" + str(net_total)+"\n")
    txtfile.write("Average Change:" + str(average_change)+"\n")
    txtfile.write("Greatest Increase in Profits:" + str(g_increase_month) + " $" + str(high)+ "\n")
    txtfile.write("Greatest Decrease in Profits:" + str(g_decrease_month) + " $" + str(low))