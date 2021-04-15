import json

def fill(input, players, stats, season, c_type):
    i = 0               
    while i in range(input):
        shell = {
            
            "firstName": stats[2][i],
            "lastName": stats[1][i],
            "college": "",
            "tid": -1,
            "imgURL": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + stats[3][i] + ".png",
            "hgt": int(stats[4][i]),
            "weight": int(stats[5][i]), 
            "draft": {
                "round": 0,
                "pick": 0,
                "tid": -1,
                "originalTid": -1,
                "year": (season - 1),
                "pot": 0,
                "ovr": 0,
                "skills": []
            },
            "born": {
                "year": season - int(stats[6][i]),
                "loc": c_type[i]
                },
            "ratings": [
                { 
                "stre": int(stats[8][i]),
                "spd": int(stats[9][i]),
                "jmp": int(stats[10][i]),
                "endu": int(stats[11][i]),
                "ins": int(stats[12][i]),
                "dnk": int(stats[13][i]),
                "ft": int(stats[14][i]),
                "fg": int(stats[15][i]),
                "tp": int(stats[16][i]),
                "oiq": int(stats[17][i]),
                "diq": int(stats[18][i]),
                "drb": int(stats[19][i]),
                "pss": int(stats[20][i]),
                "reb": int(stats[21][i]), 
                "hgt": int(stats[7][i]),
                "season": (season)
                }
            ]
            },
        # json_gen = json.dumps(shell[0], indent=4) + ","
        players.append(shell[0])
        i += 1
