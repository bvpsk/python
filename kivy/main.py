from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('./kv/button.kv')
Builder.load_file('./main.kv')
class add(Button):
    pass
class subtract(Button):
    pass
class Container(GridLayout):
    display = ObjectProperty()
    def add_one(self):
        val = int(self.display.text)
        self.display.text = str(val+1)
    def subtract_one(self):
        val = int(self.display.text)
        self.display.text = str(val-1)

class MainApp(App):

    def build(self):
        self.title = 'Awesome app!!!'
        return Container()
if __name__ == '__main__':
    app = MainApp()
    app.run()
