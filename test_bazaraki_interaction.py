import unittest

from bazaraki_interaction import *
from search_parameters import SearchParameters


class TestBazarakiInteraction(unittest.TestCase):
    def test_search_bazaraki(self):
        input_request1 = SearchParameters(lat=34.700778, lon=33.055763, radius=5000,
                                          action="rent", propertyType="apartments",
                                          priceMin=10, priceMax=3000, numberBedrooms=["3"],
                                          furnishing=["yes"], pets="yes")
        expected_endpoints1 = ('https://www.bazaraki.com/real-estate-to-rent/apartments-flats/'
                               'furnishing---1/number-of-bedrooms---3/pets---1/')
        expected_params1 = {'price_min': input_request1.priceMin,
                            'price_max': input_request1.priceMax,
                            'lat': input_request1.lat,
                            'lng': input_request1.lon,
                            'radius': input_request1.radius}
        endpoints1, params1 = search_bazaraki(input_request1)
        self.assertEqual(expected_endpoints1, endpoints1)
        self.assertEqual(expected_params1, params1)

        # no search parameters given, default from SearchParameters class are used:
        input_request2 = SearchParameters()
        expected_endpoints2 = 'https://www.bazaraki.com/real-estate-to-rent/houses/'
        expected_params2 = {'lat': 34.6974,
                            'lng': 33.0832,
                            'price_max': None,
                            'price_min': None,
                            'radius': 5000}
        endpoints2, params2 = search_bazaraki(input_request2)
        self.assertEqual(expected_endpoints2, endpoints2)
        self.assertEqual(expected_params2, params2)
