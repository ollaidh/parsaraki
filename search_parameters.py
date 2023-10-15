from pydantic import BaseModel, Field
import json


# class containing parameters of the search request.
# Inheriting from BaseModel as it allows to parse input
# json automatically and set default values
class SearchParameters(BaseModel):
    lat: float = Field(default=34.6974)
    lon: float = Field(default=33.0832)
    radius: int = Field(default=5000)
    action: str = Field(default="rent")
    propertyType: str = Field(default="")
    priceMin: int = Field(default=None)
    priceMax: int = Field(default=None)
    numberBedrooms: list[int] = Field(default=[])
    furnishing: int = Field(default=None)
    pets: int = Field(default=None)


