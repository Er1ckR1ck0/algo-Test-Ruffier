import backend.data as data
from backend.instructions import txt_test1
from frontend.components import *


class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        main_layout = BoxLayout(orientation="vertical")
        instruction = Label(text=txt_test1)

        self.p1_input = TextInput(size_hint=(0.05, 0.75))

        p1_layout = BoxLayout(
            size_hint=(0.75, 0.15), pos_hint={"center_x": 0.5}, padding=4
        )

        p1_layout.add_widget(Label(text="Введите пульс:", size_hint=(0.05, 0.35)))
        p1_layout.add_widget(self.p1_input)

        self.button = MyButton(self, "second_screen", "left", text="Продолжить")
        self.button.on_press = self.next

        main_layout.add_widget(instruction)
        main_layout.add_widget(p1_layout)
        main_layout.add_widget(self.button)
        self.add_widget(main_layout)

    def next(self):
        try:
            p1 = int(self.p1_input.text)

            if not (10 <= p1 <= 40):
                self.p1_input.text = "Как может быть такой пульс за 15 секунд?"
                raise Exception("За пределами пульса")

            data.P1 = p1

            self.button.next()

        except Exception as e:
            print(e)
