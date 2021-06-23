import json
import urllib.request

from config import *
from utils import *

with urllib.request.urlopen(PCL_EXPORT) as f:
    PCL = json.loads(f.read().decode('utf-8-sig'))

currentYear = PCL["gameAttributes"]["season"]

wild_pokemon = get_spreadsheet()

for pokemon in wild_pokemon:
    for pokemon_attributes in pokemon:
        shell = ({
            
            "firstName": name(pokemon_attributes),
            "lastName": f"({pokemon_attributes[4]})",
            "college": "",
            "tid": -1,
            "imgURL": image(pokemon_attributes),
            "hgt": int(pokemon_attributes[10]),
            "weight": int(pokemon_attributes[11]), 
            "draft": {
                "round": 0,
                "pick": 0,
                "tid": -1,
                "originalTid": -1,
                "year": (currentYear - 1),
                "pot": 0,
                "ovr": 0,
                "skills": []
            },
            "born": {
                "year": currentYear - int(pokemon_attributes[12]),
                "loc": type(pokemon_attributes)
            },
            "ratings": [
                { 
                "hgt": int(pokemon_attributes[13]),
                "stre": int(pokemon_attributes[14]),
                "spd": int(pokemon_attributes[15]),
                "jmp": int(pokemon_attributes[16]),
                "endu": int(pokemon_attributes[17]),
                "ins": int(pokemon_attributes[18]),
                "dnk": int(pokemon_attributes[19]),
                "ft": int(pokemon_attributes[20]),
                "fg": int(pokemon_attributes[21]),
                "tp": int(pokemon_attributes[22]),
                "oiq": int(pokemon_attributes[23]),
                "diq": int(pokemon_attributes[24]),
                "drb": int(pokemon_attributes[25]),
                "pss": int(pokemon_attributes[26]),
                "reb": int(pokemon_attributes[27]), 
                "season": (currentYear)
                }
            ]
            })
        PCL['players'].append(shell)

NEW_FILE = PATH_TO_NEW_EXPORT.replace(".json", "_created.json")

with open(NEW_FILE, "w"):
    print("Creating export...")
    json.dump(PCL, NEW_FILE)
    print("Export done.")