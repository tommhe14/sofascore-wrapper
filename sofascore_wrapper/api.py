import aiohttp

BASE_URL = "https://www.sofascore.com/api/v1"

class SofascoreAPI:
    def __init__(self, headers: dict = None):
        default_headers = {"User-Agent": "Mozilla/5.0"}
        self.session = None
        self.headers = default_headers or headers


    async def _get(self, endpoint):
        if self.session is None:
            self.session = aiohttp.ClientSession(headers = self.headers)
        async with self.session.get(f"{BASE_URL}{endpoint}") as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Failed to fetch {endpoint}: {response.status}")

    async def close(self):
        if self.session:
            await self.session.close()
