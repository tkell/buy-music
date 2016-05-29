#!/usr/bin/env python
# encoding: utf=8

from flask import Flask
from flask.ext.cors import CORS
from flask import request
from flask import jsonify
from google import search as google_search

app = Flask(__name__)
CORS(app)

@app.route('/search')
def search():
    '''
    Takes a track title and artist param, and returns the URLs for the track
    '''
    artist = request.args.get('artist', '')
    title = request.args.get('title', '')
    urls = _search_by_artist_and_title(artist, title)

    return jsonify(urls)

@app.route('/search-by-playlist')
def search_by_playlist():
    '''
    Takes a Spotify playlist URI, and searches for each track
    '''
    playlist_uri= request.args.get('playlist_uri', '')
    urls = _search_by_playlist(playlist_uri_

    return jsonify(urls)

def _search_by_playlist(playlist_uri):
    '''
    Gets the artist and title of each track from Spotify, and goes from there.
    '''
    # get each track
    # get each set of URLS
    # return a list of list

    return urls

def _search_by_artist_and_title(artist, title):
    '''
    Searches for artist - title <store>
    '''
    urls = []
    store_strings = ['bandcamp', 'boomkat', 'bleep', 'itunes']
    for store_string in store_strings:
        search_string = '%s - %s %s' % (artist, title, store_string)
        res = google_search(search_string)
        urls.append((store_string, res.next()))

    return urls

if __name__ == '__main__':
    app.run()
