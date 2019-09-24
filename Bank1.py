pin = 1111

userpin = int(input("skriv in din pinkod: "))

if pin != userpin:
    exit()


menu = 0
# menu 1 Insättning
# menu 2 Uttag
# menu 3 avsluta
print("1 Insättning, 2 Uttag, 3 Avsluta")
saldo = 1000
while menu != 3:
    print("Ditt saldo är: ", saldo)
    menu = int(input("Skriv ditt val[1, 2, 3]: "))
    if menu == 1:
        saldo = saldo + float(input("gör en insättning: "))
    elif menu == 2:
        saldo = saldo - float(input("gör ett uttag: "))
    else:
        print("Avslut") 



