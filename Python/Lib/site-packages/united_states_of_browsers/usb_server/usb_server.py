# -*- encoding: utf-8 -*-
import sqlite3

from pathlib import Path

import werkzeug

from flask import (Flask,
                   g,
                   render_template,
                   request,
                   )

from united_states_of_browsers.db_merge import db_search

app = Flask(__name__)
app.config.from_object(__name__)

def get_app_db_path():
    try:
        app_db_path = Path('~', '.USB', 'AppData', 'merged_db_path.txt').expanduser().read_text()
    except FileNotFoundError:
        app_db_path = Path('~', '.USB', 'usb_db.sqlite')
    return app_db_path

app.config.update(dict(
        DATABASE=get_app_db_path(),
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default',
        DEBUG=True,
        LOGGING_LOCATION=app.root_path+'error.log',
        ))
app.config.from_envvar('USB_SERVER_SETTINGS', silent=True)


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
        return g.sqlite_db


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def show_entries():
    db = get_db()
    search_results = db_search.search(db,'')
    return render_template('main.html', entries=search_results)


@app.route('/search', methods=['GET', 'POST'])
def search():
    db = get_db()
    try:
        search_results = db_search.search(db,
                                          request.args["query"],
                                          request.args["date-from"],
                                          request.args["date-to"]
                                          )
    except werkzeug.exceptions.BadRequestKeyError:
        search_results = db_search.search(db,
                                          request.form["query"],
                                          request.form["date-from"],
                                          request.form["date-to"]
                                          )

    return render_template('main.html', entries=search_results)
# return search_results

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def run_flask():
    app.run()


if __name__ == '__main__':
    run_flask()


