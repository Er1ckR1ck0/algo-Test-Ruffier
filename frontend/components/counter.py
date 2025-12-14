from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class BaseCounter(Label):
    done = BooleanProperty(False)
    
    def __init__(self, total, text, **kwargs):
        super().__init__()
        self.size_hint = (1, .25)
        self.restart(total=total, text=text)
        
    def get_text(self, text):
        return self.template_text.format(total=self.total, text=text)
        
    def restart(self, total, text, **kwargs):
        self.done = False
        self.total = total
        self._text = text
        self.template_text = "Осталось: {total} {text}"
        self.text = self.get_text(self._text)
        
    def start(self):
        self.event = Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.total -= 1
        self.text = self.get_text(self._text)
        if self.total <= 0:
            self.text = "Стоп!"
            self.done = True
            self.event.cancel()
            return False