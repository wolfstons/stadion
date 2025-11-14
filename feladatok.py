from Stadion import Stadion
from datetime import datetime

stadion_lista=[]
def beolvasas():
    a_beolvasott_lista_teljes_tartalma = open("stadion.txt","r",encoding="UTF-8")
    a_beolvasott_lista_teljes_tartalma.readline()
    teljestxt=a_beolvasott_lista_teljes_tartalma.readlines()
    """teljestxt egy lista amelynek minden eggyes eleme egy szöveg"""
    print(teljestxt)
    a_beolvasott_lista_teljes_tartalma.close()

    i=0
    while i<len(teljestxt):
        sor=teljestxt[i].strip().split(";")
        stadion=Stadion(sor[0],sor[1],int(sor[2]),sor[3],sor[4])
        stadion_lista.append(stadion)
        i+=1
    return stadion_lista

def elso():
    newstadion_mennyiseg=0
    i=0
    while i<len(stadion_lista):
        if stadion_lista[i].varos == "New York":
            newstadion_mennyiseg+=1
        i+=1
    return newstadion_mennyiseg

 

def masodikfeladat():
    csaptaennyiseg=0
    i=0
    while i<len(stadion_lista):
        stadion_lista[i]
        csaptaennyiseg+=stadion_lista[i].csapat
        i+=1
    return csaptaennyiseg

def harmadik_feladat(stadion_lista):
    i=0
    stadiumlista=[]
    datum = datetime(1999, 1, 1).date()
    while i<len(stadion_lista):
        if stadion_lista[i].elso_m <datum:
            stadiumlista.append(stadion_lista[i].stadion_nev)
    print(stadion_lista)
beolvasas()
harmadik_feladat(stadion_lista)