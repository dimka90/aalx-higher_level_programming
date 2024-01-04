#!/usr/bin/python3
import json

with open('star_wars.json', 'r') as file:
     data = json.load(file)


with open('star_war.json', 'w') as file:
     json.dump(file, data, indent = 2)


