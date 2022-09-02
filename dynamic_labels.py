from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Bieber", "Bob", "Justin", "Shawn", "Jerry"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            self.create_widgets(name)

        return self.root

    def create_widgets(self, name):
        temp_button = Button(text=name)
        self.root.ids.main_box.add_widget(temp_button)


DynamicLabelsApp().run()