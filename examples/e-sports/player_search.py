from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.player import PlayerSearch
from sofascore_wrapper.search import Search
from sofascore_wrapper.match import Match
import asyncio
import json

async def player_search():
    api = SofascoreAPI()

    init_player = Search(api, search_string = "lewis hamilton")
    search_player = await init_player.search_all(sport = "motorsport")
    print(json.dumps(search_player, indent = 4))

    init_dedicated_search = PlayerSearch(api, query = "s1mple")
    search = await init_dedicated_search.search_player()
    print(json.dumps(search, indent = 4))

    await api.close()
asyncio.run(player_search())