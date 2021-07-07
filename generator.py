import json
import urllib.request

from config import *
from utils import *

with urllib.request.urlopen(PCL_EXPORT) as f:
    PCL = json.loads(f.read().decode('utf-8-sig'))
    currentYear = PCL["gameAttributes"]["season"]

ws = get_spreadsheet()

print("This is PCL's Wild Pokemon Generator.")
print("-------------------------------------")

while True:

        print("Options:")
        print("W - Press W to insert Wild Pokemon")
        print("S - Press S to insert Surprise Tool Pokemon")
        print("P - Press P to insert Professor Gift Pokemon")
        print("T - Press T to insert Spawn Tool Pokemon")
        print("-------------------------------------")
        option = input("Input the letter of choice: ").strip().upper()

        if (option == "W"):
            print("Getting Wild Pokemon...")
            wild_pokemon = ws.batch_get([WILD_POKEMON_RANGE], major_dimension='ROWS')
            print("Inputting wild pokemon into the export...")
            wildFill(wild_pokemon, currentYear, PCL)
            break
        elif (option == "S"):
            surprise_trade = ws.batch_get([SURPRISE_TRADE], major_dimension='ROWS')
            print("-------------------------------------")
            print("Teams:")
            for team in PCL["teams"]:
                print(f"{team['tid']} - {team['region']} {team['name']}")
            print("-------------------------------------")
            tid = input("What team is this pokemon on? Input tid: ")
            surpriseFill(surprise_trade, currentYear, PCL, tid)
            break
        elif (option == "P"):
            prof_gift = ws.batch_get([PROFESSOR_GIFT], major_dimension='ROWS')
            print("-------------------------------------")
            print("Teams:")
            for team in PCL["teams"]:
                print(f"{team['tid']} - {team['region']} {team['name']}")
            print("-------------------------------------")
            tid = input("What team is this pokemon on? Input tid: ")
            giftFill(prof_gift, currentYear, PCL, tid)
            break
        elif (option == "T"):
            print("Getting Spawn Tool Pokemon...")
            spawn_tool = ws.batch_get([SPAWN_TOOL], major_dimension='ROWS')
            print("Inputting Spawn Tool Pokemon into the export...")
            stFill(spawn_tool, currentYear, PCL)
            break

print("-------------------------------------")