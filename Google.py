from googlesearch import search
import os
 
# to search
print('What we need to search?')
query = input()
print('Great question! However, can we have the name of the site? (Enter only name without https protocol and other stuff, for e.g. "4pda" not "https://4pda.to"')
site = input()

def searchfor():
    for j in search(query, tld="co.in", num=5000000, stop=None, pause=2):
        if site == 'None':
            f = open("Result.txt", "a")
            strings = j + '\n'
            f.write(strings)
            f.close()
        else:
            if site in j:
                f = open("Result.txt", "a")
                strings = j + '\n'
                f.write(strings)
                f.close()
            else:
                pass


if os.path.isfile('Result.txt'):
    os.remove('Result.txt')
    searchfor()
else:
    searchfor()
input("Press enter to exit ;)")
