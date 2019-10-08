pin = 1111

userpin = int(input("skriv in din pinkod: ")) #nu lägger man ett vrde till userpin och med int funktionen så kan man bara skriva med siffror annars blir det fel.

if pin != userpin: #om inte pin koden stämmer med värdet pin så stängs pogrammet av.
    exit()



try: 
    with open("balance.txt", "r")as balanceFile: # med try funktionen så ber man pogrammet försöka öppna filen "balance.txt" sen så försöker den att innehållet i filen ska bli ett värde till balance och sen få kör den genom filen med float så att man får ut bara siffor och inte text.
        try:
            balance = balanceFile.readline()
            balance = float(balance)
        except (ValueError):
                print("file corrupt")
                balance = 0.0
except (FileNotFoundError): #om den inte kan inte filen eller något annat inte fungerar så ger den balance värdet 0.0 och man kan forsätta använda pogrammet.
    balance = 0.0
menu = 0

print("1 Insättning, 2 Uttag, 3 Avsluta") #nu printar pogrammet ut alla alternativ så att man vet vad 1,2,3 gör



while menu != 3: #nu loopas pogrammet på 3, sedan så printar pogrammet ut ens saldo och efter det printar den alla valen och använder int på ens val så att man bara kan skriva med siffror 
    print("Ditt saldo är: ", balance)
    menu = int(input("Skriv ditt val[1, 2, 3]: "))
    if menu == 1: #om man valde 1 så kommer man till insättnings menyn där pogrammet tar balace och sen så används float för att skriva in vilket värde man vill lägga till balance.
        balance = balance + float(input("gör en insättning: "))
    elif menu == 2: # om man valde 2 så kommer man till uttags menyn där pogrammet tar balance och sen subtraherar det med värde man skriver som även går igenom float så att man bara kan skriva med siffror med decimaler.
        balance = balance - float(input("gör ett uttag: "))
    else: #om 
        exit() print("Avslut") 




