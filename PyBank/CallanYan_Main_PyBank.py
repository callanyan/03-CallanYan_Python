#PyBank - Profit/Losses

#Dependants
import os
import csv

#Variable Declarations
date = []
ProfitLoss = []
ProfitLoss_Delta = []
results = []

#OPEN CSV FILE
#Create Path
budget_data = os.path.join("Resources", "budget_data.csv")
print ("Budget Data Path Created")

#Add & Read CSV
with open(budget_data, 'r') as BD_CSV:
    print ("Path Converted to Variable")    
    
    #Split budged data csv file, BD_CSV, into BD
    BD = csv.reader(BD_CSV, delimiter=',')
    print ("Variable Data Delimited to Array")
    
    #ignores first line
    next (BD)


    for row in BD:
        date.append(row[0])
        #print ("dates list complete")
        ProfitLoss.append(float(row[1]))
        #print ("ProfitLoss list complete")
        
    print ("!!!dates list complete!!!")
    print ("!!!ProfitLoss list complete!!!")
    
    """
    for i in date:
        print (i)
    for j in ProfitLoss:
        print (j)
    """

print("Financial Analysis")
print("----------------------------")
#CALCULATE NUMBER OF MONTHS
count_months = len(list(date))
print("Total Months:", count_months)
results.append("Total Months: " + str(count_months))
#print(results[0]) #Check append by printing

#CALCULATE SUM TOTAL OF PROFIT AND LOSS, OVERALL CHANGE
profitLoss_Sum=sum(ProfitLoss)
print("Total: $", round(profitLoss_Sum,2))
results.append("Total: $" + str(round(profitLoss_Sum,2)))
#print(results[1]) # check append by printing

#CALCULATE AVERAGE MONTHLY CHANGE
#Initialize profitLoss_previous
profitLoss_previous = float(ProfitLoss[0])
#Create list ProfitLoss_Delta of monthly Profit Loss Deltas
for i in range(1, count_months):
    #print(ProfitLoss[i] - profitLoss_previous) #Check by printing
    ProfitLoss_Delta.append(float(ProfitLoss[i] - profitLoss_previous))
    profitLoss_previous = ProfitLoss[i]
#Sum ProfitLoss_Delta
ProfitLoss_Delta_Total = sum(ProfitLoss_Delta)
#print (ProfitLoss_Delta_Total) #Check by printing
#Calculate number of monthly profit and loss changes 
ProfitLoss_Delta_Length = len(list(ProfitLoss_Delta))
#print (ProfitLoss_Delta_Length) #Check by printing
#Calculate average monthly change
ProfitLoss_Delta_Average = ProfitLoss_Delta_Total/ProfitLoss_Delta_Length
print ("Average Change: $", round(ProfitLoss_Delta_Average,2))
results.append("Average Change: $" + str(round(ProfitLoss_Delta_Average,2)))
#print(results[2]) # check append by printing

#CALCULATE MAXIMUM MONTHLY INCREASE
#Initialize First Month
profitLoss_MaxInc = float(ProfitLoss_Delta[0])
for j in range (1, ProfitLoss_Delta_Length):
    #ComparisonValue = ProfitLoss_Delta[j]
    #print("ComparisonValue: ", ComparisonValue) #Check by Printing
    if ProfitLoss_Delta[j] > profitLoss_MaxInc:
        profitLoss_MaxInc = float(ProfitLoss_Delta[j])
        date_MaxInc = date[j+1]
print ("Greatest Increase in profits:", date_MaxInc, "($", round(profitLoss_MaxInc,2), ")")
results.append("Greatest Increase in profits: " + date_MaxInc + " ($"+ str(round(profitLoss_MaxInc,2)) + ")")
#print(results[3]) # check append by printing

#CALCULATE MAXIMUM MONTHLY DECREASE
#Initialize First Month
profitLoss_MaxDec = ProfitLoss[0]
for k in range (1, ProfitLoss_Delta_Length):
    if ProfitLoss_Delta[k] < profitLoss_MaxDec:
        profitLoss_MaxDec = float(ProfitLoss_Delta[k])
        date_MaxDec = date[k+1]
print ("Greatest Decrease in profits:", date_MaxDec, "($", round(profitLoss_MaxDec,2), ")")
results.append("Greatest Decrease in profits: "+ date_MaxDec+ " ($"+ str(round(profitLoss_MaxDec,2)) + ")")
#print(results[4]) # check append by printing

#WRITE RESULTS TXT FILE ----------------------
print("\nWriting txt Results File")

CallanYan_FinancialAnalysis = os.path.join("Resources", "CallanYan_FinancialAnalysis.txt")
with open(CallanYan_FinancialAnalysis, 'w') as writeFile:
    writeFile.write("Financial Analysis by Callan Yan\n----------------------------\n")
    for x in results:
        writeFile.write(x+"\n")

writeFile.close()
print("Writing txt Results File Complete!!!")
