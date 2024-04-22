import os, random, math
os.system("cls")

class Karakter:
    def __init__(self, nev, kaszt, fegyver):
        #alap adatok
        self.elet = 25
        self.maxelet = 25

        #kepesseg adatok
        self.ability  = 0
        self.kepessegAktivIdo = 0
        self.kepessegHasznalhato = True
        self.kepessegAktiv = True
        
        #megadott adatok
        self.nev = nev
        self.kaszt = kaszt
        self.fegyver = fegyver
        
        #kulombozo kasztok adatai
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

        
        #kezdo ertekek
        self.kezdemenyezes = (self.gyorsasag - 10 or 0) + self.fegyver.sebesseg
        self.vedekezes = (self.ugyesseg - 10 or 0) + self.fegyver.vedekezes 
        self.tamadas = (self.ero - 10 or 0) + self.fegyver.tamadas 
    
    #jatekosok funkcioi:
    def showelet(self):
                 
        if self.elet < 0:
            self.elet = 0
        elet = "["
        elet += math.ceil(self.elet) * math.ceil(self.maxelet - self.elet) * "-"
        elet += f"] : {int(self.elet)}"
        return elet
    
        
    def Kepesseg(self, kaszt, target):
        #nem tudod használni a képességet
        if self.ability  != 0:
            self.ability  -=1
        else:
            self.kepessegHasznalhato = True
        
        if self.kepessegHasznalhato:
            self.kepessegAktiv = True
            self.kepessegHasznalhato = False
        
        if self.kepessegAktiv:
            if kaszt == "harcos":
                self.kepessegAktivIdo = 3
                self.fegyver.sebzes += d(1,6)
                self.vedekezes = round(self.vedekezes * 0.80)
            
            elif kaszt == "tolvaj":
                Attack(self, target, False)
           
            elif kaszt == "pap":
                self.elet += 5
                if self.elet > self.maxelet:
                    self.elet = self.maxelet
    
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
        

kasztList = ["harcos", "tolvaj", "pap"]     

fegyverList = {
    "harcos" : ["Kard", "Pallos", "Buzogány"],
    "tolvaj" : ["Kard", "Tőr", "DobĂłkĂŠs"],
    "pap" : ["Tőr", "Bot"],
}

def d(db, num):
    pontszam = 0
    for _ in range(db):
        pontszam += random.randint(1, num)
    return pontszam

def Attack(self, target, ellenallas):
        if ellenallas:
            tamadas = self.tamadas + d(1, 10)
            vedekezes = target.vedekezes + d(1, 10)
            
            if tamadas > vedekezes:
                target.elet -= self.fegyver.sebzes
        else:
            if self.kaszt == "tolvaj":
                target.elet -= self.fegyver.sebzes * 1.5

def DeathCheck(p1, p2):
    if p1.elet <= 0:
        return True
    elif p2.elet <= 0:
        return True
    else:
        return False

def adatlap(player):
    f = open(f"{player.nev} adat.txt", "w", encoding="utf-8")
    
    f.write(f"{player.nev} adatai: \n")
    f.write(f"Kaszt: {player.kaszt}\n")
    f.write(f"ErĹ: {player.ero} pont\n")
    f.write(f"GyorsasĂĄg: {player.gyorsasag} pont\n")
    f.write(f"ĂgyessĂŠg: {player.ugyesseg} pont\n")
    f.write(f"Fegyver: {player.fegyver.type} pont\n")
    f.write(f"Fegyver sebzes: {player.fegyver.sebzes} pont\n")
    f.write(f"Fegyver sebesseg: {player.fegyver.sebesseg} pont\n")
    f.write(f"Fegyver vedekezes: {player.fegyver.vedekezes} pont\n")
    f.write(f"Fegyver tamadas: {player.fegyver.tamadas} pont\n")
    f.write(f"Képesség: {player.kepesseg}\n")
    f.write(20*"#" + "\n")
    f.write(20*"#")
    
    f.close()
 
def start():
    jatekosSzam = input("Hány Játékos játszik (1 vagy 2): ")
    if jatekosSzam == "1":
        setup(1)
    elif jatekosSzam == "2":
        setup(2)
    else:
        os.system("cls")
        print("Helytelen bevitel!")
        start()

