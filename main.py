from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen): #screen obj
   def sign_up(self):
       self.manager.current = "sign_up_screen"
   
   def login(self, uname, pword):
       with open("users.json") as file:
           users = json.load(file)
       if uname in users and users[uname]['password'] == pword:
           self.manager.current = "login_screen_success"
       else:
           self.ids.login_wrong.text = "Wrong username or password"

class RootWidget(ScreenManager): #inherits from Screenmanager obj
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            users[uname] = {'username':uname, 'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H-%m-%S")}
        
        with open("users.json", 'w' ) as file:
            json.dump(users, file)
        #name screen want to switch to
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def return_log_in(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current ="Login_screen"

class MainApp(App):
    def build(self):
        return RootWidget() 

if __name__=="__main__": 
    MainApp().run() 
