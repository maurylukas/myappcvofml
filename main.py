# start of imports
from kivy.app import App
from kivy.lang import Builder
# end of imports

# generating application
GUI = Builder.load_file("main.kv")

class MainApp (App):
    def build(self):
        return GUI

# running application
if __name__ == '__main__':
    MainApp ().run()
