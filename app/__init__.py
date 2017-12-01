#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from locate import get_data_from_foursquare

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from app.models import Locate

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/save/', methods=['POST'])
    def save_location_data():
        location = str(request.data.get('location', ''))
        type_col = str(request.data.get('type_col', ''))
        response_dump = json.dumps(get_data_from_foursquare(location))
        # import pdb; pdb.set_trace()
        # location_resonse = Locate.get_location_data(location)
        if location:
            locate = Locate(location=location, type_col=type_col,
                            response_dump=response_dump)
            locate.save()
            response = jsonify({
                'locate_id': locate.locate_id,
                'location': locate.location,
                'type_col': locate.type_col,
                'response_dump': locate.response_dump
            })
            response.status_code = 201
            return response

    @app.route('/locate/<location>', methods=['GET'])
    def get_location_data(location):
        response = jsonify(get_data_from_foursquare(location))
        response.status_code = 200
        return response

    @app.route('/fetch/<location>', methods=['GET'])
    def fetch_location_data(location):
        locate_fetch = Locate.fetch_location_data(location)
        return locate_fetch


    return app
