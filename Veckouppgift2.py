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
___________________________________________________________________________________________________________"""""

"""""
#Balder
length = int(input("hur lång är du i cm?")) # kan även använda float för att få med decimaltal
if length >= 130:
    print("du får åka")

#elif length > 155:
   #130 print("du får åka")

elif length <= 121:
    print("du får int åka")
----------------------------------------------------------------------------------------------------------------"""""
"""""
#Sportresultat
tottenham = int(input("Hur många mål gjorde Tottenham?"))
liverpool = int(input("Hur många mål gjorde Liverpool?"))
skillnad = abs(tottenham - liverpool)
    if tottenham > liverpool: #om Tottenham har fler mål
    print("Tottenham vann")
    print("laget vann med ", skillnad)
    elif liverpool > tottenham: #om Liverpool har fler mål
    print("Liverpool vann")
    print("laget vann med ", skillnad)
    elif liverpool == tottenham: # om det blir oavgjort
    print("Det blev oavgjort")

-----------------------------------------------------------------------------------------------------------------"""""


#tempraturomvandling version 1:
"""
tempratur_c = float(input("Skriv in en tempratur i Celsius: "))
far = 1.8 * tempratur_c + 32
print("det blir " , float(far), "fahrenheit")
"""

#tempraturomvandling version 2:


#tempraturomvandling version 3:
"""""
tempratur_c = float(input("Skriv in en tempratur i Celsius: "))
far = 1.8 * tempratur_c + 32
cel = (far - 32)/1.8
if cel >= 20:
    print("ta med dig badkläder")
elif cel <= 10:
    print("ta på dig vinterkläder")

tempratur_f =float(input("skriv in en temp i Faren:"))
cel = (tempratur_f - 32)/1.8
print("tempen är i faren")

"""
"""
ange_varde = input("Vill du ange swe eller eng? ")
#ange_varde = str("swe")
if ange_varde == str("swe") :
    print("ja")
#else:

-------------------------------------------------------------------------------------------------------------------"""
#Miniräknare 1
"""""
inmatning_av_tal1 = float(input("Skriv in tal 1: "))
tal1 = inmatning_av_tal1
inmatning_av_tal2 = float(input("Skriv in tal 2: "))
tal2 = inmatning_av_tal2
inmatning_av_tal3 = float(input("Skriv in tal 3: "))
tal3 = inmatning_av_tal3

summa = tal1 + tal2 + tal3
print (summa)
"""
"""""
#Miniräknare 2
inmatning_av_tal1 = float(input("Skriv in tal 1: "))
tal1 = inmatning_av_tal1
inmatning_av_tal2 = float(input("Skriv in tal 2: "))
tal2 = inmatning_av_tal2
inmatning_av_tal3 = float(input("Skriv in tal 3: "))
tal3 = inmatning_av_tal3
if tal1 >= tal2 and tal1 >= tal3:
    print("tal1 är större än tal2 och tal3")
elif tal2 >= tal1 and tal2 >= tal3:
    print("tal2 är större än tal1 och tal3")
elif tal3 >= tal1 and tal3 >= tal2:
    print("tal3 är större än tal1 och tal2")
"""
#Miniräknare 3
inmatning_av_tal1 = float(input("Skriv in tal 1: "))
tal1 = inmatning_av_tal1
inmatning_av_tal2 = float(input("Skriv in tal 2: "))
tal2 = inmatning_av_tal2
inmatning_av_tal3 = float(input("Skriv in tal 3: "))
tal3 = inmatning_av_tal3
if tal1 == tal2 and tal1 == tal3:
    print("alla talen är lika")

elif tal1 == tal2:
    print("tal1 är lika med tal2")
elif tal1 == tal3:
    print("tal1 är lika med tal3")


elif tal2 == tal1:
    print("tal2 är lika med tal1")
elif tal2 == tal3:
    print("tal2 är lika med tal3")


elif tal3 == tal1:
    print("tal3 är är lika med tal1")
elif tal3 == tal2:
    print("tal3 är är lika med tal2")

else:
    print("inget matchar")

#Miniräknaren 4








