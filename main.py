import customtkinter
import PIL
from PIL import Image, ImageOps, ImageDraw
import pywinstyles
import os
import random
import pygame

current_path = os.path.dirname(os.path.realpath(__file__))

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 700
        self.width = 500
        self.title("KidCat - Development - 1.0")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        self.sfx_list = [
                    os.path.join(current_path, "sfx", "meow_1.mp3"),
                    os.path.join(current_path, "sfx", "meow_2.mp3"),
                    os.path.join(current_path, "sfx", "meow_3.mp3"),
                    os.path.join(current_path, "sfx", "meow_4.mp3"),
                    os.path.join(current_path, "sfx", "meow_5.mp3"),
                    os.path.join(current_path, "sfx", "meow_6.mp3")
                   ]

        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/img/background.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

        self.image = customtkinter.CTkImage(Image.open(current_path + "/img/logo.png"), size=(250, 250))

        self.image_logo = customtkinter.CTkButton(self, image=self.image, text="", fg_color="#000001", hover="Enable", corner_radius=32, bg_color="#000001", command=self.play_random_sfx) #bg_color="#000001")
        self.image_logo.grid(row=0, column=0, sticky="n", padx=0, pady=25)

        pywinstyles.set_opacity(self.image_logo, value=1, color="#000001")

    def play_random_sfx(self):
        if self.sfx_list:
            random_sfx = random.choice(self.sfx_list)
            print(f"Playing: {random_sfx}")
            pygame.mixer.init()
            pygame.mixer.music.load(random_sfx)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()

if __name__ == "__main__":
    app = App()
    app.mainloop()
