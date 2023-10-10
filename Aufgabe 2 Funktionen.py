#a
def kleiner(a,b):
    if (a > b):
        print(b)
    else:
        print(a)

kleiner(2,4)

#b
def longest (wort1, wort2, wort3):
    laenge1 =  len(wort1)
    laenge2 = len(wort2)
    laenge3 = len(wort3)
    if (laenge1 > laenge2 and laenge1 > laenge3):
        return (wort1)
    elif(laenge2 > laenge1 and laenge2 >laenge3):
        return(wort2)
    else:
        return(wort3)

print(longest("Hallo", "Moin", "Okeeee"))

#c
def pythagoras(a,b):
    resultat_p = a**2 + b**2
    resultat_p = resultat_p**0.5
    return resultat_p
print(pythagoras(10,20))

#d
def umfangrechteck(a,b):
    resultat_u = 2 * a + 2 * b
    return resultat_u
print(umfangrechteck(30,20))

#e
def flaecheKugel(r):
    resultat_f = 4*3.1415 * r**2
    return resultat_f
print(flaecheKugel(10))

#f
def notenberechnung(max, erreichte):
    note = erreichte/max*5+1
    return note
print(notenberechnung(6,4))