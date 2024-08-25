from .BaseModel import BaseModel
from .VehicleType import VehicleType

class Vehicle(BaseModel):
    def __init__(self, id: int, owner_name: str, 
                 vehicle_type: VehicleType):
        super().__init__(id)
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type
