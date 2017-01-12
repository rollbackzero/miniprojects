#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader
import yaml
import codecs
import sys

ENV = Environment(loader=FileSystemLoader('./'))

# load yaml file into dictionary

with open("data.yaml") as _:
    dict =  yaml.load(_)

# Render template and print generated config to console, also set codec so you can output it to a text file
template = ENV.get_template("template.txt")
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
print template.render(config=dict)
