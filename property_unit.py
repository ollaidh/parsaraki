from dataclasses import dataclass


# stores information about single advertisement
@dataclass
class PropertyUnit:
    id: int  # id in bazaraki.com database
    price_history: {str: int}  # key - date, value - price
    bedrooms: int  # number of bedrooms
    adv_link: str  # link to the advertisement on bazaraki.com
