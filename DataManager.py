import csv

class BankAccount:
    def __init__(self, n_account, user, password, balance, IBAN, banco, nome, balcao):
        self.n_account = n_account
        self.user = user
        self.password = password
        self.balance = balance
        self.IBAN = IBAN
        self.banco = banco
        self.nome = nome
        self.balcao = balcao

class Transferencias:
    def __init__(self, user_id, id_transfer, date, value):
        self.user_id = user_id
        self.id_transfer = id_transfer
        self.date = date
        self.value = value


# Specify the path to your CSV file
csv_file_path = r'db\users_table.csv'

bankAccounts  = []

users = []

transfers = []

usersPasswordDic = {

}

def getBankAccountByUser(user):
    loadData()
    for account in bankAccounts:
        if user == account.user:
            return account

def getBankAccounts():
    loadData()
    return bankAccounts

def getTransfers():
    loadData()
    return transfers

def getUsersPasswordsDic():
    loadData()
    return {user[1]: user[2] for user in users}



def loadData():
    # Open the CSV file and read its contents into the matrix
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append the row as a list to the matrix
            users.append(row)
            bankAccounts.append(BankAccount(n_account = row[0],user =  row[1],password =  row[2],balance = row[3],IBAN = row[4],banco = row[5],nome = row[6],balcao =row[7]))


    icsv_file_path = r'db\transferencias.csv'
    account_moves = []

    # Open the CSV file and read its contents into the matrix
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append the row as a list to the matrix
            account_moves.append(row)
            transfers.append(Transferencias(user_id= row[0], id_transfer=row[1],date=row[2],value=row[3]))

def createNewUser():
    print("todo")





# Now, 'matrix' contains the data from the CSV file
#print(users)
#print(users[1][1])



# Specify the path to your CSV file


# Initialize an empty list to store the data



