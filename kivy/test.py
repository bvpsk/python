from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class screen(GridLayout):
    def __init__(self, **kwargs):
        super(screen,self).__init__(**kwargs)
        self.cols = 2
        self.text = str(0)
        self.label = Label(text = self.text)
        self.add_widget(self.label)
 #       self.add_widget(Label(text = ''))
        bt1=Button(text = '+1',background_color = (0,0,1.5,2.5))
        bt2 = Button(text = '-1',background_color = (0,0,1.5,1.0))
        self.add_widget(bt1)
        self.add_widget(bt2)
        bt1.bind(on_press = self.a)
        bt2.bind(on_press = self.s)
    def a(self,event):
        self.label.text = str(int(self.label.text) + 1)
    def s(self,event):
        self.label.text = str(int(self.label.text) - 1)

class aa(App):
    def build(self):
        return screen()
if __name__ == '__main__':
    aa().run()
