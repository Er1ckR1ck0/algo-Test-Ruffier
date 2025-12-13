from kivy.uix.label import Label
from kivy.clock import Clock

class Seconds(Label):
    def __init__(self, total, **kwargs):
        super().__init__()
        self.restart(total=total)
        
    def get_text(self):
        return f"Осталось: {self.total} сек."
        
    def restart(self, total, **kwargs):
        self.total = total
        self.text = self.get_text()

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.total -= 1
        self.text = self.get_text()
        if self.total <= 0:
            self.text = "Стоп!"
            return False