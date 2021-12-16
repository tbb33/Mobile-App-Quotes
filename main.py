from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen): #screen obj
   def sign_up(self):
       #order to display screen
       self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager): #inherits from Screenmanager obj
    pass

class SignUpScreen(Screen):
    def sign_up(self, uname, pword):
        print(uname, pword)

class MainApp(App):
    def build(self):
        return RootWidget() 

if __name__=="__main__": 
    MainApp().run() 
