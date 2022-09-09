from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

from middleware_grpc import runGRPCMethod

class LoginController():
    def __init__(self, **kwargs):
        super(LoginController, self).__init__(**kwargs)
        
    def on_login_pressed(self, username, password, callback):
        if True:
            userData = {
                "username": username, 
                "password": password
            }
            res = runGRPCMethod( 'login', userData)
            if(res.statusCode == 400):
                return Snackbar(text=res.message, bg_color=(1, 0, 0, 1),).open()
            callback(self, user_id=res.id)
            MDApp.get_running_app().root.transition.direction = 'left'
            MDApp.get_running_app().root.current = "Home"
    
    def on_register_pressed(self):
        MDApp.get_running_app().root.transition.direction = 'left'
        MDApp.get_running_app().root.current = "Register"