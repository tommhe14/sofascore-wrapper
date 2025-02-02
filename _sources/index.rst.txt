.. sofascore-wrapper documentation master file, created by
   sphinx-quickstart on Tue Jan 30 2025.

Welcome to sofascore-wrapper's documentation!
============================================

This is the Python API wrapper for the Sofascore undocumented API.
It allows you to fetch and interact with data from Sofascore, including information about matches, players, teams, and more.

Contents:
---------
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api_reference

   modules

Installation
============
To install the package, use pip:

.. code-block:: bash

   pip install sofascore-wrapper

Usage
=====
Here's a simple example of how to use the wrapper to search for a player:

.. code-block:: python

   import asyncio
   from sofascore_wrapper.api import SofascoreAPI
   from sofascore_wrapper.search import Search

   async def main():
      api = SofascoreAPI()  # Initialize the API client

      # Create an instance of the Search class
      search = Search(api, search_string="saka")

      # Perform the search and print the result
      player = await search.search_all()
      print(player)

      # Close the API client
      await api.close()

   if __name__ == "__main__":
      asyncio.run(main())

In this example, we initialize the `SofascoreAPI`, create a `Search` instance with the search string `"saka"`, and call `search_all()` to fetch the player data. The result is printed to the console.

From the Developer:
=============

While sofascore-wrapper lets you search for via sports, THERE IS ONLY SUPPORT FOR FOOTBALL (SOCCER). If you would like further sports added open up an issue and request for what specific things you're looking for with the front end example.


API Reference
=============
The following sections provide detailed information on the available methods and classes in the `sofascore-wrapper` API.