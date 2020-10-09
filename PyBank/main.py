import os 
import csv
from statistics import mean

budget_csv = os.path.join('Resources', 'budget_data.csv')

numberOfMonths = 0 

with open(budget_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csvreader)

    #to print/counter for total Profit
    totalProfitLoss = 0

    greatestInc, greatestDec, change, avgChange  = [], [], [], []

    for row in csvreader:
        #adding the profitloss column
        totalProfitLoss += int(row[1])
        #adding the amount of months
        numberOfMonths += 1
        #change amounts
        change.append(row[1])
        greatestInc.append(row[1])
        greatestDec.append(row[1])

    print("Number of Months: " + str(numberOfMonths))
    print("Total: $" + str(totalProfitLoss))
    #print("Average of Changes: " + str(profit))

    print("Greatest Inc: " + max(greatestInc))
    print("Greatest Dec: " + min(greatestDec))   

    for i in change:
        print("this is the loop: " + i)
        
