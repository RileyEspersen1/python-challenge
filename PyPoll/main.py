import os
import csv

voting_csv = os.path.join('Resources', 'election_data.csv')

candidateList = []

def print_info(data):

    voterID = int(data[0])
    county = str(data[1])
    candidate = str(data[2])



    #trying to print out candidate list
    if candidate not in candidateList:
        candidateList.append(candidate)
    #''
    for i in candidateList:
        print (i)
    
with open(voting_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile,delimiter = ',')
    header = next(csvreader)

    totalVotes = 0
    
    for row in csvreader:
        totalVotes += 1      
        print_info(row)
   
    #done
    print("Total Votes: " + str(totalVotes))
    
    
    
    
  