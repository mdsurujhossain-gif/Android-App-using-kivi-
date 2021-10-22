from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager  import ScreenManager,Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)

        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "wrong username or password"

class Rootwidget(ScreenManager):
    pass

class SignupScreen(Screen):
    def add_user(self,uname,pword):
        with open('users.json') as file:
            users = json.load(file)  
        users[uname]={'username': uname,'password':pword,'created':datetime.now().strftime('%Y-%m-%d %H-%M-%S')}
        
        with open('users.json','w') as file:
            json.dump(users,file)
        self.manager.current = "sign_up_screen_success"

class SignupScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'

        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    pass


class Mainapp(App):
    def build(self):
        return Rootwidget()


if __name__ == "__main__":
    Mainapp().run()