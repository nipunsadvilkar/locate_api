#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Logic to create the keys in secrets.ini.sample to secrets.ini file."""
import configparser
config = configparser.ConfigParser()

with open('etc/config/secrets.ini.sample', 'r') as f:
    config.readfp(f)

try:
    with open('etc/config/secrets.ini', 'r') as f:
        config.readfp(f)
except IOError:
    pass

with open('etc/config/secrets.ini', 'w') as f:
    config.write(f)
