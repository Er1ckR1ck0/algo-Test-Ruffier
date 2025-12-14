from .counter import BaseCounter

class Sits(BaseCounter):
    
    def __init__(self, total, **kwargs):
        super().__init__(total=total, text="приседаний")
