
import csv
import os

Election_data = os.path.join("Resources", "election_data.csv")
print(Election_data)

Ballot_id = []
Candidate_id = []
Total_count = []

Charles_C = 0
Diana = 0
Raymon = 0


with open(Election_data, 'r') as Election:
    reader=csv.reader(Election, delimiter=",")
    Header = next(Election)
    print(Header)
    
    
    for row in reader:
        Candidate = {"Candidate": ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]}
        
        if row[2] == "Charles Casper Stockham":
            Charles_C += 1
        
        if row[2] == "Diana DeGette":
            Diana += 1
        
        if row[2] == "Raymon Anthony Doane":
            Raymon += 1

Total = Charles_C + Diana + Raymon
           
print("Charles Casper Stockham:", Charles_C/Total*100, Charles_C)
print("Diana DeGette:", Diana/Total*100, Diana)
print("Raymon Anthony Doane:", Raymon/Total*100, Raymon)

Candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

Candidate_votes = [Charles_C, Diana, Raymon]
print(Candidates[Candidate_votes.index(max(Candidate_votes))])


