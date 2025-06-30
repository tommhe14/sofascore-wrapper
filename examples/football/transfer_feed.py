import asyncio
from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.player import Player
from sofascore_wrapper.transfers import Transfers
import json
import datetime
import random

leagues = {
        "Womens Super League":1044,
        "Liga F":1127,
        "Première Ligue, Féminine":1139,
        "Frauen-Bundesliga":232,
        "Serie A Women":10640,
        "NWSL":1690
    }

# feed for just womens football
async def example_transfer_feed(league_id: int):
    api = SofascoreAPI()  

    id_to_league = {v: k for k, v in leagues.items()}

    transfer = Transfers(api)
    t = await transfer.get_transfer_feed(unique_tournament_id=league_id)
    
    data = []
    for player in t["transfers"]:
        name = player["player"]["name"]
        id = player["player"]["id"]
        fromClub = player["transferFrom"]["name"]
        toClub = player["transferTo"]["name"]
        fee = player["transferFeeDescription"]
        dateTransfer = datetime.datetime.fromtimestamp(player["transferDateTimestamp"])

        if not dateTransfer.date() == datetime.datetime.now().date():
            continue

        player1 = Player(api, player_id=id)
        image = await player1.image()
        
        dataDict = {
            "playerName": name,
            "playerId": id,
            "playerImage": image,
            "fromClub": fromClub,
            "toClub": toClub,
            "Fee": fee,
            "Date": dateTransfer.isoformat(),
            "DateTimestamp": player["transferDateTimestamp"],
            "requestLeague": {
                "leagueName": id_to_league.get(league_id),
                "leagueImage": f"https://img.sofascore.com/api/v1/unique-tournament/{league_id}/image/dark"
            }
        }
        data.append(dataDict)
    
    print(json.dumps(data, indent=4, ensure_ascii=False))
    await api.close()

if __name__ == "__main__":
    asyncio.run(example_transfer_feed(random.choice(list(leagues.values()))))