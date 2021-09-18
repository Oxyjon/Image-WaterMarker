from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class WaterMark:
    def __init__(self):
        window = Tk()
        window.title('WaterMark Image')
        window.config(padx=50, pady=50)

        #Watermark Text
        self.watermark_text = Entry()
        self.watermark_text.pack()

        # Canvas
        canvas = Canvas(width=400, height=400)
        canvas.pack()
        #Buttons
        browse_btn = Button(text='Browse', command=self.browse_file)
        browse_btn.pack()

        watermark_btn = Button(text='Watermark Image', command=self.watermark_image)
        watermark_btn.pack()
        window.mainloop()


    def browse_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=[
                                                  ("image", ".jpeg"),
                                                  ("image", ".png"),
                                                  ("image", ".jpg"),
                                              ])

    def watermark_image(self):
        # Open Image
        with Image.open(self.filename).convert("RGBA") as base_img:
            # get a font
            fnt = ImageFont.truetype("arial.ttf", 255)
            # Makes the image drawable
            txt = ImageDraw.Draw(base_img)

            # draw text, half opacity
            txt.text((250, 250), self.watermark_text.get(), font=fnt, fill=(255, 255, 255, 128))

            base_img.save(self.filename[:-4] + '-watermarked.png' )
            base_img.show()
