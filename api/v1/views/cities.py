#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
from models.city import City
from models.touristsite import TouristSite
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities():
    """
    Retrieves the list of all cities objects
    of a specific State, or a specific city
    """
    list_cities = []
    cities = storage.all(City)
    for city in cities.values():
        list_cities.append(city.to_dict())

    return jsonify(list_cities)


@app_views.route('/city/<city_id>/', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """
    Retrieves a specific city based on id
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/city/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    sites = storage.all(TouristSite)
    places = []
    for site in sites.values():
        if site.to_dict()['city_id'] == city_id:
            places.append(site.to_dict())
        else:
            pass

    return jsonify(places)


@app_views.route('/allplaces', methods=['GET'], strict_slashes=False)
def get_all():
    sites = storage.all(TouristSite)
    places = []
    for site in sites.values():
        places.append(site.to_dict())

    return jsonify(places)


@app_views.route('/city/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """
    Deletes a city based on id provided
    """
    city = storage.get(City, city_id)

    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({'error': 'not found'})

if __name__ == '__main__':
    app_views.run(host='0.0.0.0', port=5000)
