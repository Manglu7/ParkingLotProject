from .BaseModel import BaseModel
from .PaymentModes import PaymentModes
from .PaymentStatus import PaymentStatus
from datetime import datetime

class Payment(BaseModel):
    def __init__(self, id: int, amount: int, 
                 payment_mode: PaymentModes, ref_id: str, bill,
                 payment_status: PaymentStatus, paid_at: datetime):
        super().__init__(id)
        self.amount = amount
        self.payment_mode = payment_mode
        self.ref_id = ref_id
        self.bill = bill
        self.payment_status = payment_status
        self.paid_at = paid_at
