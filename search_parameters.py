from pydantic import BaseModel, Field
import json


# class containing parameters of the search request.
# Inheriting from BaseModel as it allows to parse input
# json automatically and set default values
class SearchParameters(BaseModel):
    lat: float = Field(default=34.700778)
    lon: float = Field(default=34.700778)
    radius: int = Field(default=50000)
    action: str = Field(default="")
    propertyType: str = Field(default="")
    priceMin: int = Field(default=10)
    priceMax: int = Field(default=None)
    numberBedrooms: list[int] = Field(default=[])
    areaMin: int = Field(default=None)
    areaMax: int = Field(default=None)
    furnishing: int = Field(default=None)
    pets: int = Field(default=None)


