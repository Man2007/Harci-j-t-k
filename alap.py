import os, random
os.system("cls")


kasztList = ["harcos", "tolvaj", "pap"]    
harcos = {
            "tuljadonság":[erő]
        }

ero = random.randint(1,10)+10
gyorsasag = random.random(1.6) + random.randint(1,6)
ugyesseg = random.randint(1,6) + random.randint(1,6)


f_sebzes = random.randint(1.6) + 3
f_sebesseg = 6 
f_vedekezes = 8
f_tamadas = 6 

elet = 25
kezdemenyezes = gyorsasag - 10   + f_sebesseg
védekezes =  ugyesseg - 10 + f_vedekezes
tamadas = ero - 10 + f_tamadas
print(kezdemenyezes)
print(tamadas)



