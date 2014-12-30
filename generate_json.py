#!/usr/bin/python

import csv
from jinja2 import Environment, PackageLoader

file = 'eat-notation-office.csv'

env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('map-template.json')

reader = csv.DictReader(open(file), delimiter='|')

result = {}
restaurants  = []
for row in reader:
    restaurants.append(row)
 
print template.render(restaurants=restaurants)
