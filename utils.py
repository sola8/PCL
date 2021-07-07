import json
import gspread
from config import *

def get_spreadsheet():
    gc = gspread.service_account(filename=SERVICE_ACCOUNT)
    ws = gc.open(MASTER_SPREADSHEET).get_worksheet(4)
    return ws

def findImage(pokemon_attributes):
    if (pokemon_attributes[1] == '*'):
        if (pokemon_attributes[29] == 'TRUE') or (pokemon_attributes[28] == 'TRUE'):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{(pokemon_attributes[9])}.png"
        elif (int(pokemon_attributes[9]) < 810):
            return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/shiny/{(pokemon_attributes[9])}.png"
        else:
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{(pokemon_attributes[9])}.png"
    elif (pokemon_attributes[1] == ' '): 
        if (pokemon_attributes[29] == 'TRUE') or (pokemon_attributes[28] == 'TRUE'):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{(pokemon_attributes[9])}.png"
        if (int(pokemon_attributes[9]) < 810):
            return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/images/{(pokemon_attributes[9])}.png"
        if (int(pokemon_attributes[9]) > 809) and (int(pokemon_attributes[9]) < 10000):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{(pokemon_attributes[9])}.png"
    else:
        return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/images/{(pokemon_attributes[9])}.png"

def findName(pokemon_attributes):
    if (pokemon_attributes[1] == '*'):
        return f"{pokemon_attributes[5]} ✨"
    else:
        return pokemon_attributes[5]

def findType(pokemon_attributes):
    if pokemon_attributes[3] == '':
        poke_type = pokemon_attributes[2]    
    else:
        poke_type = f"{pokemon_attributes[2]}/{pokemon_attributes[3]}"
    return poke_type

# Pokemon Fillers
def wildFill(wild_pokemon, year, export):
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
                    "year": (year - 1),
                    "pot": 0,
                    "ovr": 0,
                    "skills": []
                },
                "born": {
                    "year": year - int(pokemon_stats[12]),
                    "loc": findType(pokemon_stats)
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
                    "season": (year)
                    }
                ]
                })
            export['players'].append(shell)

    NEW_FILE = PATH_TO_NEW_EXPORT.replace(".json", "_created.json")

    with open(NEW_FILE, "w") as o:
        print("Creating export...")
        json.dump(export, o)
        print("Export done.")

def surpriseFill(surprise_trade, year, export, tid):
    for pokemon in surprise_trade:
        for pokemon_stats in pokemon:
            shell = ({
                
                "firstName": findName(pokemon_stats),
                "lastName": "",
                "college": "",
                "tid": int(tid),
                "imgURL": findImage(pokemon_stats),
                "hgt": int(pokemon_stats[10]),
                "weight": int(pokemon_stats[11]), 
                "draft": {
                    "round": 0,
                    "pick": 0,
                    "tid": -1,
                    "originalTid": -1,
                    "year": (year - 1),
                    "pot": 0,
                    "ovr": 0,
                    "skills": []
                },
                "born": {
                    "year": year - int(pokemon_stats[12]),
                    "loc": findType(pokemon_stats)
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
                    "season": (year)
                    }
                ]
                })
            export['players'].append(shell)
    NEW_FILE = PATH_TO_NEW_EXPORT.replace(".json", "_created.json")

    with open(NEW_FILE, "w") as o:
        print("Creating export...")
        json.dump(export, o)
        print("Export done.")

def stFill(spawn_tool, year, export):
    for pokemon in spawn_tool:
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
                    "year": (year - 1),
                    "pot": 0,
                    "ovr": 0,
                    "skills": []
                },
                "born": {
                    "year": year - int(pokemon_stats[12]),
                    "loc": findType(pokemon_stats)
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
                    "season": (year)
                    }
                ]
                })
            export['players'].append(shell)
    NEW_FILE = PATH_TO_NEW_EXPORT.replace(".json", "_created.json")

    with open(NEW_FILE, "w") as o:
        print("Creating export...")
        json.dump(export, o)
        print("Export done.")

def giftFill(professor_gift, year, export, tid):
    for pokemon in professor_gift:
        for pokemon_stats in pokemon:
            shell = ({
                
                "firstName": findName(pokemon_stats),
                "lastName": "",
                "college": "",
                "tid": int(tid),
                "imgURL": findImage(pokemon_stats),
                "hgt": int(pokemon_stats[10]),
                "weight": int(pokemon_stats[11]), 
                "draft": {
                    "round": 0,
                    "pick": 0,
                    "tid": -1,
                    "originalTid": -1,
                    "year": (year - 1),
                    "pot": 0,
                    "ovr": 0,
                    "skills": []
                },
                "born": {
                    "year": year - int(pokemon_stats[12]),
                    "loc": findType(pokemon_stats)
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
                    "season": (year)
                    }
                ]
                })
            export['players'].append(shell)
    NEW_FILE = PATH_TO_NEW_EXPORT.replace(".json", "_created.json")

    with open(NEW_FILE, "w") as o:
        print("Creating export...")
        json.dump(export, o)
        print("Export done.")