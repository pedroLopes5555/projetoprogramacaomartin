import getpass
import Utilitis
import time

# Creating a dictionary for the Users and passwords (unsafe)
_users = {
    'Pedro Lopes': 'qwerty1234',
    'Martim Silva': "ola123"
}


def lookAplication():
    Utilitis.clear_console()
    print("-------------------------------------------------------------------------------")
    print("|                 tentativas espiradas... SISTEMA BLOQUEADO                   |")
    print("-------------------------------------------------------------------------------")

    while(True):
        time.sleep(10)  #infinite loop



def login():
    attempts = 0  #numero de tentativas para por username e passaword
    while(attempts < 3):   #a cada cilco soma uma tentativa e nao pode ser maior que 3
        Utilitis.clear_console()
        print("-----------------------------------------------------")
        user = input("Username : ")                             #limpa a cosola e pede o username e a password
        password = getpass.getpass("Enter your password: ")     #a password e pedida, mas nao e mostrada no eccra

        
        if(not user in _users): 
            print("user not found")                 #check if the inouts are correct
        else:
            if(_users.get(user) == password):
                return user
            else:
                print("Password Errada")
    
        attempts+=1

    if attempts == 3 : lookAplication()                ##loock the aplication if the attempts expire
    




        
        


