#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import load_secret_config
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import json
import requests
import geocoder

FOURSQUARE_URL = 'https://api.foursquare.com/v2/venues/explore'

config = load_secret_config()


def get_lat_long(location):
    """
    Method to get latitude and longitude for given location

    Parameters
    ----------
    location: string
        location should be ideally city

    Returns
    -------
    lat_long: list of latitude and longitude
        Latitude and Longitude for given location
    """
    g = geocoder.google(location)
    lat_long = g.latlng
    return lat_long


def get_data_from_foursquare(location):
    """
    Method to get data from foursquare API

    Parameters
    ----------
    location: string
        location should be ideally city

    Returns
    -------
    foursquare_data: JSON
        JSON response from a Foursquare API
    """
    params = dict(
        client_id=config.get('foursquare_app_info', 'fs_client_id'),
        client_secret=config.get('foursquare_app_info', 'fs_client_secret'),
        v='20170801',
        near=location,
        query='coffee',
        limit=5)
    foursquare_resp = requests.get(url=FOURSQUARE_URL, params=params)
    foursquare_data = json.loads(foursquare_resp.text)
    return(foursquare_data)


def get_data_from_uber(location):
    """
    Method to get data from Uber API

    Parameters
    ----------
    location: string
        location should be ideally city

    Returns
    -------
    foursquare_data: JSON
        JSON response from a foursquare API
    """
    lat, lng = get_lat_long(location)
    session = Session(server_token=config.get('uber_app_info',
                                              'uber_server_token'))
    client = UberRidesClient(session)
    response = client.get_products(lat, lng)
    uber_products = response.json.get('products')
    return(uber_products)


if __name__ == '__main__':
    print(get_data_from_foursquare('San Francisco'))
    print(get_data_from_uber('San Francisco'))
