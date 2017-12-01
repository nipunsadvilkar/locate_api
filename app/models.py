#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Locate(db.Model):
    __tablename__ = 'locate'

    locate_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(500))
    type_col = db.Column(db.String(15))
    response_dump = db.Column(JSON)

    def __init__(self, location, type_col, response_dump):
        self.location = location
        self.type_col = type_col
        self.response_dump = response_dump

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Locate.query.all()

    def fetch_location_data(location):
        return Locate.query.filter_by(location=location).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<locate_id {}>'.format(self.locate_id)

