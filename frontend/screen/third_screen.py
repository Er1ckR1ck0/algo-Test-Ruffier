import backend.data as data
from backend.instructions import txt_sits
from frontend.components import *


class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        main_layout = BoxLayout(orientation="vertical")
        instruction = Label(text=txt_sits)

        self.button = MyButton(self, "third_screen", "left", text="Продолжить")
        self.button.on_press = self.button.next

        main_layout.add_widget(instruction)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
