import os
import csv

election_data_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Resources', 'Election_Output.txt')
output = open(output_path, 'w')
candidate = []
unique_candidate = []
votes = []
percent = []
total_votes = 0
index_offset = 0

with open(election_data_path, newline = '') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        candidate.append(row[2])
    
    total_votes = len(candidate)

    candidate.sort()
    candidate.append("@*hiahaeosadsealah")# junk value to find last candidate, otherwise last candidate will not append to list
    #Finds the number of votes per candidate, stores vote count and corresponding candidate in two lists with matching indices
    key = candidate[0]
    for i in range(len(candidate)):
        if candidate[i] != key:
            votes.append(i - index_offset)
            index_offset = i
            unique_candidate.append(key)
            key = candidate[i]
    candidate.pop(-1) #Remove junk value from candidate list
        
    #Sort vote count and corresponding candidate from highest to lowest
    max_candidate = unique_candidate[0]
    max_value = votes[0]
    temp_index = 0
    for i in range(len(votes)):
        if votes[i] > max_value:
            temp_value = max_value
            temp_candidate = max_candidate
            max_value = votes[i]
            max_candidate = unique_candidate[i]
            votes[temp_index] = max_value
            unique_candidate[temp_index] = max_candidate
            votes[i] = temp_value
            unique_candidate[i] = temp_candidate
            temp_index = i
    winner = unique_candidate[0]
    
    #Calculate percentage of votes
    for i in votes:
       percent.append((i/total_votes)*100)
    
    #Dispay data
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for i in range(len(unique_candidate)):
        print(f"{unique_candidate[i]}: {percent[i]:.3f}% ({votes[i]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    #Write to file
    print("Election Results", file = output)
    print("-------------------------", file = output)
    print(f"Total Votes: {total_votes}", file = output)
    print("-------------------------", file = output)
    for i in range(len(unique_candidate)):
        print(f"{unique_candidate[i]}: {percent[i]:.3f}% ({votes[i]})", file = output)
    print("-------------------------", file = output)
    print(f"Winner: {winner}", file = output)
    print("-------------------------", file = output)
    output.close()

    




             

    
