#PyParagraph

#dependants
import os
import csv
import re

sentences = []
words = []
letter = []
#Create Path
txtPath1 = os.path.join("raw_data", "paragraph_1.txt")
txtPath2 = os.path.join("raw_data", "paragraph_2.txt")

#Open and convert to variable
#with open(csv_path_read, 'r') as csv_data_read:

with open (txtPath1, 'r', encoding='utf-8') as file:
    #sentences.append(str(file).split('.'))
    sentences = re.split("( )+", file)
    #noSentences = len((list)sentences)

for row in sentences:
    print("")

#print(data)
    
    
#Approximate word count

#Approximate sentence count

#Approximate letter count (per word)

#Average sentence length (in words)