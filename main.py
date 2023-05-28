# import kivy
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from pytube import YouTube
from kivy.uix.button import Button

class YouDownloader(App):
    def build(self):
        self.icon = "download.png"
        self.text = ["YouTubeDownloader"]
        app_layout = BoxLayout(orientation = "vertical")
        self.t = TextInput(font_size = 30, size_hint_y = None, height = 60)
        app_layout.add_widget(self.t)

        self.label_out = Label(text="Check Resolution before download",font_size=20)
        # label_out.bind()
        app_layout.add_widget(self.label_out)

        buttons = [
            ["mp3","360p","720p"],
            ["1080p","Max","Clear"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text= label, font_size=30,background_color="gray",
                                pos_hint={"center_x":0.5,"center_y":0.5},)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            app_layout.add_widget(h_layout)

        download_button = Button(text = "Download", font_size=40,background_color="gray",
                                 pos_hint={"center_x":0.5,"center_y":0.5},)
        download_button.bind(on_press=self.loading)
        app_layout.add_widget(download_button)

        return app_layout

    def on_button_press(self, instance):
        global button_text
        button_text = instance.text
        if button_text == "Delete":
            self.t.text = ""
        self.label_out.text = button_text

    def loading(self, instance):
        url = self.t.text
        yt = YouTube(url)
        try:
            if button_text == "mp3":
                yt.streams.filter(abr="160kbps", progressive=False).first().download(filename=yt.title+".mp3")
                self.t.text = yt.title + " Successfully."

            elif button_text == "Max":
                # self.t.text = ""
                # self.t.text = "Highest resolution Downloading..."
                yt.streams.get_highest_resolution().download()
                self.t.text = button_text + " successfully."

            else:
                yt.streams.filter(res=button_text).first().download()
                self.t.text = button_text + " successfully."
        except Exception as e:
            self.t.text = "Plz Check Resolution on Youtube before Download"

if __name__ == '__main__':
    YouDownloader().run()