MessageBox
==========

The `MessageBox` widget is a widget for displaying message boxes.
These can hold a title, a message/question and buttons for choosing
alternatives. These are linked to python routines in the calling main program.
These alternatives are given as a dictionary. The dictionary keys are the labels
for the buttons while their values define the name of the routines to jump to.
If the value is an empty string "" no action is taken when this option has been
chosen. You can also define the size of the messagebox.

A typcial use case could look like this:
```import kivy
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.garden.messagebox import MessageBox

class MessageBoxApp(App):
    
    def build(self):
        return Button(text='Press for MessageBox!', on_press=self.callpopup)

    def callpopup(self, event):
        dlg = MessageBox(self, titleheader="Title Header", message="Any Message whatsoever", 
        options={"YES": "printyes()", "NO": "printno()", "CANCEL": ""}, size = (300, 300))
        print "Messagebox shows as kivy popup and we wait for the\nuser action and callback to go to either routine"

    def printyes(self):
        # routine for going yes
        print "You chose the Yes routine"

    def printno(self):
        # routine for going no
        print "You chose the No routine"

if __name__ == '__main__':
    MessageBoxApp().run()
```

