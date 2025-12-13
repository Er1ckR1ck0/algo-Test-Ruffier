import time
import backend.data as data
from backend.instructions import txt_sits
from frontend.components import *


class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        main_layout = BoxLayout(orientation="vertical")
        instruction = Label(text=txt_sits)
        
        self.timer = Seconds(4)
        self.timer.bind(done=self.next)
        
        self.button = MyButton(self, "third_screen", "left", text="Продолжить")
        self.button.on_press = self.next
        
        main_layout.add_widget(instruction)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self, *args):
        if self.timer.done:
            self.button.disabled = False
            self.button.next()
        else:
            self.button.text = "Подождите!"
            self.button.disabled = True
            self.timer.start()