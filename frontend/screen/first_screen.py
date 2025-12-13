import backend.data as data
from backend.instructions import txt_instruction
from frontend.components import *


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        main_layout = BoxLayout(orientation="vertical")
        instruction = Label(text=txt_instruction)

        self.name_input, self.age_input = [
            TextInput(size_hint=(0.05, 0.75)) for i in range(2)
        ]

        name_layout, age_layout = [
            BoxLayout(size_hint=(0.75, 0.15), pos_hint={"center_x": 0.5}, padding=4)
            for i in range(2)
        ]

        name_layout.add_widget(Label(text="Введите имя:", size_hint=(0.05, 0.35)))
        name_layout.add_widget(self.name_input)
        age_layout.add_widget(Label(text="Введите возраст:", size_hint=(0.05, 0.35)))
        age_layout.add_widget(self.age_input)

        self.button = MyButton(self, "first_screen", "left", text="Начать")
        self.button.on_press = self.next

        main_layout.add_widget(instruction)
        main_layout.add_widget(name_layout)
        main_layout.add_widget(age_layout)
        main_layout.add_widget(self.button)
        self.add_widget(main_layout)

    def next(self):
        try:
            age = int(self.age_input.text)
            name = self.name_input.text

            if " " in name:
                self.name_input.text = "Введите имя без пробелов"
                raise Exception("Имя с пробелами")

            if not (7 <= age <= 80):
                self.age_input.text = "Данный возраст не подход"
                raise Exception("За пределами возраста")

            data.age = age
            data.name = name

            self.button.next()

        except Exception as e:
            print(e)
