from dataclasses import dataclass
from request import Request


# stores information about single advertisement
@dataclass
class PropertyUnit:
    request: Request  # by which request was this info obtained
    id: int  # id in parsaraki database
    date: str  # date of request
    bedrooms: int
    price: int
    lat: float
    lon: float
