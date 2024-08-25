from datetime import datetime

class BaseModel:
    def __init__(self, id: int):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
