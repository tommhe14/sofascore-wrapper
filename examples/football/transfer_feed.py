from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.player import PlayerSearch
from sofascore_wrapper.transfers import Transfers
import asyncio
import json

async def player_transfers():
    api = SofascoreAPI()

    init_feed= Transfers(api)
    transfer_feed = await init_feed.get_transfer_feed(sort_by = "followers", unique_tournament_id = 17)  
    print(json.dumps(transfer_feed["transfers"][:10], indent = 4))

    await api.close()
asyncio.run(player_transfers())