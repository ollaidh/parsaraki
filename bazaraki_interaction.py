from search_parameters import SearchParameters
import requests


# create web request based on input search parameters and get results of request
def search_bazaraki(search: SearchParameters) -> requests.request:
    # bazaraki search request consists of two parts: addresses (endpoints) and parameters
    # endpoints include number of search parameters: action, property type, bedrooms, furnish, pets
    # parameters include number of search parameters: price min/max, lon, lat, radius

    # forming endpoints part of request:
    url = 'https://www.bazaraki.com/'
    action = 'real-estate-to-rent/'
    property_type = 'apartments-flats/' if search.propertyType == 'apartments' else 'houses/'
    furnish = f'furnishing---{str(search.furnishing)}/' if search.furnishing else ''
    bedrooms = ''
    for param in search.numberBedrooms:
        bedrooms += f'number-of-bedrooms---{param}/'
    pets = f'pets---{search.pets}/' if search.pets else ''
    part1 = url + action + property_type + furnish + bedrooms + pets

    # forming parameters part of request:
    params = {'price_min': search.priceMin,
              'price_max': search.priceMax,
              'lat': search.lat,
              'lng': search.lon,
              'radius': search.radius}

    # request:
    request = requests.get(part1, params)
    return request




