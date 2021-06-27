import gspread
from config import *

def get_spreadsheet():
    gc = gspread.service_account(filename=SERVICE_ACCOUNT)
    works = gc.open(MASTER_SPREADSHEET).get_worksheet(4)
    wild_pokemon = works.batch_get([WILD_POKEMON_RANGE], major_dimension='ROWS')
    return wild_pokemon

def findImage(pokemon_attributes):
    if (pokemon_attributes[1] == '*'):
        if (pokemon_attributes[29] is True):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_attributes[9]}.png"
        elif (pokemon_attributes[9] < 810):
            return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/shiny/{pokemon_attributes[9]}.png"
        else:
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_attributes[9]}.png"
    elif (pokemon_attributes[1] == ''): 
        if (pokemon_attributes[29] is True):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_attributes[9]}.png"
        if (pokemon_attributes[9] < 810):
            return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/images/{pokemon_attributes[9]}.png"
        if (pokemon_attributes[9] > 809) and (pokemon_attributes[9] < 10000):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_attributes[9]}.png"
    else:
        return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/images/{pokemon_attributes[9]}.png"

def findAltImage(pokemon_attributes):
    if (pokemon_attributes[1] == '*'):
        if (pokemon_attributes[29] is True):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_attributes[9]}.png"
        elif (pokemon_attributes[9] < 810):
            return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/shiny/{pokemon_attributes[9]}.png"
        else:
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_attributes[9]}.png"
    elif (pokemon_attributes[1] == ''): 
        if (pokemon_attributes[29] is True):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_attributes[9]}.png"
        if (pokemon_attributes[9] < 810):
            return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/images/{pokemon_attributes[9]}.png"
        if (pokemon_attributes[9] > 809) and (pokemon_attributes[9] < 10000):
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_attributes[9]}.png"
    else:
        return f"https://raw.githubusercontent.com/poketwo/data/05498eef9ee224157d24c6eb3bf1237ab59f1ab9/images/{pokemon_attributes[9]}.png"

def findName(pokemon_attributes):
    if (pokemon_attributes[9] == '*'):
        return f"{pokemon_attributes[5]} ✨"
    else:
        return pokemon_attributes[5]

def findAltName(pokemon_attributes):
    if (pokemon_attributes[1] == '*'):
        return f"{pokemon_attributes[2]} ✨"
    else:
        return pokemon_attributes[2]

def findType(pokemon_attributes):
    if pokemon_attributes[3] == '':
        poke_type = pokemon_attributes[2]    
    else:
        poke_type = f"{pokemon_attributes[2]}/{pokemon_attributes[3]}"
    return poke_type

def findAltType(pokemon_attributes):
    if pokemon_attributes[5] == '':
        poke_type = pokemon_attributes[4]    
    else:
        poke_type = f"{pokemon_attributes[4]}/{pokemon_attributes[5]}"
    return poke_type

def surpriseFill(surprise_pokemon, export, year):
    for pokemon in surprise_pokemon:
        for pokemon_stats in pokemon:
            for value in pokemon_stats:
                shell = ({
                    "firstName": findName(value),
                    "lastName": f"({value[4]})",
                    "college": "",
                    "tid": -1,
                    "imgURL": findImage(value),
                    "hgt": int(value[10]),
                    "weight": int(value[11]), 
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
                        "year": year - int(value[12]),
                        "loc": type(value)
                    },
                    "ratings": [
                        { 
                        "hgt": int(value[13]),
                        "stre": int(value[14]),
                        "spd": int(value[15]),
                        "jmp": int(value[16]),
                        "endu": int(value[17]),
                        "ins": int(value[18]),
                        "dnk": int(value[19]),
                        "ft": int(value[20]),
                        "fg": int(value[21]),
                        "tp": int(value[22]),
                        "oiq": int(value[23]),
                        "diq": int(value[24]),
                        "drb": int(value[25]),
                        "pss": int(value[26]),
                        "reb": int(value[27]), 
                        "season": (year)
                        }
                    ]
                    })
                export['players'].append(shell)

def wildFill(wild_pokemon, export, year):
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
                    "season": (year)
                    }
                ]
                })
            export['players'].append(shell)

def stFill():
    return

def giftFill():
    return