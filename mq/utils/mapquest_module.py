'''This file interacts with the MapQuest Open Directions API. This
 is where the URL is built, the HTTP request is made,and the JSON response
 is parsed.'''

import json
import urllib.parse
import urllib.request

MAPQUEST_APP_KEY = 'Fmjtd%7Cluu8216z2q%2C70%3Do5-942xl6'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'

'''Builds and returns the URL based on the locations given by the user (start and end params)'''
def build_url(start: str, end: 'list of str') -> str:
    query_parameters = [('key', MAPQUEST_APP_KEY), ('from', start),
                        ('to', end)]
    
    encoded_parameters = urllib.parse.urlencode(query_parameters)
    
    return BASE_MAPQUEST_URL + '/route?'\
           + urllib.parse.unquote(encoded_parameters)

'''Takes the URL parameter and returns a parsed JSON response '''
def get_result(url: str) -> 'json':
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()
