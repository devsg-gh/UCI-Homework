# This code will find unique candidate names, calcuate the %of vote, count of vote and the winner
import csv
import os

#provide the path and read the data from CSV
elec_path = os.path.join(".", "Resources", "election_data.csv")
with open (elec_path,newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvfile)
   # define a empty list to calcuate the length or number of votes
   candidate = []
   for row in csv.reader(csvfile):
       cand_name = row[2]
       candidate.append(cand_name)
       total_votes= len(candidate)
    #define another list to add the candidate who are unique   
   uniq_candidates = []
   for cand_name in candidate:
       if cand_name not in uniq_candidates:
           uniq_candidates.append(cand_name)
    # count the number of votes each candidate got by taking the count of it via indexing in the list
   vote_cnt_index0 = candidate.count(uniq_candidates[0])
   vote_cnt_index1 = candidate.count(uniq_candidates[1])
   vote_cnt_index2 = candidate.count(uniq_candidates[2])
   vote_cnt_index3 = candidate.count(uniq_candidates[3])
   # create a dictionary to store the candidate name and its vote count , also to select a winner 
   dict_data = {uniq_candidates[0]:vote_cnt_index0, 
                uniq_candidates[1]:vote_cnt_index1,
                uniq_candidates[2]:vote_cnt_index2,
                uniq_candidates[3]:vote_cnt_index3
                }
   # calculate the % of vote
   p_index0 = round((vote_cnt_index0/total_votes)*100, 2)
   p_index1 = round((vote_cnt_index1/total_votes)*100, 2)
   p_index2 = round((vote_cnt_index2/total_votes)*100, 2)
   p_index3 = round((vote_cnt_index3/total_votes)*100, 2)
   win_cand = max(dict_data, key=dict_data.get)
   
   # print the required results
   print("Election Results\n-------------------------")
   print(f'Total Votes: {total_votes}\n-------------------------')
   print(f'{uniq_candidates[0]}: {p_index0}% ({vote_cnt_index0})')
   print(f'{uniq_candidates[1]}: {p_index1}% ({vote_cnt_index1})')
   print(f'{uniq_candidates[2]}: {p_index2}% ({vote_cnt_index2})')
   print(f'{uniq_candidates[3]}: {p_index3}% ({vote_cnt_index3})')
   print(f'-------------------------\nWinner: {win_cand}\n-------------------------')
   import sys
   file = open('output.txt', 'w')
   sys.stdout = file
   print("Election Results\n-------------------------")
   print(f'Total Votes: {total_votes}\n-------------------------')
   print(f'{uniq_candidates[0]}: {p_index0}% ({vote_cnt_index0})')
   print(f'{uniq_candidates[1]}: {p_index1}% ({vote_cnt_index1})')
   print(f'{uniq_candidates[2]}: {p_index2}% ({vote_cnt_index2})')
   print(f'{uniq_candidates[3]}: {p_index3}% ({vote_cnt_index3})')
   print(f'-------------------------\nWinner: {win_cand}\n-------------------------')
   file.close()
   