#Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {}!".format(name)


print(greet("Johnny"))
print(greet('Olha'))