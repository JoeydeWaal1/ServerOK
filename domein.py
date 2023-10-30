import json

class Domein:
    def __init__(self, domein_naam, online=False):
        self.domein_naam = domein_naam
        self.online = online
    def __str__(self) -> str:
        return f"\"domein_naam\": \"{self.domein_naam}\",\t\"online\":{self.online}"

class DomeinEncoder(json.JSONEncoder):
    def default(self, domein):
            return domein.__dict__

def print_domeinen(domeinen: [Domein]):
    if len(domeinen) == 0:
        print("Nog geen domeinen")
    for d in domeinen:
        print(str(d))

def write_domeinen(domeinen: [Domein]):
    json_str = json.dumps(domeinen, indent=4, cls=DomeinEncoder)
    with open("servers.json", "w") as f:
        f.write(json_str)

def read_domeinen() -> [Domein]:
    domeinen = []
    try:
        with open("servers.json") as f:
            data = json.load(f)
            for d in data:
                domeinen.append(Domein(d["domein_naam"], d["online"]))
    except:
        return []
    return domeinen