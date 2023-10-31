from domein import Domein, print_domeinen, write_domeinen


def management_loop(domeinen: [Domein]):
    keuze_lijst = ["add", "del", "list"]
    while True:
        actie = clean_input("SYS: Geef een keuze: add, del, list, stop\nUSR> ")
        if actie.lower() == "stop":
            write_domeinen(domeinen)
            break
        elif actie.lower() not in keuze_lijst:
            print("keuze bestaat niet, probeer opnieuw")
            continue

        match actie:
            case "add":
                domein = clean_input("SYS: Geef een domein naam\nUSR> ")
                domeinen.append(Domein(domein))
            case "del":
                domein = clean_input("SYS: Geef een domein naam\nUSR> ")
                domeinen = [d for d in domeinen if d.domein_naam != domein]
            case "list":
                print_domeinen(domeinen)
        print()


def clean_input(q: str) -> str:
    return input(q).lower().strip()
