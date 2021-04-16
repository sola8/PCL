def clean(stats, c_type):
    for poke_type in stats[0]:
        if poke_type.endswith('/'):
            poke_type = poke_type.rstrip("/")
        c_type.append(poke_type)
    return c_type