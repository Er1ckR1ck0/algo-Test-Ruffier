# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

import backend.data as data
from frontend.screen import (
    fifth_screen,
    fourth_screen,
    first_screen,
    third_screen,
    second_screen,
)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(fourth_screen.FourthScreen(name="third_screen"))
        sm.add_widget(first_screen.FirstScreen(name="main_screen"))
        sm.add_widget(second_screen.SecondScreen(name="first_screen"))
        sm.add_widget(third_screen.ThirdScreen(name="second_screen"))
        sm.add_widget(fifth_screen.FifthScreen(name="final_screen"))
        return sm


app = MyApp()
app.run()
