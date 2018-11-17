#PyBoss

import os
import csv

#Variable Declaration
ID  = []
Name = []
NameFirst = []
NameLast = []
DOB = []
DOB_NewFormat = []
SSN = []
SSN_NewFormat = []
State = []
State_NewFormat = []

StateAbv = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}



#Create Path
csv_path_read = os.path.join("", "employee_data.csv")
print("#Confirm: CSV path created")


#open and read
with open(csv_path_read, 'r') as csv_data_read:
    #skip first line, headers
    next(csv_data_read)
    
    #Read employee data as variable, delimited by ','
    EmpData = csv.reader(csv_data_read, delimiter = ',')
    print("#Confirm: Path converted to variabledata ")    
    #Split into lists
    for row in EmpData:
        ID.append(row[0])
        Name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        State.append(row[4])
    print("#Confirm: Variable data split into lists")


#Determine number of employees
entries = len(list(Name))

#Check list completeness
#for i in Name:
#    print(i)
    

#CHANGE NAME TO FIRST AND LAST NAME from frist and last name to last, first name
for row in Name:
    #print(row) #Print to check original name
    firstName, lastName = row.split(" ") #split into first and last name
    NameFirst.append(firstName)
    NameLast.append(lastName)
print("#Confirm: Name split into first and last names")
"""
#check Names converted to new formats
print(Name[0], "\t--> ", Name_NewFormat[0])    
print(Name[1], "\t--> ", Name_NewFormat[1])    
print(Name[2], "\t--> ", Name_NewFormat[2])    
"""

#change DOB from to MM/DD/YYYY format
for row in DOB:
    #print(DOB) #Print to check original name
    Year, Month, Day = row.split("-") #split into first and last name
    DOB_NewFormat.append(str(Month + "/" + Day + "/" + Year)) #append first and last to new list into new format
print("#Confirm: Chagnge DOB Format")
"""
#check DOB converted to new formats
print(DOB[0], "\t--> ", DOB_NewFormat[0])    
print(DOB[1], "\t--> ", DOB_NewFormat[1])    
print(DOB[2], "\t--> ", DOB_NewFormat[2])  
"""

#change DOB from to MM/DD/YYYY format
for row in SSN:
    newSSN = ("***-**-" + row[-4:])
    SSN_NewFormat.append(newSSN)
print("#Confirm: Chagnge SSN Format")    
"""
#check DOB converted to new formats
print(SSN[0], "\t--> ", SSN_NewFormat[0])    
print(SSN[1], "\t--> ", SSN_NewFormat[1])    
print(SSN[2], "\t--> ", SSN_NewFormat[2])   
"""
#change State to Abreviation
for row in State:
    State_NewFormat.append(StateAbv[row])
print("#Confirm: Chagnge State Format to Abreviation")    
"""
for row in State_NewFormat:
    print (row)
"""

    

#WRITE FILE
#Create Path
csv_path_write = os.path.join("", "employee_data_new.csv")

#Open Path
with open (csv_path_write, 'w') as EmpData_New:
    EmpData_New.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")
    for x in range (0,entries):
        EmpData_New.write(ID[x] + "," + NameFirst[x] + "," + NameLast[x] + "," + DOB_NewFormat[x] + "," + SSN_NewFormat[x] + "," + State_NewFormat[x] + "\n")


print("Complete")
