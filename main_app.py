# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

import backend.data as data
from frontend.screen import (
    final_screen,
    first_screen,
    main_screen,
    second_screen,
    third_screen,
)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(main_screen.MainScreen(name="main_screen"))
        sm.add_widget(first_screen.FirstScreen(name="first_screen"))
        sm.add_widget(second_screen.SecondScreen(name="second_screen"))
        sm.add_widget(third_screen.ThirdScreen(name="third_screen"))
        sm.add_widget(final_screen.FinalScreen(name="final_screen"))
        return sm


app = MyApp()
app.run()
