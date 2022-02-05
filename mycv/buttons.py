# start of imports
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
# end of imports


# clickable image
class ImageButton(ButtonBehavior, Image):
    pass

# clickable label
class LabelButton(ButtonBehavior, Label):
    pass