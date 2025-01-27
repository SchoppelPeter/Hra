import sys
import game_story as gs
import time as t
import random as r

cesta = gs._UVOD()




if cesta == 1:
    
    gs._bprint(".............")
    gs._bprint(".............")

    gs._bprint("Cesta pro bohatství není jen tak..")
    gs.wait(2)
    gs._bprint("Ale vypadáš relativně schopně.. tak proč to nezkusit...")
    gs.wait(2)
    gs._bprint("OH MUJ BOZE!! TO JE DRAK VSECHNOPENEZOMLS!!!")
    gs.wait(1.9)
    gs._bprint("Delam si srandu... Ale ceka nas první rozcestí..")
    gs.wait(1)
    gs._bprint("Pozor však dej, obě rozhodnutí nesou RIZIKO.")
    gs.wait(2.6)
    path = gs.listen2choices([
        "Jít do lesa za klauny s mačety, ale treba to jsou jen hracky...",
        "Jít do hradu, kde princezna je seriovy vrah, ale muze to byt jen pomluva..."
    ])
     
    gs._bprint("....")
    gs.wait(2.6)
    gs._bprint("....")
    gs.wait(3.4)


    if path==1: #klauni
        gs._bprint("Tak snad to bude dobrý... jdeme teda, modleme se...")
        gs.wait(2.53)
        if r.randint(1,3) == 1: #killers
            gs._bprint("Haha.. to je vtipný... ono to co drží nevypadá moc jako hračka...")
            gs.wait(2.6)
            gs._bprint("JAKO NEVIM ALE MĚLI BYCHOM RADŠI UTÍKAT!!!!!")
            gs.wait(2)
            gs._bprint("NASEL JSI ZBRAN!! HNED JI VEM")
            zbran = gs.listen2choices([
                "Vzít",
                "Nemám pud přežití, tak proč to nenechat ležet?"
            ])
            end = False
            if zbran == 1:
                gs._bprint("UTOOOK!!")
                gs.wait(3)
                gs._bprint("Porazil si je... WOW.")
                gs.wait(1.6)
                gs._bprint("Tady mas 10 rubynu.. Jo, tady to taky existuje. Mozna ti to pomuzu dál  pribehu...")
                gs.wait(2)
            elif zbran == 2:
                end = True
                gs._bprint("?!?!?! COOOOOOOO!!!")
                gs.wait(2.6)
                gs._bprint("TAK TEDA UTIKEJ, ZDA TI JE ZIVOT MILY, PAC TE TAKY ASI ZABIJU!!!!!")
                gs.wait(1.8)
                gs._bprint("..")
                gs.wait(1.8)
                gs._bprint("..")
                gs.wait(2.6)
                gs._bprint("Byl jsi zabit... avšak né klaunama...")

                gs._bprint("_______GAME OVER_______")
                sys.exit("game's over, DUH!")
            if not end:
                gs._bprint("Prohledejme ty klauny, jen tak..")
                gs.wait(2)
                gs._bprint("Paráda, měli u sebe pistoli...")
                gs.wait(1.8)
                gs._bprint("*strel*")
                gs.wait(1.3)
                gs._bprint("Aha.. tak voda... no tak nic. I tak si to nechme.")
                gun=True
                gs.wait(2)
        else:
            gs._bprint("Aha.. nastesti to byli jen hračky, asi jdou.. nevim kam a proc.")
            gs.wait(2)
        
        gs._bprint("Kazdopadne jdeme dal...")
        gs.wait(1.8)
        gs._bprint("*nahodou se zjevi plamínek Firey - má na srdce miliony zivotu, jeho velikost klame*")
        gs.wait(3)
        gs._bprint("FIREY!! sakra ne. NEEEE!! tak to je asi náš konec!!!")
        gs.wait(2.4)
        gs._bprint("[FIREY]: Mhmmm too tedy jeee vašov konec tady, klan se a milost ti moznee dám.")
        gs.wait(1.9)
        opt = gs.listen2choices([
            "Klanit se.",
            "Použít pistolku!!! ~nese riziko~"
        ])

        if opt == 1:
            gs._bprint("..")
            gs.wait(1.9)
            gs._bprint("[FIREY]: Dobree jsi udelal poskok moj.")
            gs.wait(2)
            gs._bprint("?!?!?! MY???")
            gs.wait(1.6)
            gs._bprint("[FIREY]: Ne...")
            gs.wait(2)
            gs._bprint("[FIREY]: jen ti dva pred mnouuu co vypadaju ako ultimatni zebrooci")
            gs.wait(1.5)
            gs._bprint("[FIRED]: tak uz sebo hybnete vy obri, pojdete za mno do hraduj")
            gs.wait(3)
            gs._bprint("_______GAME OVER_______")
            sys.exit("")
        else:
            gs._bprint("..")
            gs.wait(1.9)
            gs._bprint("*Pistoka selže*")
            gs.wait(2)
            gs._bprint("[FIREY]: Joo aha. Tak tyy takhlo!!!!!")
            gs.wait(2)
            gs._bprint("**FIREY te necha sežehnout silou atomové bomby**")
            sys.exit()

    else:
        gs._bprint("[PRINCEZNA]: Jeee ahoj!! Vitam Vas odvážlivci!!")
        gs.wait(2)
        gs._bprint("[PRINCEZNA]: Je to taaaaak dlouho co jsem tady potkala někoho živého... hahahah!!")
        gs.wait(2.86)
        gs._bprint("*princeznin smích ti přijde znepokojivý*")
        gs.wait(1.8)
        gs._bprint("[PRINCEZNA]: Nedáte si se mnou čaj? :-)")
        gs.wait(2.1)
        princess_opt = gs.listen2choices([
            "Proč ne!"#,
           # "Ne",
           # "Utíct z hradu"
        ])
        if princess_opt==1:
            gs._bprint("[PRINCEZNA]: No skvěle! Tak pojdte do mého největšího pokoje..")
            gs.wait(2.3)
            gs._bprint("*vejdeš do pokoje a vydíš samé kostry*")
            gs.wait(1.6)
            gs._bprint("[PRINCEZNA]: Toho si prosím nevšimejte.. Kamarádi se nechteli kamarádit..")
            gs.wait(2.4)
            gs._bprint("[PRINCEZNA]: Tak si sednete.. a počkejte na mě. Hned přijdu s čajem! :DD")
            gs.wait(1.8)
            gs._bprint("..")
            gs.wait(1.9)
            gs._bprint(".. *dvere se zamknou* ..")
            gs.wait(1.9)
            gs._bprint("No, tak to ne. NE. Místo čaje jed!")
            tea = gs.listen2choices([
                "Skočit z okna"
            ])
            if tea==1:
                gs._bprint("*skok*")
                gs.wait(2)
                gs._bprint("*vydíš princeznu jak stojí s úsměvem tam, kde máš dopadnout*")
                gs.wait(2)
                gs._bprint("WTF??")
                gs.wait(1.3)
                gs._bprint("NEEEEEEEEEEE!!!!")
                gs.wait(1.8)
                gs._bprint("*princezna tě chytne, ale ne proto abys přežil...*")
                gs.wait(2)
                gs._bprint("Pokračování příšte...")
                sys.exit("")

    print("s")
elif cesta == 2:
    print("b")
else:
    gs._bprint("TAHLE CESTA NEJDE!!! NEEEEEEEEE!!!!!!!")
    gs.wait(2)
    sys.exit("Vyprávěč tě zabil z neznámého důvodu...")