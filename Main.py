import Menu
import Levantamentos
import Utilitis




print(Menu.loadMenuStrings())


case = input("escolha uma opção:\n\n")

if Menu.isInputValueAllowed(case):
    if case ==  "1":
        Utilitis.clear_console()
        print(Levantamentos.getWithdrawalsAsciiArt())

