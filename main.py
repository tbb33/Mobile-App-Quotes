from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
from datetime import datetime
import glob
from pathlib import Path
import random

Builder.load_file('design.kv')

class LoginScreen(Screen): #screen obj
   def sign_up(self):
       self.manager.current = "sign_up_screen"
   
   def login(self, uname, pword):
       with open("users.json") as file:
           users = json.load(file)
       if uname in users and users[uname]['password'] == pword:
           self.manager.transition.direction = "left"
           self.manager.current = "login_screen_success"
       else:
           self.ids.login_wrong.text = "Wrong username or password"

   def forgot_pword(self):
       self.manager.current = "reset_password_screen"

class RootWidget(ScreenManager): #inherits from Screenmanager obj
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            
            if uname in users: 
                self.ids.taken_uname.text = "Username is taken. Please try another"
            else: 
                users[uname] = {'username':uname, 'password': pword,
                'created': datetime.now().strftime("%Y-%m-%d %H-%m-%S")}
        
                with open("users.json", 'w' ) as file:
                    json.dump(users, file)
                self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def return_log_in(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current ="Login_screen"

    def quote(self, feel):
        feel=feel.lower()
        avail_files = glob.glob("quotes/*txt")
        avail_files = [Path(filename).stem for filename in
                        avail_files]
        #print(avail_files)
        if feel in avail_files:
            with open(f"quotes/{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            #print(quotes)
            self.ids.show_quote.text = random.choice(quotes)
        else:
             self.ids.show_quote.text = "Try another feeling"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

#overwrites existing password if username exists
class ResetPasswordScreen(Screen):
    def reset(self, uname, pword):
        with open("users.json", 'r' ) as file:
            users = json.load(file)
                
            if uname in users:
                users[uname] = {'username':uname, 'password': pword,
                'created': datetime.now().strftime("%Y-%m-%d %H-%m-%S")}
        
                with open("users.json", 'w' ) as file:
                    json.dump(users, file)
                self.manager.current = "reset_screen_success"
            else:
                self.ids.username_wrong.text = "Username does not exist"

class ResetScreenSuccess(Screen):
    def return_log_in(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_screen"

class MainApp(App):
    def build(self):
        return RootWidget() 

if __name__=="__main__": 
    MainApp().run() 
