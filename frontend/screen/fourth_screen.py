import backend.data as data
from backend.instructions import txt_instruction
from frontend.components import *
from frontend.screen import fiveth_screen


class ThirdScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        main_layout = BoxLayout(orientation="vertical")
        instruction = Label(text=txt_instruction)

        self.p2_input, self.p3_input = [
            TextInput(size_hint=(0.05, 0.75)) for i in range(2)
        ]

        p2_layout, p3_layout = [
            BoxLayout(size_hint=(0.75, 0.15), pos_hint={"center_x": 0.5}, padding=4)
            for i in range(2)
        ]

        p2_layout.add_widget(Label(text="Введите Пульс до:", size_hint=(0.05, 0.35)))
        p2_layout.add_widget(self.p2_input)
        p3_layout.add_widget(Label(text="Введите Пульс после:", size_hint=(0.05, 0.35)))
        p3_layout.add_widget(self.p3_input)

        self.button = MyButton(self, "final_screen", "left", text="Начать")
        self.button.on_press = self.next

        main_layout.add_widget(instruction)
        main_layout.add_widget(p2_layout)
        main_layout.add_widget(p3_layout)
        main_layout.add_widget(self.button)
        self.add_widget(main_layout)

    def next(self):
        try:
            p2 = int(self.p2_input.text)
            p3 = int(self.p3_input.text)

            if not (10 <= p2 <= 40):
                self.p2_input.text = "Как может быть такой пульс за 15 секунд?"
                raise Exception("За пределами пульса")
            if not (10 <= p3 <= 40):
                self.p3_input.text = "Как может быть такой пульс за 15 секунд?"
                raise Exception("За пределами пульса")

            data.P2 = p2
            data.P3 = p3

            fiveth_screen.FinalScreen.update()
            self.button.next()

        except Exception as e:
            print(e)
