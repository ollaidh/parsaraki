# Parsaraki



### Input request json
Has the following structure and options:

    {
      "lat": 34.700778,
      "lon": 33.055763,
      "radius": 5000,
      "action": "rent",
      "propertyType": "apartments",
      "priceMin": 1000,
      "priceMax": 5000,
      "numberBedrooms": ["2", "3", "studio"],
      "furnishing": ["yes", "partly"],
      "pets": "yes"
    }

- `lat` (float) - latitude (decimal degrees) of the center of searching area. *Default* = `34.6974`
- `lon` (float) - longitude (decimal degrees) of the center of searching area. *Default* = `33.0832` 
- `radius`(int) - radius (meters) of search area. *Default* = `5000`
- `action`(str) - do we buy or rent. *Options:* `rent`, `buy`. *Defualt* = `buy`
- `propertyType` (str) - type of property. *Options:* `apartments`, `houses`. *Defualt* = empty 
- `priceMin` (int) - minimum price for rent/sale. *Defualt* = empty
- `priceMax` (int) - maximum price for rent/sale. *Defualt* = empty 
- `numberBedrooms` (list[str]) - number of bedrooms. *Options:* `1`... `100`, `studio`. *Defualt* = empty 
- `furnishing` (list[str]) - kind of furnishing for property.  *Options:* `yes`, `no`, `partly`, `appliances only`. *Defualt* = empty 
- `pets` (str) - are pets allowed. *Options:* `yes`, `no`. *Defualt* = empty

Where the default option is empty, if nothing is set search results include all available options.
