import requests
import json

apiKey = "your api key here"
key = "?access_token=" + apiKey
guildID = "your guild id here"
characterName = "your character name here"

class Wealth():
    money = requests.get("https://api.guildwars2.com/v2/account/wallet" + key)

    print(money.text)

    currency = json.loads(money.text)

    Coins = str(currency[0]["value"])
    Karma = str(currency[1]["value"])
    Other1 = str(currency[2]["value"])
    Other2 = str(currency[3]["value"])

    print("Karma: " + Karma)
    print("Coins: " + Coins)
    print("Other1: " + Other1)
    print("Other2: " + Other2)

class Character():
    char = requests.get("https://api.guildwars2.com/v2/characters/" + characterName + key)

    print(char.text)

    charData = json.loads(char.text)

    charLvl = str(charData["level"])
    charName = str(charData["name"])
    charRace = str(charData["race"])
    charGender = str(charData["gender"])
    charFlags = str(charData["flags"])
    charGuild = str(charData["guild"])
    charAge = str(charData["age"])
    charCreation = str(charData["created"])
    charDeaths = str(charData["deaths"])
    charProfession = str(charData["profession"])

    print(charProfession)

class Guild():
    guildMem = requests.get("https://api.guildwars2.com/v2/guild/" + guildID +"/members" + key)
    guildTeams = requests.get("https://api.guildwars2.com/v2/guild/" + guildID +"/teams" + key)
    guild = requests.get("https://api.guildwars2.com/v2/guild/" + guildID + key)

    guildMemName = ""
    guildMemRank = ""

    print(guildMem.text)

    GuildData = json.loads(guild.text)
    GuildMemData = json.loads(guildMem.text)
    GuildTeamData = json.loads(guildTeams.text)

    guildTeamNames = GuildTeamData

    guildName = GuildData["name"]
    guildLvl = GuildData["level"]
    guildInfluence = GuildData["influence"]
    guildAetherium = GuildData["aetherium"]
    guildResonance = GuildData["resonance"]
    guildFavor = GuildData["favor"]
    guildMemCount = GuildData["member_count"]
    guildMemCap = GuildData["member_capacity"]
    guildTag = GuildData["tag"]

    for name in GuildMemData:
        # Print the "name" value of the first element in the returned JSON.
        print("Name: " + name["name"])
        print("Rank: " + name["rank"])
        print("------------------")
        guildMemName = name["name"]
        guildMemRank = name["rank"]