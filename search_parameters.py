from pydantic import BaseModel, Field


# class containing parameters of the search request.
# Inheriting from BaseModel as it allows to parse input
# json automatically and set default values
class SearchParameters(BaseModel):
    lat: float = Field(default=34.700778)
    lon: float = Field(default=34.700778)
    radius: int = Field(default=50000)
    action: str = Field(default="")
    propertyType: str = Field(default="")
    priceMin: int = Field(default=None)
    priceMax: int = Field(default=None)
    constructionYearMin: int = Field(default=None)
    constructionYearMax: int = Field(default=None)
    numberBedrooms: int = Field(default=None)
    areaMin: int = Field(default=None)
    areaMax: int = Field(default=None)
    furnishing: str = Field(default="")
    facilities: list[str] = Field(default=[])
    pets: str = Field(default="")
    onlineViewing: str = Field(default="")
