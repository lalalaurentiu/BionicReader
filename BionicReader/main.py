from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import kivy.properties as prop
from kivy.uix.popup import Popup

import os

class LoadDialog(FloatLayout):
    load = prop.ObjectProperty(None)
    cancel = prop.ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = prop.ObjectProperty(None)
    text_input = prop.ObjectProperty(None)
    cancel = prop.ObjectProperty(None)

class mainBox(BoxLayout):
    loadfile = prop.ObjectProperty(None)
    savefile = prop.ObjectProperty(None)
    text_input = prop.StringProperty('')
    
    def __init__ (self, **kwargs):
        super(mainBox, self).__init__(**kwargs)
        Window.bind(on_dropfile=self.on_drop_file)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Incarca un Fisier", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        from utility import refactoring
        print(path, filename)
        
        with open(os.path.join(path, filename[0])) as stream:
            doc = stream.read()

        lst = doc.splitlines()
        for line in lst:
            self.text_input += refactoring(line) + "\n"

        self.dismiss_popup()

    def on_drop_file(self,window, file_path):
        from utility import refactoring
        with open(file_path) as stream:
            doc = stream.read()

        lst = doc.splitlines()
        for line in lst:
            self.text_input += refactoring(line) + "\n"
            print(self.text_input)

class BioReaderApp(App):
   pass

if __name__ == '__main__':
    BioReaderApp().run()