def setup(jatekosSzam):
    global Jatekosok
    Jatekosok = []
    
    if jatekosSzam == 1:
        ValasztottNev = input("Add meg a neved: ")
            
        print("-" * 20)
            
        print("Választható kasztok: ")
        for kaszt in kasztList:
            print("-" + kaszt)
        while True:
            ValasztottKaszt = input("Melyik kasztot választod: ")
            if ValasztottKaszt == "" or ValasztottKaszt not in kasztList:
                print("Helytelen adat!")
                continue
            else:
                break
        
        
        print("-" * 20)
        
        for fegyver in fegyverList[ValasztottKaszt.lower()]:
            print("-" + fegyver)
        while True:
            ValasztottFegyver = input("Melyik fegyvert választod: ")
            if ValasztottFegyver == "" or ValasztottFegyver.capitalize() not in fegyverList[ValasztottKaszt.lower()]:
                print("Helytelen adat!")
                continue
            else:
                break
        
        Player = Karakter(ValasztottNev, ValasztottKaszt.lower(), Fegyver(ValasztottFegyver.lower()))
        Jatekosok.append(Player)
        adatlap(Player)
        botKarakter = random.choice(kasztList)
        bot = Karakter("Enemy", botKarakter, Fegyver(random.choice(fegyverList[botKarakter]).lower()))
        Jatekosok.append(bot)
        adatlap(bot)
        Game(1)     
        
    else:
        for x in range(2):
            print(f"Játékos{x+1}.")
            ValasztottNev = input("Add meg a neved: ")
            
            print("-" * 20)
            
            print("VĂĄlaszthatĂł kasztok: ")
            for kaszt in kasztList:
                print("-" + kaszt)
            while True:
                ValasztottKaszt = input("Melyik kasztot választod: ")
                if ValasztottKaszt == "" or ValasztottKaszt not in kasztList:
                    print("Helytelen adat!")
                    continue
                else:
                    break
            
            print("-" * 20)
            
            for fegyver in fegyverList[ValasztottKaszt.lower()]:
                print("-" + fegyver)
            while True:
                ValasztottFegyver = input("Melyik fegyvert választod: ")
                if ValasztottFegyver == "" or ValasztottFegyver.capitalize() not in fegyverList[ValasztottKaszt.lower()]:
                    print("Helytelen adat!")
                    continue
                else:
                    break
            
            os.system("cls")
            
            Player = Karakter(ValasztottNev, ValasztottKaszt.lower(), Fegyver(ValasztottFegyver.lower()))
            adatlap(Player)
            Jatekosok.append(Player)
        Game(2) 
  
