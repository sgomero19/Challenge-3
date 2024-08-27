import os
import csv
election_path= r"C:\Users\balth\OneDrive\Desktop\Phyton\Challenge-3\PyPoll\Resources\election_data.csv"
with open(election_path) as csv_file:
  csv_reader=csv.reader(csv_file, delimeter=",")
  csv_header=next(csv_reader)
  candidates_name=[]
  Final_candidates_list=[]
  Votes_count=[]
for row in csv_reader:
  candidates_name.append(row[2])
  if not row[2] in Final_candidates_list:
    Final_candidates_list.append(row[2])

Votes_count=len(candidates_name)
for candidate in Final_candidates_list:
  Percent_candidates= [Final_candidates_list.count(candidate)/Votes_count(candidate)]/100
  Number_candidates= candidates_name.count(candidate)
  winner_vote_candidate= max(Number_candidates)
  
print("Election Results")
print("------------------------------------------------")
print(f"Total Votes: {Votes_count}\n")



