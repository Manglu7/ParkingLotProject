from .BaseModel import BaseModel
from datetime import datetime
from .Slot import Slot
from .Gate import Gate

class Ticket(BaseModel):
    def __init__(self, id: int, number: str, 
                 entry_time: datetime, vehicle, 
                 parking_slot: Slot, generated_gate: Gate):
        super().__init__(id)
        self.number = number
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.parking_slot = parking_slot
        self.generated_gate = generated_gate
