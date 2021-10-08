#import
import os
import csv
from typing import List

#set path
csvpath = os.path.join("PyPoll","Resources","election_data.csv")

#variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#open and read csv
with open(csvpath, newline='') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    row = next(csvreader)

    for row in csvreader:
        #total votes
        total_votes = total_votes + 1
        #votes for each candidate
        if (row[2] == "Khan"):
            khan_votes = khan_votes + 1
        elif (row[2] == "Correy"):
            correy_votes = correy_votes + 1
        elif (row[2] == "Li"):
            li_votes = li_votes + 1
        else: otooley_votes = otooley_votes + 1

    #percentage of votes for each candidate
    k_percent = (khan_votes / total_votes)*100
    c_percent = (correy_votes / total_votes)*100
    l_percent = (li_votes / total_votes)*100
    o_percent = (otooley_votes / total_votes)*100

    #find the winner
    winner = max(khan_votes,correy_votes,li_votes,otooley_votes)
    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

print("Election Results")
print("--------------------")
print("Total Votes:" + str(total_votes))
print("--------------------")
print("Khan: " + str(k_percent) + "% " + str(khan_votes))
print("Correy: " + str(c_percent) + "% " + str(correy_votes))
print("Li: " + str(l_percent) + "% " + str(li_votes))
print("O'Tooley: " + str(o_percent) + "% " + str(otooley_votes))
print("--------------------")
print("Winner: " +str(winner_name))
print("--------------------")

#create txt file
output_file = os.path.join(".","PyPoll", "analysis", "election_analysis.txt")

with open(output_file, 'w',) as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------\n")
    txtfile.write("Total Votes:" + str(total_votes)+"\n")
    txtfile.write("--------------------\n")
    txtfile.write("Khan: " + str(k_percent) + "% " + str(khan_votes)+"\n")
    txtfile.write("Correy: " + str(c_percent) + "% " + str(correy_votes)+"\n")
    txtfile.write("Li: " + str(l_percent) + "% " + str(li_votes)+"\n")
    txtfile.write("O'Tooley: " + str(o_percent) + "% " + str(otooley_votes)+"\n")
    txtfile.write("--------------------\n")
    txtfile.write("Winner:" + str(winner_name)+"\n")
    txtfile.write("--------------------")
