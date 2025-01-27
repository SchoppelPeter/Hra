import random
import time

dontbreak = False
name = None
bank = 0
speedrun_mode = True




def listen2choices(listOfChoices,exclude):
    n = 1
    for c in listOfChoices:
        print(f"{n} ~ {c}")
        n+=1
    inpt = input("Jakou cestu si vybereš? : ")
    
    while True:

        if inpt.isnumeric()!=True:
            inpt = input(f"Neplatný údaj - vyber mezi 1 - {len(listOfChoices)} : ")
            continue
        elif int(inpt)>len(listOfChoices) or int(inpt)<1:
            inpt = input(f"Neplatný údaj - vyber mezi 1 - {len(listOfChoices)} : ")
            continue
        
        if int(inpt)==exclude:
            inpt = input(f"Cesta není zatím přístupná - vyber mezi 1 - {len(listOfChoices)} KROMĚ {exclude} : ")
            continue
        
        break
            
    ### MISSION: accomplish checking for text or diff number -- ACCOMPLISHED!

    
    return int(inpt)


def _showName():
    return name


def _bprint(content): #print with break

    print(content+"\n") if dontbreak!=True else print(content)
def wait(seconds):
    if speedrun_mode:
        return
    if seconds:
        time.sleep(seconds)
    else:
        time.sleep(1)


def _UVOD():
    global dontbreak
    global name
    global speedrun_mode
    dontbreak = True

    _bprint(".......................")
    _bprint(".......................")

    print("Chceš aktivovat speedrun mode? 1-ANO, 2-NE")
    spdrn = input("Cokoliv jiného než číslovka nebo jiné číslo znamená 'NE': ")
    if spdrn == "1":
        speedrun_mode = True
    else:
        speedrun_mode = False

    if speedrun_mode:
        _bprint("SPEEDRUN ACTIVATED!")
    _bprint(".......................")
    _bprint(".......................")
    wait(1)
    dontbreak = False
    _bprint("Vítej... hmm.. tvé jméno není známo..")
    wait(3)
    name = input("Jakou přezdívku si zvolíš? : ")
    _bprint("..")
    wait(1.3)
    _bprint("..")
    wait(1.7)
    _bprint(f"Zajímavé jméno, {name}!")

    wait(1.5)

    _bprint("Mám na tebe jednu otázku..")
    wait(1.4)
    _bprint("Toužil si, hráči, po bohatství, který by sám Elon Musk záviděl?")
    wait(2)
    _bprint("Či po lásce? Najít toho pravého, co s tebou bude sdílet zbytek života?")
    wait(2.38)
    _bprint("Nebo snad.... ne.. to nemůžu dát jako nabídku.. ne..")
    wait(2)
    _bprint("Co to bude, hráči?")

    
    
    return listen2choices([
            "Bohatstvi",
            "[není zpřístupněná]Láska",
            "..."
            ], 2)

