from search_parameters import SearchParameters
# from property_unit import PropertyUnit
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs
import datetime


# create web request based on input search parameters and get results of request
def search_bazaraki(search: SearchParameters) -> tuple:
    # bazaraki search request consists of two parts: addresses (endpoints) and parameters
    # endpoints include number of search parameters: action, property type, bedrooms, furnish, pets
    # parameters include number of search parameters: price min/max, lon, lat, radius

    # forming endpoints part of request:
    url = 'https://www.bazaraki.com/'
    action = 'real-estate-to-rent/'
    property_type = 'apartments-flats/' if search.propertyType == 'apartments' else 'houses/'
    furnish = ''
    for param in search.furnishing:
        furnish += f'furnishing---{param}/'
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
def parse_single_ads(parameters: tuple[str, dict]) -> dict[int: dict]:
    # returning the result - dict where key is id of apartment and value is dict with it's parameters
    result = {}

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
        # print(results)
        # list of all ads:
        ads = results.find_all("a", class_="advert__content-price _not-title")
        # get property id, price, bedrooms and link for each ad from search results:
        for ad in ads:
            # get prices (current and maybe before discount):
            prices = ad.find('span').get_text(strip=True).lstrip("€")
            # to get only current price and get rid of price before discount:
            prices = prices.split('€')

            id_ppt = int(ad["href"].split("/")[2].split("_")[0])
            price = prices[0]
            bedrooms = ad["href"].split("/")[2].split("_")[1].split("-")[0]
            link = f'https://www.bazaraki.com{ad["href"]}'
            result[id_ppt] = {
                    "date": str(datetime.date.today()),
                    "price": price,
                    "bedrooms": bedrooms,
                    "link": link
                }
        # go to next page:
        parameters[1]['page'] += 1

    print(result)
    return result
