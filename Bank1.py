pin = 1111

userpin = int(input("skriv in din pinkod: "))

if pin != userpin:
    exit()



try: 
    with open("balance.txt", "r")as balanceFile:
        try:
            balance = balanceFile.readline()
            balance = float(balance)
        except (ValueError):
                print("file corrupt")
                balance = 0.0
except (FileNotFoundError):
    balance = 0.0
menu = 0

print("1 Insättning, 2 Uttag, 3 Avsluta")



while menu != 3:
    print("Ditt saldo är: ", balance)
    menu = int(input("Skriv ditt val[1, 2, 3]: "))
    if menu == 1:
        balance = balance + float(input("gör en insättning: "))
    elif menu == 2:
        balance = balance - float(input("gör ett uttag: "))
    else:
        print("Avslut") 




