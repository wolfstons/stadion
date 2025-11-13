from Stadion import Stadion

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

def elso():
    newstadion_mennyiseg=0
    i=0
    while i<len(stadion_lista):
        if stadion_lista[i].varos == "New York":
            newstadion_mennyiseg+=1
        i+=1
    return newstadion_mennyiseg

 

print(stadion_lista)
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
    while i<len(stadion_lista):
        stadion_lista[i].elso_m
        if kulonbseg>
    print(kulonbseg.days, "nap")