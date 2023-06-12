from kivy.app import App
from requests.employees import Employees
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class MyPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Login Inválido!'
        self.size_hint = (None, None)
        self.size = (200, 150)

        content = Label(text='Confira os dados de login.')
        close_button = Button(text='Fechar', size_hint=(1, 0.2))
        close_button.bind(on_release=self.dismiss)

        self.content = BoxLayout(orientation='vertical')
        self.content.add_widget(content)
        self.content.add_widget(close_button)

class MyApp(App):
    title = "Sweet Apple Acres"
    def build(self):
        return RootWidget()
    
class RootWidget(FloatLayout):
    pass

class LoginSystem(FloatLayout):

        def loginButton(self):
            enterLogin = self.ids.inputLogin.text
            enterPassword = self.ids.inputPassword.text
            if  enterLogin != "" and enterPassword  != "": 
                JSONEmployees = Employees()
                print(JSONEmployees.Login(enterLogin.strip(), enterPassword.strip()))
                if(JSONEmployees.Login(enterLogin.strip(), enterPassword.strip())):
                     print('Login OK')
                else:
                    popup = MyPopup()
                    popup.open()
            else:
                popup = MyPopup()
                popup.open()
                


MyApp().run()