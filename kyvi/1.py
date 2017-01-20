__author__ = 'kud'
from kivy.app import App  # for main app
from kivy.uix.floatlayout import FloatLayout  # UI layout
from kivy.uix.label import Label  # label for info
from kivy.clock import Clock  # clock
from plyer import accelerometer


class UI(FloatLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.lblAcce = Label(text="Accelerometer")
        self.add_widget(self.lblAcce)
        try:
            accelerometer.enable()
            Clock.shedule_interval(self.update, 1.0 / 24)
        except:
            self.lblAcce.text = "Failed to start accelerometer"

    def update(self, dt):
        txt = ""
        try:
            txt = "Accelerometer\nX=%.2f\nZ=%2.f" % (
                accelerometer.acceleration[0], accelerometer.acceleration[1], accelerometer.acceleration[2])
        except:
            txt = "Cannot read accelerometer"
            self.lblAcce.text = txt


class Accelerometer(App):
    def build(self):
        ui = UI()
        return ui


if __name__ == "__main__":
    Accelerometer().run()
