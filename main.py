from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen): #screen obj
   def sign_up(self):
       self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager): #inherits from Screenmanager obj
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            #create another pair of key/value
            users[uname] = {'username':uname, 'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H-%m-%S")}
        print(users)

        #overwrite existing users.json file, write new dict
        with open("users.json", 'w' ) as file:
            json.dump(users, file)
        #name screen want to switch to
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def return_log_in(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_screen"

class MainApp(App):
    def build(self):
        return RootWidget() 

if __name__=="__main__": 
    MainApp().run() 
