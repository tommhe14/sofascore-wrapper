from .api import SofascoreAPI

class Flag:
    def __init__(self, api: SofascoreAPI, flag_code: str):
        """
        Initializes the Flag class with the SofascoreAPI instance and flag code.

        Args:
            api (SofascoreAPI): An instance of the SofascoreAPI class.
            flag_code (str): The country code for the flag (e.g., "gb" for Great Britain).
        """
        self.api = api
        self.flag_code = flag_code.lower()

    async def image(self) -> str:
        """
        Retrieves the URL of the flag image for the specified country code.

        Returns:
            str: The URL of the flag image.

        Example Response:
            "https://www.sofascore.com/static/images/flags/gb.png"
        """
        return f"https://www.sofascore.com/static/images/flags/{self.flag_code}.png"