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

def harmadik_feladat():
    i=0
    kilencvenelottistaionok=[]
    datum = datetime(1900, 1, 1).date()
    while i<len(stadion_lista):
        if stadion_lista[i].elso_m <datum:
            kilencvenelottistaionok.append(stadion_lista[i].stadion_nev)
        i+=1
    print(f"1900-elötti stadionok:{kilencvenelottistaionok}")



#4. Hány olyan stadion van, amelyben 200 óta nem volt mérkőzés? 


def negyedik_feladat():
    ketszazevenemvoltmerkozes=0
    i=0
    while i<len(stadion_lista):
        kulombesg=(stadion_lista[i].utolso_m - stadion_lista[i].elso_m).days
        if kulombesg>730:
            ketszazevenemvoltmerkozes+=1
        i+=1
    print(f"200 év óta nem volt mérkőzés:{ketszazevenemvoltmerkozes}")
    return ketszazevenemvoltmerkozes
