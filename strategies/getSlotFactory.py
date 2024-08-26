from models import SlotAssignmentStrategyEnum
from .RandomSlotFindingStgy import RandomSlotFindingStgy


class SlotFactory:

    @staticmethod
    def get_slot_stgy_obj(slotStrgyEnum):
        if slotStrgyEnum == SlotAssignmentStrategyEnum.RANDOM:
            return RandomSlotFindingStgy()
