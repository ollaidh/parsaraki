from pydantic import BaseModel, field_validator, model_validator, Field

# map json input actions (buy, rent etc) to bazaraki actions
actions = {"rent": "real-estate-to-rent", "buy": "real-estate-for-sale"}

property_types = {"apartment": "apartments-flats", "house": "houses"}


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
    numberBedrooms: list[str] = Field(default=[])
    furnishing: list[str] = Field(default="")
    pets: str = Field(default="")

    @field_validator("lat")
    def lat_ok(cls, v) -> float:
        if v < 34.545318 or v > 35.693639:
            raise ValueError("Latitude OUT OF CYPRUS!")
        return v

    @field_validator("lon")
    def lon_ok(cls, v) -> float:
        if v < 32.328499 or v > 34.585886:
            raise ValueError("Latitude OUT OF CYPRUS!")
        return v

    @field_validator("radius")
    def radius_ok(cls, v) -> int:
        if v and v < 0:
            raise ValueError(f"Search radius must ne positive!")
        return v

    @field_validator("action")
    @classmethod
    def action_ok(cls, v) -> str:
        if v and v not in actions:
            raise ValueError(f"Actions are: {actions.keys()}!")
        return actions[v]

    @field_validator("propertyType")
    @classmethod
    def property_ok(cls, v) -> str:
        if v and v not in property_types:
            raise ValueError(f"Types of property are: {property_types.keys()}!")
        return property_types[v]

    @field_validator("priceMin")
    def price_min_ok(cls, v) -> int:
        if v and v < 0:
            raise ValueError("Min price must be > 0!")
        return int(v)  # bazaraki accepts integers only

    @field_validator("priceMax")
    def price_max_ok(cls, v) -> int:
        if v and v < 0:
            raise ValueError("Max price must be > 0!")
        return int(v)

    @model_validator(mode="before")
    def prices_ok(cls, data) -> int:
        if (
            "priceMin" in data.keys()
            and "priceMax" in data.keys()
            and data["priceMin"] > data["priceMax"]
        ):
            raise ValueError("Max price must be > Min price!")
        return data

    @field_validator("numberBedrooms")
    def bedrooms_ok(cls, values) -> str:
        bedrooms = {"studio"}
        for v in values:
            try:
                if int(v) < 0:
                    raise ValueError("Number of bedrooms must be positive!")
            except ValueError:
                if v not in bedrooms:
                    raise ValueError(
                        f"Number of bedrooms must be entered as a number or {bedrooms}"
                    )
        return

    @field_validator("furnishing")
    def furnishing_ok(cls, values) -> list[str]:
        furnishing = {"yes": "1", "no": "2", "partly": "3", "appliances only": "4"}
        f = []
        for v in values:
            if v not in furnishing:
                raise ValueError(f"Furnishing can be: {furnishing}")
            f.append(furnishing[v])
        return f

    @field_validator("pets")
    def pets_ok(cls, value) -> list[str]:
        pets = {"yes": "1", "no": "2"}
        if value not in pets:
            raise ValueError(f"Furnishing can be: {pets}")
        return pets[value]
