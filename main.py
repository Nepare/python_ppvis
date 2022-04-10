from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class DatabaseApp(App):
    def build(self):
        label = Label(text='Hello world :)')
        layout = BoxLayout(padding=10)
        layout.add_widget(label)

        return layout


if __name__ == '__main__':
    app = DatabaseApp()
    app.run()