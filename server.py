#!/usr/bin/env python
# encoding: utf=8

from flask import Flask
from flask import request
from flask import jsonify
from google import search as google_search

STORE_STRINGS = ['bandcamp', 'boomkat', 'bleep', 'itunes']
app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Takes a title and artist param, and searches for artist - title <store>
    '''
    artist = request.args.get('artist', '')
    title = request.args.get('title', '')
    urls = []
    for store_string in STORE_STRINGS:
        search_string = '%s - %s %s' % (artist, title, store_string)
        res = google_search(search_string)
        urls.append((store_string, res.next()))

    return jsonify(urls)

if __name__ == '__main__':
    app.run()
