from pydantic import BaseModel

class HousingInput(BaseModel):

    median_income: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    latitude: float
    longitude: float
    ocean_proximity: str