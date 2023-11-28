import csv

# Specify the path to your CSV file
csv_file_path = r'db\users_table.csv'

# Initialize an empty list to store the data
users = []

# Open the CSV file and read its contents into the matrix
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the row as a list to the matrix
        users.append(row)

# Now, 'matrix' contains the data from the CSV file
print(users)



def getUserLine(user_name):
    result = 0
    for user in users:
        if(user[1] == user_name): 
            return result
        else:
            result+=1
    return result



def checkUserExists(user_name):
    for user in users:
        if(user[1] == user_name): return True

    return False


def getUserPassword(user_name):
    if not checkUserExists(user_name):
        return None
    return users[2][getUserLine(user_name)]
    





# Specify the path to your CSV file
csv_file_path = r'db\transferencias.csv'

# Initialize an empty list to store the data
account_moves = []

# Open the CSV file and read its contents into the matrix
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the row as a list to the matrix
        account_moves.append(row)

# Now, 'matrix' contains the data from the CSV file
print(account_moves)
