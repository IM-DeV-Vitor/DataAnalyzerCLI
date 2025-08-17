from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Nenhum arquivo selecionado")
        filechooser = FileChooserListView()
        btn = Button(text="Selecionar Arquivo")

        def escolher(instance):
            if filechooser.selection:
                self.label.text = f"Selecionado: {filechooser.selection[0]}"

        btn.bind(on_press=escolher)
        layout.add_widget(filechooser)
        layout.add_widget(btn)
        layout.add_widget(self.label)
        return layout

MyApp().run()
