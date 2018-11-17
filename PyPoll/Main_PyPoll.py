#PyBank

#Output:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#Dependants
import os
import csv

#Variable Declaration
VoterID = []
Ballets = []
Candidatelist = [] #list of candidates
CandidateResults = [] #Couter for total votes
CandidateResultsPercent = []
results = []

results.append("Election Results\n-------------------------")


#Create Path
ElectionDataCSV_Path = os.path.join("Resources", "election_data.csv")


#Open Path as Variable
with open(ElectionDataCSV_Path, 'r') as ElectionDataCSV:
    #Split csv into ElectionData by ','
    ElectionData = csv.reader(ElectionDataCSV, delimiter=',')    
    print("converting data file into lists") # Check Message
    #ignore first line
    next (ElectionData)
    for row in ElectionData:
        #print(row) #Print to check
        VoterID.append(int(row[0]))
        #print(row[0]) #Print to check
        Ballets.append(str(row[2]))
        #print(row[2]) #Print to check
    print("data converted into lists") # Check Message
    print("counting vote") # Check Message
    


#Counter total votes
total_votes = len(list(VoterID))
print ("Total Votes:", total_votes)
results.append("Total Votes: " + str(total_votes)) #append total votes to results list
results.append("-------------------------")


#Complie Candidate List
for vote in Ballets:
    if vote not in Candidatelist:
        Candidatelist.append(vote)
        CandidateResults.append (0) #initialize results list
        #print (vote) #print to confirm adding candidate to list
        #print (CandidateResults) # print to confirm addition to results list


#Count votes for each Candidate on list
for vote in Ballets:
    for i in range (len(list(Candidatelist))):
        if Candidatelist[i]==vote:
            #print(vote, " TRUE") #Check statement for recognizing match
            CandidateResults[i] +=1
            #print (CandidateResults[i]) #print check to show incrimenting vote count


#Calculate Percentage
for i in range (len(list(Candidatelist))):
    CandidateResultsPercent.append (CandidateResults[i]/total_votes*100)
    
#Print to check: show results
for i in range (len(list(Candidatelist))):
    print(Candidatelist[i],":", round(CandidateResultsPercent[i],1), "% (", CandidateResults[i], ")") 
    results.append(Candidatelist[i] + ": "+ str(round(CandidateResultsPercent[i],3)) + "% (" + str(CandidateResults[i]) + ")") 
results.append("-------------------------")


#find winner
#initialize winner and winning result
currentWinningResult = CandidateResults[0]
winner = Candidatelist[0]
for i in range (len(list(Candidatelist))):
    if CandidateResults[i] > currentWinningResult:
        currentWinningResult = CandidateResults[i]
        winner = Candidatelist[i]
print ("Winner:", winner)
results.append("Winner: " + winner)
results.append("-------------------------")


#PRINT RESULTS TO OUTPUT FILE
print("\nWriting txt Results File")
writefile = os.path.join("Resources","CallanYan_PollData_Results.txt")
with open(writefile, 'w') as summary:
    for rows in results:
        summary.write(rows + "\n") 
        
print("Writing txt Results File Complete!!!")
print ("DONE!!!!!")