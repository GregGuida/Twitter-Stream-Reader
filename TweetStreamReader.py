#!/usr/bin/python

import requests
import json

requestobject = requests.post('https://stream.twitter.com/1/statuses/sample.json',
        auth=(argsv[1],argsv[2]))

for line in requestobject.iter_lines():
    if line:
        tweet = json.loads(line)
        if 'text' in tweet:
            print tweet['text']
