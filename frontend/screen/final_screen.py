import backend.data as data
from backend.ruffier import test
from frontend.components import *


class FinalScreen(Screen):
    instruction = Label(text="Nope")

    @classmethod
    def update(cls):
        cls.instruction.text = test(data.P1, data.P2, data.P3, data.age)

    def __init__(self, **kw):
        super().__init__(**kw)
        main_layout = BoxLayout(orientation="vertical")

        main_layout.add_widget(self.instruction)

        self.add_widget(main_layout)
