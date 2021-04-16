from poke_gen import fill_shell, get_spreadsheet, remove_slash, stat_grab
import json

# gspread set-up
wild_poke = get_spreadsheet.get_spreadsheet()

stats = [[] for i in range(22)]
c_type = []
players = []

while True:
    try:
        num_of_pokemon = int(input("Input the number of Pokémon you want to create: "))
        season = int(input("Input the current season: "))
        break
    except ValueError:
        print("This wasn't a valid integer.")

# Allot the spreadsheet stats onto arrays
stat_grab.grab(stats, wild_poke)    

# Clean the extra forward slashes on single-typed Pokémon
remove_slash.clean(stats, c_type)

# Fill the JSON shell with all of the stripped data
fill_shell.fill(num_of_pokemon, players, stats, season, c_type)

# output file - used to copy into cleaned league file    
with open('output.json', "w", encoding='utf-8-sig') as o:
    json.dump(players, o, indent=4)