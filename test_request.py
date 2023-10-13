import unittest
from request import create_request, Request


class TestRequestParser(unittest.TestCase):
    def test_create_request_ok(self):
        input_json = ('{"lat": 34.7,'
                      '"lon": 33.3,'
                      '"lon": 33.3,'
                      '"radius": 5000,'
                      '"action": "rent",'
                      '"propertyType": "apartmemts",'
                      '"priceMin": 10,'
                      '"priceMax": 3000,'
                      '"constructionYearMin": 2000,'
                      '"constructionYearMax": 2023,'
                      '"numberBedrooms": [3],'
                      '"areaMin": 50,'
                      '"areaMax": 150,'
                      '"furnishing": "fully",'
                      '"facilities": ["pool", "fireplace", "elevator"],'
                      '"pets": "allowed",'
                      '"onlineViewing": "no"'
                      '}')
        expected = Request(lat=34.7, lon=33.3, radius=5000,
                           action="rent", propertyType="apartmemts",
                           priceMin=10, priceMax=3000, constructionYearMin=2000,
                           constructionYearMax=2023, numberBedrooms=[3],
                           areaMin=50, areaMax=150, furnishing="fully",
                           facilities=["pool", "fireplace", "elevator"],
                           pets="allowed", onlineViewing="no")
        self.assertEqual(expected, create_request(input_json))

    def test_create_request_errors(self):
        with self.assertRaises(ValueError) as exc:
            r = Request(lat=12.22, lon=33.33)
            self.assertEqual(str(exc.exception), "Latitude OUT OF CYPRUS!")


if __name__ == '__main__':
    unittest.main()
