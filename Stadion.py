from datetime import datetime

class Stadion:
    def __init__(self,stadion_nev:str,varos:str,csapat:int,elso_m:str,utolso_m:str):
        self.stadion_nev=stadion_nev
        self.varos=varos
        self.csapat=csapat
        self.elso_m = datetime.strptime(elso_m, "%Y-%m-%d").date()
        self.utolso_m = datetime.strptime(utolso_m, "%Y-%m-%d").date()
    def __str__(self):
        return f"sor: {self.stadion_nev},{self.varos},{self.csapat},{self.elso_m},{self.utolso_m}"