#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>', strict_slashes=False)
def render_state_id(state_id=None):
    """display a HTML page"""
    states = storage.all("State")
    if state_id is not None:
        state_id = "State.{}".format(state_id)
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def testing(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
