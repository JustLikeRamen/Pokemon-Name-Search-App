from dataWork import APIWork
from flask import request, render_template
from flask.views import MethodView

class PokeSearch(MethodView):
    def __init__(self):
        """
        Connect up the class we've created for managing API data to this file.
        """
        self.dataWork = APIWork()

    def get(self):
        """
        Accepts GET requests, and loads our initial webpage where there's no data.
        """
        return render_template('index.html', dexEntry="", name="", ability="", forms="", sprite="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/HD_transparent_picture.png/640px-HD_transparent_picture.png", types="")

    def post(self):
        """
        Accepts POST requests, processes the user's input, and then automatically
        refreshes the page, filling the empty information with the pokemon's data
        if appropriate. If there is no existing pokemon with that name, missingNo
        is displayed.
        """
        # Get the user's requested pokemon.
        pokemonName = request.form['search']

        # Get the pokemon's information.
        pokemon = self.dataWork.getPokemonData(pokemonName)
        if pokemon == []:
            return render_template('index.html', dexEntry=" 000", name=" missingNo", ability="Glitch", forms=" N/A", sprite="https://static.wikia.nocookie.net/character-stats-and-profiles/images/6/6c/MissingNo_Ghost.png", types=" Bird/Normal")

        # Return this new information with a new webpage.
        return render_template('index.html', dexEntry=pokemon[0], name=pokemon[1], ability=pokemon[2], forms=pokemon[3], sprite=pokemon[4], types=pokemon[5])
