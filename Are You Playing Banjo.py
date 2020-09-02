def areYouPlayingBanjo(name):
    # Implement me!
    #for i in name:
    #name = str(name)
    if name[0] == 'R' or name[0] == 'r':
        return name + "plays banjo"
    else:
        return name + " does not play banjo"


print(areYouPlayingBanjo('olga'))