#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
import sys
sys.path.append('.')
from models.city import City
from models.touristsite import TouristSite
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request, redirect


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
