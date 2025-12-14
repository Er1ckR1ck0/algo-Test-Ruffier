from .counter import BaseCounter

class Seconds(BaseCounter):
    
    def __init__(self, total, **kwargs):
        super().__init__(total=total, text="сек.")
