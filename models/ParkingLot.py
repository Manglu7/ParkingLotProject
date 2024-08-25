from .BaseModel import BaseModel
from typing import List
from .VehicleType import VehicleType
from .SlotAssignmentStrategy import SlotAssignmentStrategyEnum
from .Floor import Floor
from .Gate import Gate
from .ParkingLotStatus import ParkingLotStatus

class ParkingLot(BaseModel):
    def __init__(self, id: int, name: str, address: str,
                 parking_floors: List[Floor], gates: List[Gate],
                 allowed_vehicles: List[VehicleType], 
                 capacity: int, status: ParkingLotStatus,
                 slot_assignment_strategy: SlotAssignmentStrategyEnum):
        super().__init__(id)
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.gates = gates
        self.allowed_vehicles = allowed_vehicles
        self.capacity = capacity
        self.status = status
        self.slot_assignment_strategy = slot_assignment_strategy
