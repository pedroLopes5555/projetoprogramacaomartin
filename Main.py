import Menu
import Levantamentos
import Utilitis
import Login





Utilitis.clear_console()

Login.login()
print(Menu.loadMenuStrings())


case = input("escolha uma opção:\n\n")

if Menu.isInputValueAllowed(case):
    if case ==  "1":
        Utilitis.clear_console()
        print(Levantamentos.getWithdrawalsAsciiArt())
    else:
        print("Escolha Invalida")

