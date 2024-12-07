import customtkinter
import PIL
from PIL import Image, ImageOps, ImageDraw
import pywinstyles
import os

current_path = os.path.dirname(os.path.realpath(__file__))

def crop_circle(image_path, size):
    img = Image.open(image_path).convert("RGBA")
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)
    circular_image = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    circular_image.putalpha(mask)
    return circular_image.resize(size, Image.LANCZOS)


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

        circular_logo = crop_circle(current_path + "/img/logo.jpeg", (250, 250))
        self.image = customtkinter.CTkImage(light_image=circular_logo, size=(250, 250))

        self.image_label = customtkinter.CTkLabel(self, image=self.image, text="", bg_color="#000001")
        self.image_label.grid(row=0, column=0, sticky="n", padx=0, pady=25)

        pywinstyles.set_opacity(self.image_label, value=1, color="#000001")

if __name__ == "__main__":
    app = App()
    app.mainloop()