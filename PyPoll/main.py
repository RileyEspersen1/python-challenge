import os
import csv

voting_csv = os.path.join('Resources', 'election_data.csv')

with open(voting_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile,delimiter = ',')
    header = next(csvreader)

    totalVotes = 0
    
    candidateList, uniqueCandidateList, voterIDlist = [], [], []

    mydict = {}

    for row in csvreader:
        
        #total vote count
        totalVotes += 1      
        
        #lists
        candidateList.append(row[2])
        voterIDlist.append(row[0])
        
        #setting point totals
        khanTotal = 0
        correyTotal = 0
        liTotal = 0
        oTooleyTotal = 0

    #getting unique values in the full candidates List
    for i in range(len(candidateList) - 1):
      
        if(candidateList[i] in uniqueCandidateList):
            pass
        else:
            uniqueCandidateList.append(candidateList[i])

    #counting Total votes    
    for i in range(len(voterIDlist) - 1):
        if(candidateList[i] == "Khan"):
                khanTotal += 1
        if(candidateList[i] == "Correy"):
                correyTotal += 1
        if(candidateList[i] == "Li"):
                liTotal += 1
        if(candidateList[i] == "O'Tooley"):
                oTooleyTotal += 1

    # for i in candidateList:
    #unique list
    print("-----------")
    print("Unique Values:")
    for i in uniqueCandidateList:
        print(i)
    
    print("-----------")

    #Percentage Of Votes Calc
    print("Percentage of Votes:")
    khanPercentVote = (khanTotal/totalVotes) * 100
    print("Khan's Percent: %", round(khanPercentVote,3))
    correyPercentVote = (correyTotal/totalVotes) * 100
    print("Correy's Percent: %", round(correyPercentVote,3))
    liPercentVote = (liTotal/totalVotes) * 100
    print("Li's Percent: %" , round(liPercentVote,3))
    oTooleyPercentVote = (oTooleyTotal/totalVotes) * 100
    print("O'Tooley's Percent:  %", round(oTooleyPercentVote, 3))

    print("-----------")

    #voteTotals
    print("Vote Totals:")
    print("khan's total: " + str(khanTotal))
    print("Correy's Total: " + str(correyTotal))
    print("Li's Total: " + str(liTotal))
    print("o'Tooley's Total: " + str(oTooleyTotal))

    #Total Votes
    print("Total Votes: " + str(totalVotes))
    
    #creating dictionary using unique candidates and their vote Totals
    mydict = {str(uniqueCandidateList[0]): khanTotal, str(uniqueCandidateList[1]): correyTotal,
    str(uniqueCandidateList[2]) : liTotal, str(uniqueCandidateList[3]) : oTooleyTotal
    }

    #finding the person with the most amount of votes
    winner = max(mydict, key= mydict.get)
    
    print("-----------")
    print("This is the winner: " +  winner )
    print("-----------") 
    print("Created Dictionary with values")   
    print(mydict)
    print("-----------")

with open("Analysis/poll_results.txt" , "w") as txt_file:
    txt_file.write("Election Results \n")    
    txt_file.write("------------------------------ \n") 
    txt_file.write("Total Votes: " + str(totalVotes) + "\n")
    txt_file.write("------------------------------ \n") 
    txt_file.write(uniqueCandidateList[0] + ": " + str(round(khanPercentVote, 2))+ "% ("+ str(khanTotal)+ ") \n")
    txt_file.write(uniqueCandidateList[1] + ": " + str(round(correyPercentVote, 2))+ "% ("+ str(correyTotal)+ ") \n")
    txt_file.write(uniqueCandidateList[2] + ": " + str(round(liPercentVote, 2))+ "% ("+ str(liTotal)+ ") \n")
    txt_file.write(uniqueCandidateList[3] + ": " + str(round(oTooleyPercentVote, 2))+ "% ("+ str(oTooleyTotal)+ ") \n")
    txt_file.write("------------------------------ \n") 
    txt_file.write("Winner: " + winner + "!!! \n")
    txt_file.write("------------------------------ \n") 
  