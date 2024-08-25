from .VehicleType import VehicleType
from typing import List 
from .FloorStatus import FloorStatus
from .BaseModel import BaseModel

class Floor(BaseModel):
    def __init__(self, id: int, parking_slots_list: List, 
                 floor_number: int, floor_status: FloorStatus,
                 allowed_vehicles: List[VehicleType]):
        super().__init__(id)
        self.parking_slots_list = parking_slots_list
        self.floor_number = floor_number
        self.floor_status = floor_status
        self.allowed_vehicles = allowed_vehicles

