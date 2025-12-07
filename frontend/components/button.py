from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class MyButton(Button):
    def __init__(self, screen, goal, direction, **kwargs):
        super().__init__(**kwargs)
        self.background_color = "#00ff00"
        self.size_hint = (0.25, 0.25)
        self.pos_hint = {"center_x": 0.5}
        self.screen: Screen = screen
        self.goal = goal
        self.direction = direction

    def next(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
        return super().on_press()
