import os, random, math
os.system("cls")

class Karakter:
    def __init__(self, nev, kaszt, fegyver):
        #hp
        self.hp = 25
        self.maxhp = 25
        
        #kepesseg adatok
        self.Cooldown = 0
        self.kepessegAktivIdo = 0
        self.kepessegHasznalhato = True
        self.kepessegAktiv = True
        
        self.nev = nev
        self.kaszt = kaszt
        self.fegyver = fegyver
        
        #kasztok
        if kaszt == "harcos":
            self.ero = d(1, 10) + 10
            self.gyorsasag = d(2, 6) + 8
            self.ugyesseg = d(3, 6)
            self.kepesseg = "Csatakiáltás"
            
        elif kaszt == "tolvaj":
            self.ero = d(3, 6)
            self.gyorsasag = d(1, 10) + 10
            self.ugyesseg = d(2, 6) + 8
            self.kepesseg = "Hátbaszurás"
            
        elif kaszt == "pap":
            self.ero = d(2, 6) + 8
            self.gyorsasag = d(3, 6)
            self.ugyesseg = d(1, 10) + 10
            self.kepesseg = ""
        
        #kezdo ertekek
        self.kezdemenyezes = (self.gyorsasag - 10 or 0) + self.fegyver.SPD
        self.vedekezes = (self.ugyesseg - 10 or 0) + self.fegyver.DEF 
        self.tamadas = (self.ero - 10 or 0) + self.fegyver.ATT 
    
    #jatekosok funkcioi:
    def showHP(self):
                 
        if self.hp < 0:
            self.hp = 0
        HP = "["
        HP += math.ceil(self.hp) * "\033[1;34;40\033[00m" + math.ceil(self.maxhp - self.hp) * "-"
        HP += f"] : {int(self.hp)}"
        return HP
    
        
    def Kepesseg(self, kaszt, target):
        if self.Cooldown != 0:
            self.Cooldown -=1
        else:
            self.kepessegHasznalhato = True
        
        if self.kepessegHasznalhato:
            self.kepessegAktiv = True
            self.kepessegHasznalhato = False
        
        if self.kepessegAktiv:
            if kaszt == "harcos":
                self.kepessegAktivIdo = 3
                self.fegyver.DMG += d(1,6)
                self.vedekezes = round(self.vedekezes * 0.80)
            
            elif kaszt == "tolvaj":
                Attack(self, target, False)
           
            elif kaszt == "pap":
                self.hp += 5
                if self.hp > self.maxhp:
                    self.hp = self.maxhp
    
class Fegyver:
    def __init__(self, type):
        if type == "kard":
            self.type = "kard"
            self.DMG = d(1, 6) + 3
            self.SPD = 6
            self.DEF = 8
            self.ATT = 6
            
        elif type == "Tőr":
            self.type = "Tőr"
            self.DMG = d(1, 6)
            self.SPD = 10
            self.DEF = 3
            self.ATT = 10
            
        elif type == "bot":
            self.type = "bot"
            self.DMG = d(1, 4)
            self.SPD = 8
            self.DEF = 10
            self.ATT = 8
            
        elif type == "pallos":
            self.type = "pallos"
            self.DMG = d(2, 6)
            self.SPD = 1
            self.DEF = 1
            self.ATT = 5
        
        elif type == "Buzogány":
            self.type = "Buzogány"
            self.DMG = d(2, 4) + 2
            self.SPD = 4
            self.DEF = 5
            self.ATT = 4
        
        elif type == "nagykard":
            self.type = "nagykard"
            self.Sebzés = d(1, 10) + 2
            self.sebb= 5
            self.DEF = 7
            self.ATT = 8
    

kasztList = ["harcos", "tolvaj", "pap"]     

