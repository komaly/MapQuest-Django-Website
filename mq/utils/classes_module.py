'''This file contains multiple classes. Each class searches and retrieves specific 
information from the parsed json output'''

import json

class Steps:
    def generate(self, json: 'json'):
        '''Searches json and prints step by step directions for the route to the location(s)'''
        routed = []
        print('\nSTEPS')
        for item in json:
          for element in item["route"]["legs"]:
            for subitem in element["maneuvers"]:
                if subitem["narrative"] not in routed:
                    routed.append(subitem["narrative"])
        return routed

class TotalDistance:
    def generate(self, json:'json'):
        '''Searches json and prints the total distance travelled'''
        distance = 0
        for element in json:
            distance += element["route"]["distance"]
        return round(distance)

class TotalTime:
    def generate(self, json:'json'):
        '''Searches json and calculates and prints the times it takes to travel the route'''
        time = 0
        for element in json:
            time += element["route"]["time"]/60
            
        return round(time)

class LatLong:
    def generate(self, json:'json'):
        '''Searches json and prints the latitude/longtitude for each location'''
        lat_long = []
        for element in json:
          json_text = element["route"]["locations"]
          for item in json_text:
              if "displayLatLng" in item:
                  lat = item["displayLatLng"]["lat"]
                  lon = item["displayLatLng"]["lng"]
                  if lat >=0:
                      if lon >=0:
                          lat_long.append(str(abs(round(lat, 2))) + " N " + str(abs(round(lon, 2))) + " E")
                      elif lon < 0:
                          lat_long.append(str(abs(round(lat, 2)))+ " N " + str(abs(round(lon, 2)))+ " W")
                  else:
                      if lon >= 0:
                          lat_long.append(str(abs(round(lat, 2))) + " S " + str(abs(round(lon, 2))) + " E")
                      elif lon < 0:
                          lat_long.append(str(abs(round(lat, 2))) + " S " + str(abs(round(lon, 2))) + " W")
        
        return list(set(lat_long))
            
        
            

