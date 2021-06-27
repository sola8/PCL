import json
import urllib.request

from config import *
from utils import *

with urllib.request.urlopen(PCL_EXPORT) as f:
    PCL = json.loads(f.read().decode('utf-8-sig'))

currentYear = PCL["gameAttributes"]["season"]

wild_pokemon = get_spreadsheet()

for pokemon in wild_pokemon:
    for pokemon_stats in pokemon:
        shell = ({
            
            "firstName": findName(pokemon_stats),
            "lastName": f"({pokemon_stats[4]})",
            "college": "",
            "tid": -1,
            "imgURL": findImage(pokemon_stats),
            "hgt": int(pokemon_stats[10]),
            "weight": int(pokemon_stats[11]), 
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
                "year": currentYear - int(pokemon_stats[12]),
                "loc": type(pokemon_stats)
            },
            "ratings": [
                { 
                "hgt": int(pokemon_stats[13]),
                "stre": int(pokemon_stats[14]),
                "spd": int(pokemon_stats[15]),
                "jmp": int(pokemon_stats[16]),
                "endu": int(pokemon_stats[17]),
                "ins": int(pokemon_stats[18]),
                "dnk": int(pokemon_stats[19]),
                "ft": int(pokemon_stats[20]),
                "fg": int(pokemon_stats[21]),
                "tp": int(pokemon_stats[22]),
                "oiq": int(pokemon_stats[23]),
                "diq": int(pokemon_stats[24]),
                "drb": int(pokemon_stats[25]),
                "pss": int(pokemon_stats[26]),
                "reb": int(pokemon_stats[27]), 
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