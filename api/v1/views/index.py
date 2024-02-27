#!/usr/bin/python3
"""index view module"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """"Return JSON status: OK"""
    return jsonify({"status": "OK"})


app_views.route('/api/v1/stats', methods=['GET'])


def get_stats():
    """Retrieve the number of each object type"""
    stat = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "review": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    }
    return jsonify(stats)
