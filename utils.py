#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from configparser import ConfigParser


def load_secret_config():
    """
    Method to load the secret configurations.

    Parameters
    ----------
    None

    Returns
    -------
    config: ConfigParser
        Secrets configuration.
    """
    secret_path = path.join(
        path.dirname(path.abspath(__file__)), 'etc', 'config', 'secrets.ini'
    )
    config = ConfigParser(allow_no_value=True)
    config.read(secret_path)

    return config


