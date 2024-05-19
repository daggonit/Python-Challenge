import os
import csv
import pandas as pd
#from collections import Counter

Average_Change=[]

row_count = 0
total = 0
Average_Change = 0.0
yearly_change=0
Greatest_Inc_Profits = 0
Greatest_Dec_Profits = 0


df=pd.read_csv(r"election_data.csv")

print(df)

Candidate_Count = len(pd.unique(df.loc[0,2]))

print("Candiate Votes :", Candidate_Count)
#Candidate_column = df.value_counts['Candidate']



#candidate_column_df = Candidate_column.value_counts

#csvpath = os.path.join("..","Resources", "election_data.csv")



#with open (csvpath) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    
    
    #print(csvreader)
    
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #for row in csvreader:
     #   row_count +=1

    #print(f"Total Voters: {row_count}")

    #for 