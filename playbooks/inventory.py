#! /usr/bin/python

# Simple inventory script to be used by jenkins
# FQDN is set by a jenkins parameter

from os import environ
from json import dumps


if environ.get('FQDN'):
    fqdn = environ.get('FQDN')
else:
    print "FQDN environmet variable not set"
    exit(1)

inventory = { "web": { "hosts": [ fqdn ] } } 



print dumps(inventory)
