#import
import os
import csv

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
    
