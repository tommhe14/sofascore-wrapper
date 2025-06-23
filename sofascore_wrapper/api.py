from playwright.async_api import async_playwright

BASE_URL = "https://www.sofascore.com/api/v1"

class SofascoreAPI:
    def __init__(self):
        self.browser = None
        self.page = None
        self.playwright = None

    async def _init_browser(self):
        if self.playwright is None:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=True)
            self.page = await self.browser.new_page()

    async def _get(self, endpoint):
        await self._init_browser()
        url = f"{BASE_URL}{endpoint}"
        response = await self.page.goto(url)
        if response.status == 200:
            return await response.json()
        else:
            raise Exception(f"Failed to fetch {endpoint}: {response.status}")

    async def _raw_get(self, url):
        await self._init_browser()
        response = await self.page.goto(url)
        if response.status == 200:
            return await response.json()
        else:
            raise Exception(f"Failed to fetch {url}: {response.status}")

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
