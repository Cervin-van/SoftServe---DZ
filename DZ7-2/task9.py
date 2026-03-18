def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0] == "R" or "r" else name + " does not play banjo"

print(are_you_playing_banjo("richard"))