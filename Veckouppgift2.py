"""""
                is_member = False
                level1 = 100
                level2 = 300
                discount = 0

                price = input ("Välkommen, köp något dyrt: ")
                price = float(price)
                if price > level1:
                    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
                    discount = discount + 10
                if price >= level2:
                    print("Grattis du har avanerat till nivå 2 och får 25% rabatt.")
                    discount = discount + 25
                
                
                final_price = price *(100 - discount) / 100
                print ("efter rabatter blir priset....", str(final_price))
                """""

"""""
#Balder
length = int(input("hur lång är du i cm?")) # kan även använda float för att få med decimaltal
if length >= 130:
    print("du får åka")

#elif length > 155:
   #130 print("du får åka")

elif length <= 121:
    print("du får int åka")
"""""

 #Sportresultat
tottenham = int(input("Hur många mål gjorde Tottenham?"))
liverpool = int(input("Hur många mål gjorde Liverpool?"))
skillnad = tottenham - liverpool
if tottenham > liverpool: #om Tottenham har fler mål
    print("Tottenham vann")
    print("laget vann med ", skillnad)
elif liverpool > tottenham: #om Liverpool har fler mål
    print("Liverpool vann")
    print("laget vann med ", skillnad)
elif liverpool == tottenham: # om det blir oavgjort
    print("Det blev oavgjort")
















