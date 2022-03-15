# start of imports
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard
from mycv import screens
from mycv import buttons
#import certifi
#import os
# end of imports

# generating application
#os.environ['SSL_CERT_FILE'] = certifi.where()
GUI = Builder.load_file("mycv/main.kv")

class MainApp (App):
    def build(self):
        self.icon = "mycv/img/luna.png"
        #Window.size = (360,800)
        return GUI

    def on_start(self):
        Window.bind (on_keyboard = self.voltar)

    def voltar (self, window, key, *args):
        if key == 27:
            if self.root.ids ["manager"].current_screen.name == "home":
                return False
            elif self.root.ids ["manager"].current_screen.name in ("resume", "projects"):
                self.root.ids ["manager"].current = "home"
                self.root.ids ["titulo"].text = "A little bit about me"
                return True
            else:
                self.root.ids ["manager"].current = "projects"
                self.nomear (id)
                return True

    def alternar (self, id):
        self.root.ids ["manager"].current = id
        self.nomear (id)

    def nomear (self, id):
        self.root.ids ["titulo"].text = str (self.root.ids ["manager"].current).title()

    def copiar (self):
        self.email = "maurylukas@yahoo.com"
        Clipboard.copy (self.email)
        Popup (title = "", content = Label (text = "E-mail copied to clipboard:\n\n" + self.email + "\n\nClick anywhere else to close", halign = "center"),
               size_hint = (0.3, 0.3), background_color = (0, 0, 0, 0), separator_color = (0, 0, 0, 0)).open ()


# running application
if __name__ == '__main__':
    MainApp ().run()