def Game(jatekosok):
    #eldontjuk melyik jatekos kezdemenyez
    if jatekosok == 2:
        if Jatekosok[0].kezdemenyezes + d(1, 10) > Jatekosok[1].kezdemenyezes  + d(1, 10):
            global Jatekos1, Jatekos2
            Jatekos1 = Jatekosok[0]
            Jatekos2 = Jatekosok[1]
        else:
            Jatekos1 = Jatekosok[1]
            Jatekos2 = Jatekosok[0]
    else:
        Jatekos1 = Jatekosok[0]
        Jatekos2 = Jatekosok[1]
        
    if jatekosok == 2:
        while True:
            os.system("cls")
            #jatekosok eletereje
            print(Jatekos1.nev + f" {Jatekos1.showelet()}")
            print(Jatekos2.nev + f" {Jatekos2.showelet()}")
            #megnezzuk hogy meghalt e valamelyik jatekos
            if Jatekos1.elet <= 0:
                print("A Játéknak vége!")
                print(Jatekos2.nev + " a győztes!")
                break
            elif Jatekos2.elet <= 0:
                print("A Játéknak vége!")
                print(Jatekos1.nev + " a győztes!")
                break
            #lepesek bekerese
            Jatekos1Lepes = input(f'{Jatekosok[0].nev}! Mit cselekszel? (Támadás, Védekezés, Képesség): ')
            
            Jatekos2Lepes = input(f'{Jatekosok[1].nev}! Mit cselekszel? (Támadás, Védekezés, Képesség): ')
            #lepesek kivitelezese
            if Jatekos1Lepes.capitalize() == "Támadás" and Jatekos2Lepes.capitalize() == "Támadás":
                Attack(Jatekos1, Jatekos2, True)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Attack(Jatekos2, Jatekos1, True)
            
            elif Jatekos1Lepes.capitalize() == "Támadás" and Jatekos2Lepes.capitalize() == "Védekezés":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Támadás" and Jatekos2Lepes.capitalize() == "Képesseg":
                Attack(Jatekos1, Jatekos2, True)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Jatekos2.Kepesseg(Jatekos2.kaszt, Jatekos1)
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "Támadás":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "Védekezés":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "Képesseg":
                Jatekos2.Kepesseg(Jatekos2.kaszt, Jatekos1)
            
            elif Jatekos1Lepes.capitalize() == "Képesseg" and Jatekos2Lepes.capitalize() == "Támadás":
                Jatekos1.Kepesseg(Jatekos1.kaszt, Jatekos2)
                Attack(Jatekos2, Jatekos1, True)
            
            elif Jatekos1Lepes.capitalize() == "Képesseg" and Jatekos2Lepes.capitalize() == "Védekezés":
                Jatekos1.Kepesseg(Jatekos1.kaszt, Jatekos2)
            
            elif Jatekos1Lepes.capitalize() == "Képesseg" and Jatekos2Lepes.capitalize() == "Képesseg":
                Jatekos1.Kepesseg(Jatekos1.kaszt, Jatekos2)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Jatekos2.Kepesseg(Jatekos2.kaszt, Jatekos1)
                
    else:
        while True:
            os.system("cls")
            #kiirjuk a jatekosok eleterejet
            print(Jatekos1.nev + f" {Jatekos1.showelet()}")
            print(Jatekos2.nev + f" {Jatekos2.showelet()}")
            #megnezzuk hogy meghalt e valamelyik jatekos
            if Jatekos1.elet <= 0:
                print("A játéknak vége!")
                print(Jatekos2.nev + " a győztes!")
                break
            elif Jatekos2.elet <= 0:
                print("A játéknak vége!")
                print(Jatekos1.nev + " a győztes!")
                break
            #lepesek bekerese
            Jatekos1Lepes = input(f'{Jatekosok[0].nev}! Mit cselekszel? (Támadás, Védekezés, képesség): ')
            
            Jatekos2Lepes = random.choice(["támadás", "Védekezés", "képesség"])
            #lepesek kivitelezese
            if Jatekos1Lepes.capitalize() == "támadás" and Jatekos2Lepes.capitalize() == "támadás":
                Attack(Jatekos1, Jatekos2, True)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Attack(Jatekos2, Jatekos1, True)
            
            elif Jatekos1Lepes.capitalize() == "támadás" and Jatekos2Lepes.capitalize() == "Védekezés":
                pass
            
            elif Jatekos1Lepes.capitalize() == "támadás" and Jatekos2Lepes.capitalize() == "képesség":
                Attack(Jatekos1, Jatekos2, True)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Jatekos2.Kepesseg(Jatekos2.kaszt, Jatekos1)
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "támadás":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "Védekezés":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "képesség":
                Jatekos2.Kepesseg(Jatekos2.kaszt, Jatekos1)
            
            elif Jatekos1Lepes.capitalize() == "képesség" and Jatekos2Lepes.capitalize() == "támadás":
                Jatekos1.Kepesseg(Jatekos1.kaszt, Jatekos2)
                Attack(Jatekos2, Jatekos1, True)
            
            elif Jatekos1Lepes.capitalize() == "képesség" and Jatekos2Lepes.capitalize() == "Védekezés":
                Jatekos1.Kepesseg(Jatekos1.kaszt, Jatekos2)
            
            elif Jatekos1Lepes.capitalize() == "képesség" and Jatekos2Lepes.capitalize() == "képesség":
                Jatekos1.Kepesseg(Jatekos1.kaszt, Jatekos2)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Jatekos2.Kepesseg(Jatekos2.kaszt, Jatekos1)
                
start()