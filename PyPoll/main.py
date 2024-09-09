import os
import csv
 
def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header
        return list(csv_reader)
 
def count_votes(data):
    candidate_votes = {}
    total_votes = 0
    for row in data:
        candidate = row[2]
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1
        total_votes += 1
    return candidate_votes, total_votes
 
def calculate_results(candidate_votes, total_votes):
    results = []
    for candidate, votes in candidate_votes.items():
        percentage = round(votes / total_votes * 100, 3)
        results.append((candidate, percentage, votes))
    return results
 
def find_winner(candidate_votes):
    return max(candidate_votes, key=candidate_votes.get)
 
def write_results(file_path, total_votes, results, winner):
    with open(file_path, 'w') as file:
        header = (
            "\nElection Results\n"
            "---------------------------------------\n\n"
            f'Total Votes: {total_votes}\n\n'
            "----------------------------------------\n\n"
        )
        file.write(header)
        print(header)
 
        for candidate, percentage, votes in results:
            result_line = f'{candidate}: {percentage}% ({votes})\n'
            file.write(result_line)
            print(result_line, end='')
 
        footer = (
            "\n----------------------------------------\n"
            f'\nWinner: {winner}\n'
            "----------------------------------------\n"
        )
        file.write(footer)
        print(footer)
 
    print(f"Results have been written to '{file_path}'")
 
# Main execution
if __name__ == "__main__":
    csv_path = os.path.join('Resources', 'election_data.csv')
    output_path = 'election_results.txt'
 
    data = read_csv(csv_path)
    candidate_votes, total_votes = count_votes(data)
    results = calculate_results(candidate_votes, total_votes)
    winner = find_winner(candidate_votes)
 
    write_results(output_path, total_votes, results, winner)
    
  









