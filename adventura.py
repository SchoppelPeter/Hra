import random
 
#kód z domu zkopírováno
def uvod():
    print("\nVítej v Summoner Riftu, Vyvolávači!")
    print("Tvým cílem je prozkoumat Jungle, kde se nachází monstra!")
    print("Začínáš s 5 životy. Pokud ztratíš všechny životy, zemřeš!")
    print("Campy, které je možné navštívit:")
    print("1. Temná skalka")
    print("2. Herald pit")
    print("3. Baron pit")
    print("4. Ukončit hru")
 
def skalka():
    print("\nVstoupil jsi do zóny, kde sídlí Gromp. Je tu ticho a slyšíš podivné zvuky.")
    volba = input("Najednou Gromp vyskočil ze skály! Co uděláš? (1 = Utéci, 2 = Bojovat): ")
    if volba == "1":
        print("Utíkáš, co ti síly stačí, a podaří se ti uniknout! Ale nic jsi nezískal.")
        return 0, 0
    elif volba == "2":
        if random.randint(1, 2) == 1:
            print("Podařilo se ti zabít Grompa, úžasná práce.")
            return 2, 0
        else:
            print("Gromp tě zabil, zkus to příště!")
            return 0, 1
    else:
        print("Neplatná volba, ztratil jsi se u temné skalky. Ztrácíš 1 život.")
        return 0, 1
 
def herald():
    print("\nVyrazil jsi na lov žlebového Heralda. Prázdnota je všude před tebou!")
    volba = input("Herald se vynoří z prázdnoty (1 = Utéci, 2 = Bojovat): ")
    if volba == "1":
        print("Skočíš přes zeď pomocí Talon E a unikneš!")
        return 0, 0
    elif volba == "2":
        if random.randint(1, 3) > 1:
            print("Porazil jsi Herlada, získáváš body a Oko věčné prázdnoty ke štěstí, jen tak dále!")
            return 3, 0
        else:
            print("Herlad ti zasadil tvrdý zásah, umřel jsi!")
            return 0, 2
    else:
        print("Neplatná volba, zmizel jsi v prázdnotě. Ztrácíš 1 život.")
        return 0, 1
 
def baron():
    print("\nDošel jsi k mocnému Baronovi.")
    volba = input("V žlebu se vynoří velký Baron. Co uděláš? (1 = Utéci, 2 = Bojovat): ")
    if volba == "1":
        print("Utíkáš pryč ze žlebu! Ale nic jsi nezískal.")
        return 0, 0
    elif volba == "2":
        if random.randint(1, 4) > 1:
            print("Porazil jsi Barona přímým úderem!")
            return 5, 0
        else:
            print("Baron tě roztrhal na kusy. Ztrácíš 3 životy.")
            return 0, 3
    else:
        print("Neplatná volba, očarováním jsi se propadl do prázdnoty. Ztrácíš 1 život.")
        return 0, 1
 
def hra():
    body = 0
    zivoty = 3
    uvod()
 
    while zivoty > 0:
        print(f"\nTvé body: {body} | Zbývající životy: {zivoty}")
        volba = input("Kam chceš jít? (1 = temná skalka, 2 = Herald pit, 3 = Baron pit, 4 = Ukončit hru): ")
        if volba == "1":
            b, z = skalka()
        elif volba == "2":
            b, z = herald()
        elif volba == "3":
            b, z = baron()
        elif volba == "4":
            print("Ukončil jsi hru.")
            break
        else:
            print("Neplatná volba, ztrácíš čas a nic nezískáváš.")
            b, z = 0, 0
 
        
        body += b
        zivoty -= z
 
        if zivoty <= 0:
            print("\nZtratil jsi všechny životy. Chceš pokračovat?")
            pokracovat = input("(1 = Ano, 2 = Ne): ")
            if pokracovat == "1":
                zivoty = 2  
                print("Vracíš se do hry s 2 životy.")
            else:
                print("Rozhodl ses ukončit hru.")
                break
 
    print(f"\nHra skončila. Nasbíral jsi celkem {body} bodů. Díky za hraní Summoner Riftu!")
 
# Spuštění hry
hra()
