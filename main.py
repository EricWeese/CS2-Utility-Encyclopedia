import tkinter as tk
from PIL import Image, ImageTk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # set the window size and title
        self.geometry("1920x1080")
        self.title("Image Viewer")

        # create a list of image filenames
        self.image_filenames = [
            "image1.png",
            "image2.png",
            "image3.png",
            "image4.png"
        ]

        # create the images
        self.images = []
        for filename in self.image_filenames:
            image = Image.open(filename).resize((128, 128))
            image = ImageTk.PhotoImage(image)
            self.images.append(image)

        # create the image labels
        self.image_labels = []
        for i, image in enumerate(self.images):
            label = tk.Label(self, image=image, bg="black")
            label.image = image
            label.bind("<Button-1>", lambda event,
                       index=i: self.show_screen2(index))
            self.image_labels.append(label)

        # position the image labels in a grid
        for i, label in enumerate(self.image_labels):
            row = i // 2
            column = i % 2
            padx = pady = 50
            label.grid(row=row, column=column, padx=padx, pady=pady)

        # create the screen 2 label
        self.screen2_label = tk.Label(self, text="", font=("Arial", 40))

    def show_screen2(self, index):
        # hide the image labels
        for label in self.image_labels:
            label.grid_forget()

        # show the screen 2 label with the screen number
        self.screen2_label.config(text=f"Screen {index+1}")
        self.screen2_label.grid(row=0, column=0, sticky="nsew")


app = Application()
app.mainloop()
