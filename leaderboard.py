import json


print "parsing leaderboard"

won = []
loss = []

with open("leaderboard.json") as jdata:
    ldata = json.load(jdata)
    print ldata
    for x in ldata:
        obj = {}
        obj["name"] = x["name"]
        obj["wins"] = x["gamesWon"]
        won.append(obj)
        obj = {}
        obj["name"] = x["name"]
        obj["losses"] = x["gamesLost"]
        loss.append(obj)
        print("name: " , x["name"])
        print("wins: " , x["gamesWon"])
        print("losses: " , x["gamesLost"])

print won
print loss

won.sort(key=lambda x: x["wins"], reverse=True)
print won

loss.sort(key=lambda x: x["losses"], reverse=True)
print loss

winners = []
losers = []

for x in won:
    winners.append(x["name"])

for x in loss:
    losers.append(x["name"])

print winners
print losers

print "done"