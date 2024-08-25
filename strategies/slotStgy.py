from abc import ABC, abstractmethod

from models import VehicleType, Slot


class SlotStgy(ABC):

    @abstractmethod
    def get_slot(self, vehicleType: VehicleType, gate) -> Slot:
        pass