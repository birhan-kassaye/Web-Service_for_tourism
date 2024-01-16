#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
import sys
sys.path.append('.')
from models.city import City
from models.touristsite import TouristSite
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request, redirect


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
def get_all_places():
    sites = storage.all(TouristSite)
    places = []
    for site in sites.values():
        places.append(site.to_dict())

    return jsonify(places)


@app_views.route('/all', methods=['GET'], strict_slashes=False)
def get_all():
    allObj = storage.all()
    allObjs = []
    for i in allObj.values():
        allObjs.append(i.to_dict())
    
    return jsonify(allObjs)


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

@app_views.route('/add_city', methods=['GET', 'POST'], strict_slashes=False)
def add_city():
    if request.method == 'POST':
        new = City()

        new.name = request.form.get('name')
        new.population = request.form.get('population')
        new.region = request.form.get('region')
        new.location = request.form.get('location')
        storage.new(new)
        storage.save()
        return redirect('http://0.0.0.0:5000')

@app_views.route('/add_place', methods=['POST', 'GET'], strict_slashes=False)
def add_place():
    if request.method == 'POST':
        new = TouristSite()

        new.name = request.form.get('place')
        new.location = request.form.get('location')
        
        for i in storage.all('City').values():
            if i.to_dict()['name'] == request.form.get('city'):
                new.city_id = i.to_dict()['id']
                break
            else:
                continue

        new.description['type'] = request.form.get('type')
        new.description['price'] = request.form.get('price')
        new.description['detail'] = request.form.get('details')
        storage.new(new)
        storage.save()
        return redirect('http://0.0.0.0:5000')


if __name__ == '__main__':
    app_views.run(host='0.0.0.0', port=5000)
