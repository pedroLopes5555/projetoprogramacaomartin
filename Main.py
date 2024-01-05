import Menu
import Levantamentos
import Utilitis
import Login
import pandas as pd
import getpass
import DataManager
import time





Utilitis.clear_console()
print("-----------------------------------------------------")

attempts = 0

while(attempts < 3):
    
    username = input("Username : ")                             #limpa a cosola e pede o username e a password
    password = getpass.getpass("Enter your password: ")     #a password e pedida, mas nao e mostrada no eccra

    if(Login.login(username, password)): break
    attempts += 1

if(attempts == 3): Login.lookAplication()



#username = 'Pedro'
User = DataManager.getBankAccountByUser(username)
    

Utilitis.clear_console()


print("-------------------------------------------------" + username + "-------------------------------------------------")
print(Menu.loadMenuStrings())




def levantamento():
    while(True):
        value = input("Qual o valor a levantar:\n")

        if value.isdigit():
            if(int(User.balance) < int(value)):
                print("Erro, saldo insuficiente")
            else:
                DataManager.changeAccountBalance(username, str(int(User.balance)-int(value)))
                break
        else:
            print("Valor invalido")








while(True):        
    case = input("escolha uma opção:\n\n")
    if case ==  "1":
        Utilitis.clear_console()
        print(Levantamentos.getWithdrawalsAsciiArt())
        levantamento()
    else:
        print("-----ESCOLHA INVALIDA-----")
        time.sleep(2)
        Utilitis.clear_console()
        print("-------------------------------------------------" + username + "-------------------------------------------------")
        print(Menu.loadMenuStrings())




