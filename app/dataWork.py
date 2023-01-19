import gbmodel
import requests

# The core of our back-end, does all the API calls and filtering of data.
class APIWork():

    def __init__(self):
        """
        Initializes the model that we'd like to prep for the data.
        """
        self.model = gbmodel.get_model()

    def getPokemonData(self, pokemonName):
        """
        Sends a request to the PokeAPI for a specific pokemon.
        """
        # Lower-case and replace any spaces with dashes because the URL hates it otherwise...
        pokemonName = pokemonName.replace(' ', '-').replace('.', '').replace('\'', '').lower()

        # Make a GET request to the API so we can recieve this data.
        url = 'https://pokeapi.co/api/v2/pokemon/' + pokemonName
        try:
            response = requests.get(url).json()
        except requests.exceptions.JSONDecodeError:
            return []

        # Filter this data.
        return self.filterPokeData(response)

    def filterPokeData(self, pokeData: dict) -> list:
        """
        Runs through the raw JSON retrieved from the API, extracting
        the data we're looking for and storing it as a list for a
        return value to the webpage.
        """
        cleanPokeData = []

        # Get the pokedex entry, name, ability, alt forms, sprite, and types.
        cleanPokeData.append(pokeData["id"])
        cleanPokeData.append(pokeData["name"].replace('-', ' ').title())
        cleanPokeData.append(pokeData["abilities"][0]["ability"]["name"].replace('-', ' ').title())
        cleanPokeData.append(pokeData["forms"][0]["name"].title())
        cleanPokeData.append(pokeData["sprites"]["front_default"])
        cleanPokeData.append(pokeData["types"][0]["type"]["name"].title())

        if len(pokeData["types"]) > 1:
            cleanPokeData[-1] = cleanPokeData[-1] + '/' + pokeData["types"][1]["type"]["name"].title()

        # Return this cleaned-up data.
        return cleanPokeData
