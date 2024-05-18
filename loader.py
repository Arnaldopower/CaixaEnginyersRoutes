import csv

def read_tsv(filename) -> list[list]:
    with open(filename, encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        data = [row for row in reader]
    return data

# Example usage:
if __name__ == "__main__":
    filename = 'input.tsv'
    data = read_tsv(filename)
    for row in data:
        print(row)