class TicketResponse:

    def __init__(self, TicketId, entryTime, slot, Status, floor, Vehicle):
        self.TicketId = TicketId
        self.entryTime = entryTime
        self.slot = slot
        self.Status = Status
        self.floor = floor
        self.Vehicle = Vehicle
