from .BaseModel import BaseModel
from .GateType import GateType
from .GateStatus import GateStatus

class Gate(BaseModel):
    def __init__(self, id: int, gate_number: int,
                  gate_type: GateType, parking_lot,
                    gate_status: GateStatus):
        super().__init__(id)
        self.gate_number = gate_number
        self.gate_type = gate_type
        self.parking_lot = parking_lot
        self.gate_status = gate_status
