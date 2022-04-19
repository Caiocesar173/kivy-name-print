from kivymd.app import MDApp as App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (.6, .7)
        self.window.pos_hint = {"center_x": .5, "center_y": .5}

        self.logo = Image(source="assets/image/logo.png")
        self.window.add_widget(self.logo)

        self.label_name = Label(text="", font_size=24, color='#ff1a1a')
        self.window.add_widget(self.label_name)
        
        self.label_type_name = Label(
            text="Digite seu nome:",
            font_size='20sp', 
            color='#00000'
        )
        
        self.window.add_widget(self.label_type_name)

        self.user = TextInput(
            multiline = False,
            padding_y = (15,15),
            size_hint = (1, .6)
            )
        self.window.add_widget(self.user)

        self.submit_btn = Button(
            text="Enviar",
            size_hint=(1,.5),
            bold=True,
            background_color="#00FFCE"
        )

        self.submit_btn.bind(on_press=self.callback)
        self.window.add_widget(self.submit_btn)
        
        return self.window


    def callback(self, event):
        username = "usuario"
        if(self.user.text is not ""):
            username = self.user.text

        self.label_name.text = "Olá, " + username + "!"
        



if __name__ == "__main__":
    SayHello().run()