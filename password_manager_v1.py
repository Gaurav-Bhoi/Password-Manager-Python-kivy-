'''
Core program
started on - ???
completed on - 26 Feb 2020
created by NEXGEN
programmer - Gaurav Bhoi
'''
import os, sys
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.resources import resource_add_path, resource_find

class Popup_Window(Popup) :
    pass

class LogIn_Screen(Screen):
    password = ObjectProperty(None)
    username = ObjectProperty(None)

    def Access(self):
        if (self.username.text == str('Admin') and self.password.text == str('Sys123')) :
            self.parent.current = 'After_LogIn_Screen'
        else:
            self.username.text = ''
            self.password.text = ''

class After_LogIn_Screen(Screen) :
    files_in_boxlayout = ObjectProperty(None)
    file_name_label = ObjectProperty(None)
    file_content = ObjectProperty(None)
    save_file = ObjectProperty(None)
    file_list = os.listdir('Files')
    Window.clearcolor = (1, 1, 1, 1)

    def on_kv_post(self, base_widget):
        for items in self.file_list:
            file_name = Button(text=str(items.split('.')[0]), size_hint_y=None, height=50,
                               background_color = (0, 0, 0, 0), color = (.5, .5, 0, 1),font_size = 19 )
            self.files_in_boxlayout.add_widget(file_name)
            file_name.bind(on_release=self.Load_Files)

    def popup_window(self):
        popup = Popup_Window()
        popup.open()

    def Add_File(self, text):
        File = Button(text = text, size_hint_y=None, height=50, background_color = (0, 0, 0, 0),
                      color = (.5, .5, 0, 1), font_size = 19)
        open('Files/' + text + '.txt', 'w')
        self.files_in_boxlayout.add_widget(File)
        File.bind(on_release=self.Load_Files)

    def Load_Files(self, instance):
        self.file_name_label.text = instance.text
        file = open('Files/' + instance.text + '.txt', 'r+')
        self.file_content.text = file.read()

    def Save_File(self):
        file = open('Files/'+ self.file_name_label.text + '.txt', 'w')
        file.write(self.file_content.text)
        file.close()

class ScreenManagement(ScreenManager) :
    pass

kv_file = Builder.load_file("password_manager.kv")

class PasswordProtector(App) :
    def build(self):
        return kv_file

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    PasswordProtector().run()
