from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen): #screen obj
   def sign_up(self):
       print("sign up button pressed")

class RootWidget(ScreenManager): #inherits from Screenmanager obj
    pass

class MainApp(App): #inherit form App obj
    def build(self):
        return RootWidget() #object not class

if __name__=="__main__": #call MainApp class
    #crate instance of MainApp and use run method of mainApp and App
    MainApp().run() 
