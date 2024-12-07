import customtkinter
import PIL
from PIL import Image, ImageOps, ImageDraw
import pywinstyles
import os

current_path = os.path.dirname(os.path.realpath(__file__))

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 700
        self.width = 500
        self.title("KidCat - Development - 1.0")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/img/background.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

        self.image = customtkinter.CTkImage(Image.open(current_path + "/img/logo.png"), size=(250, 250))

        self.image_logo = customtkinter.CTkButton(self, image=self.image, text="", fg_color="#000001", hover="False", corner_radius=32, bg_color="#000001") #bg_color="#000001")
        self.image_logo.grid(row=0, column=0, sticky="n", padx=0, pady=25)

        pywinstyles.set_opacity(self.image_logo, value=1, color="#000001")

if __name__ == "__main__":
    app = App()
    app.mainloop()
