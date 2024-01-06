import getpass
import Utilitis
import time
import AsciiArt
import DataManager


# Creating a dictionary for the Users and passwords (unsafe)




def lookAplication():
    Utilitis.clear_console()
    print("-------------------------------------------------------------------------------")
    print("|                 tentativas espiradas... SISTEMA BLOQUEADO                   |")
    print("-------------------------------------------------------------------------------")

    while(True):
        time.sleep(10)  #infinite loop



def login(username, password):
    userPass = DataManager.getUsersPasswordsDic()
    attempts = 0  #numero de tentativas para por username e passaword
    while(attempts < 3):   #a cada cilco soma uma tentativa e nao pode ser maior que 3

        if(not username  in userPass):
            print("user dosent exists")
        else:
            if(password == userPass[username]):
                return True
            else:
                print("Password Incorrect")
        return False            
    




        
        


