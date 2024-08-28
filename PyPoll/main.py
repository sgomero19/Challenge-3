import os
import csv
election_path= r"C:\Users\balth\OneDrive\Desktop\Phyton\Challenge-3\PyPoll\Resources\election_data.csv"
with open(election_path) as csv_file:
  csv_reader=csv.reader(csv_file, delimiter=",")
  csv_header=next(csv_reader)
  Candidate_options=[]
  Candidate_list=[]
  Votes_number=[]
  Total_votes=0
  for row in csv_reader:
    Total_votes +=1
    Candidate_options.append(row[2])
    if row[2] not in Candidate_list:
      Candidate_list.append(row[2])

  for candidate in Candidate_list:
   Count_candidates= (Candidate_options.count(candidate))
   Percent_candidates= (Candidate_options.count(candidate)/Total_votes)*100
 
  print("Elections Result\n")
  print("-----------------------------------")
  print(f"Total Votes: {Total_votes}\n")
  for x in range(len(Candidate_list)):
      print(f"{Count_candidates[x]}")

  









