from pydantic import BaseModel, ValidationError, field_validator, Field
import json


class Request(BaseModel):
    lat: float = Field(default=34.700778)
    lon: float = Field(default=34.700778)
    radius: int = Field(default=50000)
    action: str = Field(default="")
    propertyType: str = Field(default="")
    priceMin: int = Field(default=None)
    priceMax: int = Field(default=None)
    constructionYearMin: int = Field(default=None)
    constructionYearMax: int = Field(default=None)
    numberBedrooms: list[int] = Field(default=None)
    areaMin: int = Field(default=None)
    areaMax: int = Field(default=None)
    furnishing: str = Field(default="")
    facilities: list[str] = Field(default=None)
    pets: str = Field(default="")

    @field_validator('lat')
    def lat_ok(cls, v) -> float:
        if v < 34.545318 or v > 35.693639:
            raise ValueError('Latitude OUT OF CYPRUS!')
        return v

    @field_validator('lon')
    def lon_ok(cls, v) -> float:
        if v < 32.328499 or v > 34.585886:
            raise ValueError('Latitude OUT OF CYPRUS!')
        return v

    @field_validator('radius')
    def radius_ok(cls, v) -> int:
        if v < 0:
            raise ValueError('Search radius must ne positive!')
        return v

    @field_validator('action')
    def action_ok(cls, v) -> int:
        actions = ["rent", "buy"]
        if v not in actions:
            raise ValueError(f'Actions are: {actions}!')
        return v


def create_request(json_data: str) -> Request:
    try:
        request = Request.model_validate_json(json_data)
    except ValidationError as e:
        print(f'ERROR:\n{e.json()}')
    else:
        return request


