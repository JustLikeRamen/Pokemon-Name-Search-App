"""

A Pokemon Name Search Application run on Flask!

"""

import flask
from flask.views import MethodView
from pokeSearch import PokeSearch

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=PokeSearch.as_view('pokeSearch'),
                 methods=["GET" , "POST"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
