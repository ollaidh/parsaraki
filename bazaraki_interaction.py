from search_parameters import SearchParameters
from property_unit import PropertyUnit
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs


# create web request based on input search parameters and get results of request
def search_bazaraki(search: SearchParameters) -> tuple:
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
    endpoints = url + action + property_type + furnish + bedrooms + pets

    # forming parameters part of request:
    params = {'price_min': search.priceMin,
              'price_max': search.priceMax,
              'lat': search.lat,
              'lng': search.lon,
              'radius': search.radius}

    return endpoints, params


# sends a request, gets search result, parses search result into separate links to each adv
def parse_single_ads(parameters: tuple[str, dict]):
    # using set to avoid duplicates, because the same ad on one page can occur twice:
    # in VIP section and in regular section
    result = set()

    # starting from page 1
    parameters[1]['page'] = 1

    # send request and parse results:
    req_result = requests.get(parameters[0], parameters[1])
    soup = BeautifulSoup(req_result.content, "html.parser")
    # finding a section with number of search pages info:
    results = soup.find("link", rel="last")
    if results:
        # getting number of pages:
        url = results["href"]
        parsed_url = urlparse(url)
        pages = int(parse_qs(parsed_url.query)['page'][0])
    # if no info on number of pages - means we have only one page:
    else:
        pages = 1

    # for each page of search results:
    while parameters[1]['page'] <= pages:
        # send a request and parse it:
        req_result = requests.get(parameters[0], parameters[1])
        soup = BeautifulSoup(req_result.content, "html.parser")
        results = soup.find(id="listing")
        # list of all ads:
        ads = results.find_all("a", class_="advert__content-price _not-title")
        # form the whole link and add to resulting set:
        for ad in ads:
            result.add('https://www.bazaraki.com' + ad["href"])
        # go to next page:
        parameters[1]['page'] += 1
    return result


def get_adv_params(adv_link: str) -> PropertyUnit:
    adv_req = requests.get(adv_link)
    soup = BeautifulSoup(adv_req.content, "html.parser")
    print(soup)