fegyverList = {
    "harcos" : ["Kard", "Pallos", "Buzogány"],
    "tolvaj" : ["Kard", "Tőr"],
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
                target.hp -= self.fegyver.DMG
        else:
            if self.kaszt == "tolvaj":
                target.hp -= self.fegyver.DMG * 1.5

def DeathCheck(p1, p2):
    if p1.hp <= 0:
        return True
    elif p2.hp <= 0:
        return True
    else:
        return False

def adatlap(player):
    f = open(f"{player.nev} adatai.txt", "w", encoding="utf-8")
    
    f.write(f"{player.nev} adatai: \n")
    f.write(f"Kaszt: {player.kaszt}\n")
    f.write(f"Erő: {player.ero} pont\n")
    f.write(f"Gyorsaság: {player.gyorsasag} pont\n")
    f.write(f"Ugyesség: {player.ugyesseg} pont\n")
    f.write(f"Fegyver: {player.fegyver.type} pont\n")
    f.close()
 
def start():
    jatekosSzam = input("Hány Játékos Játszik (1 vagy 2): ")
    if jatekosSzam == "1":
        setup(1)
    elif jatekosSzam == "2":
        setup(2)
    else:
        os.system("cls")
        print("Helytelen bevitt érték!")
        start()

def setup(jatekosSzam):
    global Jatekosok
    Jatekosok = []
    
    if jatekosSzam == 1:
        ValasztottNev = input("Add meg a neved: ")
            
        print("-" * 20)
            
        print("Válaszható kasztok: ")
        for kaszt in kasztList:
            print("-" + kaszt)
        while True:
            ValasztottKaszt = input("Melyik kasztot Választod: ")
            if ValasztottKaszt == "" or ValasztottKaszt not in kasztList:
                print("Helytelen adat!")
                continue
            else:
                break
        
        
        print("-" * 20)
        
        for fegyver in fegyverList[ValasztottKaszt.lower()]:
            print("-" + fegyver)
        while True:
            ValasztottFegyver = input("Melyik fegyvert Választod: ")
            if ValasztottFegyver == "" or ValasztottFegyver.capitalize() not in fegyverList[ValasztottKaszt.lower()]:
                print("Helytelen adat!")
                continue
            else:
                break
        
        Player = Karakter(ValasztottNev, ValasztottKaszt.lower(), Fegyver(ValasztottFegyver.lower()))
        Jatekosok.append(Player)
        adatlap(Player)
        EnemyKarakter = random.choice(kasztList)
        Enemy = Karakter("Enemy", EnemyKarakter, Fegyver(random.choice(fegyverList[EnemyKarakter]).lower()))
        Jatekosok.append(Enemy)
        adatlap(Enemy)
        Game(1)     
        
    else:
        for x in range(2):
            print(f"Játékos{x+1}.")
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
            #kiirjuk a jatekosok eleterejet
            print(Jatekos1.nev + f" {Jatekos1.showHP()}")
            print(Jatekos2.nev + f" {Jatekos2.showHP()}")
            #megnezzuk hogy meghalt e valamelyik jatekos
            if Jatekos1.hp <= 0:
                print("A játéknak vége!")
                print(Jatekos2.nev + " a Győztes!")
                break
            elif Jatekos2.hp <= 0:
                print("A játéknak vége!")
                print(Jatekos1.nev + " a Győztes!")
                break
            #lepesek bekerese
            Jatekos1Lepes = input(f'{Jatekosok[0].nev}! Mit cselekszel? (Támadás, Védekezés): ')
            
            Jatekos2Lepes = input(f'{Jatekosok[1].nev}! Mit cselekszel? (Támadás, Védekezés): ')
            #lepesek kivitelezese
            if Jatekos1Lepes.capitalize() == "Támadás" and Jatekos2Lepes.capitalize() == "Támadás":
                Attack(Jatekos1, Jatekos2, True)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Attack(Jatekos2, Jatekos1, True)
            
            elif Jatekos1Lepes.capitalize() == "Támadás" and Jatekos2Lepes.capitalize() == "Védekezés":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "Támadás":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "Védekezés":
                pass
            
            elif Jatekos2Lepes.capitalize() == "Támadás":
                Attack(Jatekos2, Jatekos1, True)
            
            elif  Jatekos2Lepes.capitalize() == "Védekezés":
                Jatekos1.Kepesseg(Jatekos1.kaszt, Jatekos2)
                
    else:
        while True:
            os.system("cls")
            #kiirjuk a jatekosok eleterejet
            print(Jatekos1.nev + f" {Jatekos1.showHP()}")
            print(Jatekos2.nev + f" {Jatekos2.showHP()}")
            #megnezzuk hogy meghalt e valamelyik jatekos
            if Jatekos1.hp <= 0:
                print("A Játéknak vége")
                print(Jatekos2.nev + " a győztes!")
                break
            elif Jatekos2.hp <= 0:
                print("A Játéknak vége")
                print(Jatekos1.nev + " a győztes!")
                break
            #lepesek
            Jatekos1Lepes = input(f'{Jatekosok[0].nev}! Mit cselekszel? (Támadás, Védekezés): ')
            
            Jatekos2Lepes = random.choice(["Támadás", "Védekezés"])
            #lepesek
            if Jatekos1Lepes.capitalize() == "Támadás" and Jatekos2Lepes.capitalize() == "Támadás":
                Attack(Jatekos1, Jatekos2, True)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Attack(Jatekos2, Jatekos1, True)
            
            elif Jatekos1Lepes.capitalize() == "Támadás" and Jatekos2Lepes.capitalize() == "Védekezés":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Támadás":
                Attack(Jatekos1, Jatekos2, True)
                if DeathCheck(Jatekos1, Jatekos2):
                    continue
                Jatekos2.Kepesseg(Jatekos2.kaszt, Jatekos1)
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "Támadás":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Védekezés" and Jatekos2Lepes.capitalize() == "Védekezés":
                pass
            
            elif Jatekos1Lepes.capitalize() == "Védekezés":
                Jatekos2.Kepesseg(Jatekos2.kaszt, Jatekos1)
            
            elif Jatekos2Lepes.capitalize() == "Támadás":
                Attack(Jatekos2, Jatekos1, True)
            
            elif Jatekos2Lepes.capitalize() == "Védekezés":
                Jatekos1.Kepesseg(Jatekos1.kaszt, Jatekos2)    
start()