#Remove the time
#Write a function, shortenToDate, that takes the Website date/time in its original string format, and returns the shortened format.
#Assume shortenToDate's input will always be a string, e.g.
#  "Friday May 2, 7pm". Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".

def shorten_to_date(long_date):
    short = long_date.split()
    short.pop()
    new_date = ''
    for i in range(len(short)):
        new_date = new_date + ' ' + short[i]
        new_date.strip()

    return new_date
    

# def shorten_to_date(long_date):

#     return long_date[0 : long_date.index(',')]

# shorten_to_date = lambda d: d[:d.find(",")]


# def shorten_to_date(long_date):
#     return ' '.join(long_date.split()[:-1]).replace(',', '')


# def shorten_to_date(long_date):
#     x = long_date.split(',')
#     del x[-1]
#     return x[0]


# def shorten_to_date(long_date):
#     return long_date.split(',')[0]

# def shorten_to_date(long_date):
#     return long_date[0 : long_date.index(',')]


print(shorten_to_date("Monday February 2, 8pm"))