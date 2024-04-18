import os, random, math
os.system("cls")

class Karakter:
    def __init__(self,kaszt,fegyver):
        #hp
        self.elet = 25
        self.maxelet = 25
    
        self.kaszt = kaszt
        self.fegyver = fegyver
        
        #kasztok
        if kaszt == "harcos":
            self.ero = random.randint(1, 10) + 10
            self.gyorsasag = random.randint(2, 6) + 8
            self.ugyesseg = random.randint(3, 6)
            self.kepesseg = "Csatakiáltás"
            
        elif kaszt == "tolvaj":
            self.ero = random.randint(3, 6)
            self.gyorsasag = random.randint(1, 10) + 10
            self.ugyesseg = random.randint(2, 6) + 8
            self.kepesseg = "Hátbaszurás"
            
        elif kaszt == "pap":
            self.ero = random.randint(2, 6) + 8
            self.gyorsasag = random.randint(3, 6)
            self.ugyesseg = random.randint(1, 10) + 10
            self.kepesseg = "gyógyítás"

class Fegyver:
    def __init__(self, type):
        if type == "kard":
            self.type = "kard"
            self.ero = random.randint(1, 6) + 3
            self.sebeseg = 6
            self.vedekezes = 8
            self.tamadas = 6
            
        elif type == "Tőr":
            self.type = "Tőr"
            self.ero = random.randint(1, 6)
            self.sebeseg = 10
            self.vedekezes = 3
            self.tamadas = 10
            
        elif type == "bot":
            self.type = "bot"
            self.ero = random.randint(1, 4)
            self.sebeseg = 8
            self.vedekezes = 10
            self.tamadas = 8
            
        elif type == "pallos":
            self.type = "pallos"
            self.ero = random.randint(2, 6)
            self.sebeseg = 1
            self.vedekezes = 1
            self.tamadas = 4
        
        elif type == "Buzogány":
            self.type = "Buzogány"
            self.ero = random.randint(2, 4) + 2
            self.sebeseg = 4
            self.vedekezes = 5
            self.tamadas = 4
        
kasztList = ["harcos", "tolvaj", "pap"]     

fegyverList = {
    "harcos" : ["Kard", "Pallos", "Buzogány"],
    "tolvaj" : ["Kard", "Tőr"],
    "pap" : ["Tőr", "Bot"],
}