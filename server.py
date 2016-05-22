#!/usr/bin/env python
# encoding: utf=8

from google import search

store_strings = ['bandcamp', 'boomkat', 'bleep', 'itunes']
artist = 'Archie Pelago'
title = 'Clammy Customer'

urls = []
for store_string in store_strings:
    search_string = '%s %s %s' % (artist, title, store_string)
    res = search(search_string)
    urls.append((store_string, res.next()))

