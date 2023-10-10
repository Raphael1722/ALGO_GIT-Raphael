#a
wort = str(input("Bitte ein Palindrom: "))
wort2 = wort[::-1]
if (wort == wort2):
    print (str(wort) + " ist ein Palindrom")
else:
    print(str(wort) +" ist kein Palindrom")

#b
satz = str(input("Schreib einen Palindromasatz: "))
satz2 = satz[::-1]
if (satz == satz2):
    print ("Gut dein Satz ist ein Palindrom")
else:
    print("Dein Satz ist kein Palindrom")