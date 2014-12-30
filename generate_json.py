#!/usr/bin/python

import csv
import sys
from jinja2 import Environment, PackageLoader

def get_template(default='map-template.json'):
    env = Environment(loader=PackageLoader('app', 'templates'))
    template = env.get_template(default)
    return template

def get_data(file):
    reader = csv.DictReader(open(file), delimiter='|')
    return [ row for row in reader ]

def workflow(input_file):
    template = get_template()
    data = get_data(input_file)
    print template.render(restaurants=data)
    # should probably validate the generated json

if __name__ == '__main__':
    input_file = 'eat-notation-office.csv'
    sys.exit( workflow(input_file) )
