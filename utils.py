import gspread
from config import *

def get_spreadsheet():
    gc = gspread.service_account(filename=SERVICE_ACCOUNT)
    works = gc.open(MASTER_SPREADSHEET).get_worksheet(4)
    wild_pokemon = works.batch_get([WILD_POKEMON_RANGE], major_dimension='ROWS')
    return wild_pokemon

def image(pokemon_attributes):
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

def name(pokemon_attributes):
    if (pokemon_attributes[9] == '*'):
        return f"{pokemon_attributes[5]} ✨"
    else:
        return pokemon_attributes[5]

def type(pokemon_attributes):
    if pokemon_attributes[3] == '':
        poke_type = pokemon_attributes[2]    
    else:
        poke_type = f"{pokemon_attributes[2]}/{pokemon_attributes[3]}"
    return poke_type