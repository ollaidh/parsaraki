from search_parameters import SearchParameters
import requests


def create_bazaraki_search_request(search: SearchParameters) -> requests.request:
    url = 'https://www.bazaraki.com/'
    action = 'real-estate-to-rent/'
    property_type = 'apartments-flats/' if search.propertyType == 'apartments' else 'houses'
    furnish = f'furnishing---{str(search.furnishing)}/' if search.furnishing else ''
    bedrooms = ''
    for param in search.numberBedrooms:
        bedrooms += f'number-of-bedrooms---{param}/'
    pets = f'pets---{search.pets}/'
    part1 = url + action + property_type + furnish + bedrooms + pets
    params = {'price_min': search.priceMin,
              'price_max': search.priceMax,
              'lat': search.lat,
              'lng': search.lon,
              'radius': search.radius}
    request = requests.get(part1, params)
    print(request.url)



