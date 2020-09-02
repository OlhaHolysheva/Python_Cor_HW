def enough(cap, on, wait):
    if cap >= on + wait:
        return 0
    else:
        return (on+wait) - cap


print(enough(40,30,15))