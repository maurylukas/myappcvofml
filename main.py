# start of imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
# end of imports

# generating screens
class Home (Screen):
    pass
class Resume (Screen):
    pass
class Projects (Screen):
    pass

# generating application
GUI = Builder.load_file("main.kv")

class MainApp (App):
    def build(self):
        return GUI

    def on_start(self):
        Window.bind (on_keyboard = self.voltar)

    def voltar (self, window, key, *args):
        if key == 27:
            if self.root.ids ["manager"].current_screen.name == "home":
                return False
            elif self.root.ids ["manager"].current_screen.name == "resume" or "projects":
                self.root.ids ["manager"].current = "home"
                return True
            else:
                self.root.ids ["manager"].current = "projects"
                return True

    def alternar (self, id):
        self.root.ids ["manager"].current = id


# running application
if __name__ == '__main__':
    MainApp ().run()
