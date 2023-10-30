from domein import Domein, print_domeinen, write_domeinen

def management_loop(domeinen: [Domein]):
    keuze_lijst = ["add", "del", "list"]
    while True:
        actie = input("SYS: Geef een keuze: add, del, list, stop\nUSR> ").lower().strip()
        if actie.lower() == "stop":
            write_domeinen(domeinen)
            break
        elif actie.lower() not in keuze_lijst:
            print("keuze bestaat niet, probeer opnieuw")
            continue
        
        match actie:
            case "add":
                domein = input("SYS: Geef een domein naam\nUSR> ").lower().strip()
                domeinen.append(Domein(domein))
            case "del":
                domein = input("SYS: Geef een domein naam\nUSR> ").lower().strip()
                domeinen = [d for d in domeinen if d.domein_naam != domein]
            case "list":
                print_domeinen(domeinen)
        print()   