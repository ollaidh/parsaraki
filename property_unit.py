from dataclasses import dataclass
from search_parameters import SearchParameters


# stores information about single advertisement
@dataclass
class PropertyUnit:
    request: SearchParameters  # by which request was this info obtained
    id: int  # id in parsaraki database
    date: str  # date of request
    bedrooms: int
    price: int
    lat: float
    lon: float
