import os 
import csv
from statistics import mean

budget_csv = os.path.join('Resources', 'budget_data.csv')

print("Election Results")
print("======================")

#numberOfMonths to print
numberOfMonths = 0 
#counter for total Profit
totalProfitLoss = 0


with open(budget_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csvreader)

    #counter for avg Change
    counter = 0  

    greatestInc, greatestDec, avgChange, finalList, dateTrack  = [], [], [], [], []

    for row in csvreader:

        #adding the profitloss column
        totalProfitLoss += int(row[1])

        #adding the amount of months        
        numberOfMonths += 1

        #greatest inc and dec
        dateTrack.append(row[0])
        greatestInc.append(int(row[1]))
        greatestDec.append(int(row[1]))       
        
        #Average Change
        counter = counter + 1 
        avgChange.append(int(row[1]))
    
    #getting the change
    for i in range(len(avgChange) - 1):
        finalList.append(avgChange[i + 1]- avgChange[i])

    mostIncVal = 0
    mostDecVal = 0 

    #greatestInc Calculation + print date
    for i in range(len(greatestInc) - 1):
        if(greatestInc[i] > mostIncVal):
            mostIncVal = greatestInc[i]
            for j in range(len(dateTrack) - 1):
                indexVal = dateTrack[i]

    #greatestDec Calculation + print date
    for x in range(len(greatestDec) - 1):
        if(greatestDec[x] < mostDecVal):
            mostDecVal = greatestDec[x]
            for j in range(len(dateTrack) - 1):
                indexVal2 = dateTrack[x]

    #mean value to print
    avg = mean(finalList)
       
    #finished print statements
    print("Number of Months: " + str(numberOfMonths))
    print("Total: $" + str(totalProfitLoss))
    print("The average = $", round(avg, 2))
    print("Greatest Inc: ", indexVal ,mostIncVal)
    print("Greatest Dec: ", indexVal2, mostDecVal)      
    
#print to txt file 
with open("Analysis/analysis.txt" , "w") as txt_file:
    txt_file.write("Financial Analysis \n")
    txt_file.write("-------------------- \n")
    txt_file.write("Number of Months: " + str(numberOfMonths) + "\n")
    txt_file.write("Total: $" + str(totalProfitLoss) + "\n")
    txt_file.write("The average = $" + str(round(avg, 2)) + "\n")
    txt_file.write("Greatest Inc: " + str(indexVal) + " " + str(mostIncVal) + "\n")
    txt_file.write("Greatest Dec: " + str(indexVal2) + " " + str(mostDecVal))