#print("Hello world from Jarvis\n")

#for countdown in 5, 4, 3, 2, 1, "hey!":
# print(countdown)

#spells = [
# "Riddikulus!",
# "Wingardium Leviosa!",
# "Avada Kedavra!",
# "Expecto Patronum!",
# "Nox!",
# "Lumos!",
# ]
#print(spells[5])

#quotes = {
# "Moe": "A wise guy, huh?",
# "Larry": "Ow!",
# "Curly": "Nyuk nyuk!",
# }
#stooge = "Curly"
#print(stooge, "says:", quotes[stooge])

import webbrowser
import json
from urllib.request import urlopen

print("Let's find an old website.")
site = input("Type a website URL: ") #lolcats.com
era = input("Type a year, month, and day, like 20150613: ") #20151022
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)