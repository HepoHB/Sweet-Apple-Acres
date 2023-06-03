from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    title = "Sweet Apple Acres"
    def build(self):
        return RootWidget()
    
class RootWidget(FloatLayout):
    pass

class LoginSystem(FloatLayout):
    pass

MyApp().run()