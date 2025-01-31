from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.search import Search
from sofascore_wrapper.match import Match
import asyncio
import json

async def match():
    api = SofascoreAPI()

    init_search = Search(api, search_string = "girona v arsenal")
    search_match = await init_search.search_match()
    print(json.dumps(search_match, indent = 4))

    selected_match = search_match["results"][0]

    match_id = selected_match["entity"]["id"]
    match_init = Match(api, match_id = match_id)

    match_stats = await match_init.stats()
    print(json.dumps(match_stats, indent = 4))

    match_commentary = await match_init.commentary()
    print(json.dumps(match_commentary, indent = 4))

    channels = await match_init.match_channels()
    print(json.dumps(channels, indent = 4))

    gb_channel = channels["countryChannels"]["GB"]
    channels = []
    for channel in gb_channel:
        channel_name = await match_init.get_channel(channel)
        channels.append(channel_name)

    print("GB Channels:\n" + "\n".join(channels))

    await api.close()
asyncio.run(match())