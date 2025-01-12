print("Hello world")
print("This program was made by MonirehBergstrom.")

biljettPris = 100  # biljettpris
fickPengar = 200  # pengar på fickan
print("Det blir " + str(fickPengar - biljettPris) + " kronor över.")
z = (200 - 100) / 2
print("Hälften är: " + str(z))

#Vi har hittat tre sätt att skriva ut strängar.
#Med konvertering tex str(variabel) med ,(komma) och med print(f...

x = input("Skriv in ett heltal:")
print(x)
y = input ("skriv in ett heltal:")
print(f"Summan av talen är: {int(x) + int(y)}")


#uppgift 3.2.a
jacka = 2000
rea_procent = 50
slut_pris = jacka * rea_procent / 100
print ("jackan kostar: " + str(slut_pris) +"kronor med " +str(rea_procent )+"% rabatt")



jacka = 2000
rabatt = input("Vilken rabatsats är det på jackan?")
rabattSumma = jacka * (int(rabatt)/100)
slutSumma = jacka - rabattSumma
print("Jackan kostar:" + str(slutSumma)+ "kronor med " + str(rabatt) + "% rabatt")
