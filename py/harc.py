import os, random, math
os.system('cls')

class Karakter:
    def __init__(self,kaszt,fegyver):
        self.kaszt = kaszt
        self.fegyver = fegyver
        self.elet = 25

        #kaszt = Karakter
        #3db kaszt  harcos, tolvaj, pap
        #fegyver = kard, Tőr, bot, pallos, buzogány

        #kasztok definiálása
        if kaszt == "harcos":
            self.ero = random.randint(1, 10) + 10
            self.gyorsasag = random.randint(2, 6) + 8
            self.ugyesseg = random.randint(3, 6)
            self.kepesseg = "Csatakiáltás"
            
        elif kaszt == "tolvaj":
            self.ero = random.randint(3, 6)
            self.gyorsasag = random.randint(1, 10) + 10
            self.ugyesseg = random.randint(2, 6) + 8
            self.kepesseg = "Hátbaszúrás"
            
        elif kaszt == "pap":
            self.ero = random.randint(2, 6) + 8
            self.gyorsasag = random.randint(3, 6)
            self.ugyesseg = random.randint(1, 10) + 10
            self.kepesseg = "Gyógyítás"

#fegyverek definiálása
class Fegyver():
    def __init__(self, type):
        if type == "kard":
            self.type = "kard"
            self.sebzes = random.randint(1, 6) + 3
            self.sebesseg = 6
            self.vedekezes = 8
            self.tamadas = 6
            
        elif type == "Tőr":
            self.type = "Tőr"
            self.sebzes = random.randint(1, 6)
            self.sebesseg = 10
            self.vedekezes = 3
            self.tamadas = 10
            
        elif type == "bot":
            self.type = "bot"
            self.sebzes = random.randint(1, 4)
            self.sebesseg = 8
            self.vedekezes = 10
            self.tamadas = 8
            
        elif type == "pallos":
            self.type = "pallos"
            self.sebzes = random.randint(2, 6)
            self.sebesseg = 1
            self.vedekezes = 1
            self.tamadas = 5
        
        elif type == "buzogány":
            self.type = "buzogány"
            self.sebzes = random.randint(2, 4) + 2
            self.sebesseg = 4
            self.vedekezes = 5
            self.tamadas = 4

#kezdo ertekek kiszamolasa
        self.kezdemenyezes = (self.gyorsasag - 10 or 0) + self.fegyver.sebesseg
        self.vedekezes = (self.ugyesseg - 10 or 0) + self.fegyver.vedekezes 
        self.tamadas = (self.ero - 10 or 0) + self.fegyver.tamadas 
        
#Választható karakterek listája
kasztList = ["harcos", "tolvaj", "pap"]     

fegyverList = {
    "harcos" : ["Kard", "Pallos", "Buzogány"],
    "tolvaj" : ["Kard", "Tőr"],
    "pap" : ["Tőr", "Bot"],
}

# játékos nevánek bekérése
fnev = input("Add meg a nevedet: ")
    
print("-" * 25)
# választahtó kasztok
print("Választható kasztok:")
for kaszt in kasztList:
    print("-" + kaszt)

print("-" * 25)

while True:
    #kaszt kiválastása
    ValasztottKaszt = input("Melyik kasztot választod: ")
    if ValasztottKaszt == "" or ValasztottKaszt not in kasztList:
        print("Helytelen adat!")
        continue
    else:
        break   

#Választható fegyverek kiirása 
for fegyver in fegyverList[ValasztottKaszt.lower()]:
    print("-" + fegyver)

while True:
    # fegyver kiválszatása
    #ValasztottFegyver = amit mi kiválasztotunk fegyver
    ValasztottFegyver = input("Melyik fegyvert választod: ")
    if ValasztottFegyver == "" or ValasztottFegyver.capitalize() not in fegyverList[ValasztottKaszt.lower()]:
        print("Helytelen adat!")
        continue
    else:
        break

os.system("cls")

while True:
    Jatekos1Lepes = input(f"{fnev}! Mit cselekszel? (Támadás 1, Védekezés 2, Képesség 3): ")
    Jatekos2Lepes = input("bot! Mit cselekszel? (Támadás 1, Védekezés 2, Képesség 3): ")
    hossz = "{fnev}! Mit cselekszel? (Támadás 1, Védekezés 2, Képesség 3): "
    print()
    print("-" * len(hossz))
    print()