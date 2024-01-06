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
    
    
    def toString(self):
        return f"{self.n_account},{self.user},{self.password},{self.balance},{self.IBAN},{self.banco},{self.nome},{self.balcao}"
    



class Transferencias:
    def __init__(self, user_id, id_transfer, date, value, type):
        self.user_id = user_id
        self.id_transfer = id_transfer
        self.date = date
        self.value = value
        self.type = type

    def toString(self):
        return f"{self.user_id},{self.id_transfer},{self.date},{self.value},{self.type}"





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


def getUserLine(username):
    loadData()
    i = 0
    for account in bankAccounts:
        if username == account.user:
            return i
        i += 1


def changeAccountBalance(username, newBalance):
    csv_file_path = r'db\users_table.csv'

    with open(csv_file_path, 'r') as file:
        lines = file.readlines()

    account = getBankAccountByUser(username);
    account.balance = newBalance 
    lines[getUserLine(username)] = account.toString()

    with open(csv_file_path, 'w') as file:
        file.writelines(lines)


def saveTransfer(user_id, id_tranfer,date,value,type):
    csv_file_path = r'db\transferencias.csv'

    with open(csv_file_path, 'r') as file:
        lines = file.readlines()
    transf = Transferencias(user_id= user_id, id_transfer= id_tranfer, date= date, value= value,type=type)
    lines.append(transf.toString() + "\n")
    with open(csv_file_path, 'w') as file:
        file.writelines(lines)

    
def getLastTrasnferNumber():
    csv_file_path = r'db\lastTransfer.csv'
    with open(csv_file_path, 'r') as file:
        lines = file.readlines()
    return int(lines[0])

def addLastTrasnferNumber():
    csv_file_path = r'db\lastTransfer.csv'
    with open(csv_file_path, 'r') as file:
        lines = file.readlines()
    helper = int(lines[0]) + 1
    lines[0] = str(helper)
    with open(csv_file_path, 'w') as file:
        file.writelines(lines)







def loadData():
    # Open the CSV file and read its contents into the matrix
    with open(r'db\users_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append the row as a list to the matrix
            users.append(row)
            bankAccounts.append(BankAccount(n_account = row[0],user =  row[1],password =  row[2],balance = row[3],IBAN = row[4],banco = row[5],nome = row[6],balcao =row[7]))

    account_moves = []

    # Open the CSV file and read its contents into the matrix
    with open(r'db\transferencias.csv', 'r') as file:
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append the row as a list to the matrix
            account_moves.append(row)
            transfers.append(Transferencias(user_id= row[0], id_transfer=row[1],date=row[2],value=row[3],type=row[4]))



