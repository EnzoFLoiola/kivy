from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout  
from kivy.lang import Builder

class ToDoApp(App):
    def build(self):
        return Builder.load_file("layout.kv")

    def add_task(self, instance=None):
        task_text = self.root.ids.input_text.text.strip()
        if task_text:
            task_layout = self.root.ids.task_list 


            task_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)

            check = CheckBox()
            task_label = Label(text=task_text, font_size=18, halign='left', valign='middle')
            task_label.bind(size=task_label.setter('text_size')) 

            task_box.add_widget(check)
            task_box.add_widget(task_label)


            task_layout.add_widget(task_box)

            self.root.ids.input_text.text = ""

ToDoApp().run()









