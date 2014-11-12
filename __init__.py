import kivy
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App

class MessageBoxApp(App):
    
    def build(self):
        return Button(text='Press for MessageBox!', on_press=self.callpopup)

    def callpopup(self, event):
        dlg = MessageBox(self, titleheader="Title Header", message="Any Message whatsoever", options={"YES": "printyes()", "NO": "printno()", "CANCEL": ""})
        print "Messagebox shows as kivy popup and we wait for the\nuser action and callback to go to either routine"

    def printyes(self):
        # routine for going yes
        print "You chose the Yes routine"

    def printno(self):
        # routine for going no
        print "You chose the No routine"

class MessageBox(MessageBoxApp):
    def __init__(self, parent, titleheader="Title", message="Message", options={"OK": ""}, size=(400, 400)):

        def popup_callback(instance):
            "callback for button press"
            self.retvalue = instance.text
            self.popup.dismiss()

        self.parent = parent
        self.retvalue = None
        self.titleheader = titleheader
        self.message = message
        self.options = options
        self.size = size
        box = GridLayout(orientation='vertical', cols=1)
        box.add_widget(Label(text=self.message, font_size=16))
        b_list =  []
        buttonbox = BoxLayout(orientation='horizontal')
        for b in self.options:
            b_list.append(Button(text=b, size_hint=(1,.35), font_size=20))
            b_list[-1].bind(on_press=popup_callback)
            buttonbox.add_widget(b_list[-1])
        box.add_widget(buttonbox)
        self.popup = Popup(title=titleheader, content=box, size_hint=(None, None), size=self.size)
        self.popup.open()
        self.popup.bind(on_dismiss=self.OnClose)

    def OnClose(self, event):
        self.popup.unbind(on_dismiss=self.OnClose)
        self.popup.dismiss()
        if self.retvalue != None and self.options[self.retvalue] != "":
            command = "self.parent."+self.options[self.retvalue]
            exec command

if __name__ == '__main__':
    MessageBoxApp().run()