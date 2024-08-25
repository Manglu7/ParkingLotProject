from .BaseModel import BaseModel
from .VehicleType import VehicleType
from .SlotStatus import SlotStatus
from .Floor import Floor

class Slot(BaseModel):
    def __init__(self, id: int, slot_number: int, 
                 vehicle_type: VehicleType, 
                 parking_slot_status: SlotStatus,
                 parking_floor: Floor):
        super().__init__(id)
        self.slot_number = slot_number
        self.vehicle_type = vehicle_type
        self.parking_slot_status = parking_slot_status
        self.parking_floor = parking_floor
