def grab(stats, wild_poke):
    for poke in wild_poke:
        for t in poke:
            stats[0].append(t[0]+"/"+t[1]) # Figure out a way to remove the '/' if
                                         # pokemon has single-typing
            stats[1].append("("+t[2]+")")
            stats[2].append(t[3])
            stats[3].append((t[6]))
            stats[4].append(t[7])
            stats[5].append(t[8])
            stats[6].append(t[9])
            stats[7].append(t[10])    
            stats[8].append(t[11])    
            stats[9].append(t[12])    
            stats[10].append(t[13])   
            stats[11].append(t[14])    
            stats[12].append(t[15])    
            stats[13].append(t[16])
            stats[14].append(t[17])
            stats[15].append(t[18])
            stats[16].append(t[19])
            stats[17].append(t[20])
            stats[18].append(t[21])
            stats[19].append(t[22])
            stats[20].append(t[23])
            stats[21].append(t[24])
    return stats