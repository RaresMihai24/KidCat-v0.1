import customtkinter
from PIL import Image
import os
from functions import play_random_sfx
import pywinstyles
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
            os.path.join(current_path, "sfx", "meow_2.mp3"),
            os.path.join(current_path, "sfx", "meow_3.mp3"),
            os.path.join(current_path, "sfx", "meow_4.mp3"),
            os.path.join(current_path, "sfx", "meow_5.mp3"),
            os.path.join(current_path, "sfx", "meow_6.mp3"),
        ]

        self.bg_image = customtkinter.CTkImage(
            Image.open(current_path + "/img/background.jpg"),
            size=(self.width, self.height),
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

        self.original_image = Image.open(current_path + "/img/logo.png")
        self.ctk_image = customtkinter.CTkImage(self.original_image, size=(250, 250))

        self.image_logo = customtkinter.CTkButton(
            self,
            image=self.ctk_image,
            text="",
            fg_color="#000001",
            hover="Enable",
            corner_radius=32,
            bg_color="#000001",
            command=self.on_button_press,
        )
        self.image_logo.grid(row=0, column=0, sticky="n", padx=0, pady=25)

        pywinstyles.set_opacity(self.image_logo, value=1, color="#000001")

        self.angle = 0
        self.animating = False

    def rotate_image_smoothly(self):
        if self.angle < 360:
            self.angle += 20
            rotated_image = self.original_image.rotate(self.angle, resample=Image.BICUBIC)
            self.ctk_image = customtkinter.CTkImage(rotated_image, size=(250, 250))
            self.image_logo.configure(image=self.ctk_image)
            self.after(20, self.rotate_image_smoothly)
        else:
            self.angle = 0
            self.image_logo.configure(image=customtkinter.CTkImage(self.original_image, size=(250, 250)))
            self.animating = False

    def on_button_press(self):
        if not self.animating:
            play_random_sfx(self.sfx_list)
            self.animating = True
            self.rotate_image_smoothly()

if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.set_num_channels(20)
    channel2 = pygame.mixer.Channel(1)
    ambient_sound  = os.path.join(current_path, "sfx", "song.mp3")
    pygame.mixer.music.load(ambient_sound)
    channel2.play(pygame.mixer.Sound(ambient_sound), -1)
    channel2.set_volume(0.01)
    app = App()
    app.mainloop()
