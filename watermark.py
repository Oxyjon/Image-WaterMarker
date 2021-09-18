from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WaterMark:
    def __init__(self):
        window = Tk()
        window.title('WaterMark Image')
        window.config(padx=50, pady=50)

        #Watermark Text
        self.watermark_input = Entry()
        self.watermark_input.grid(column=1, row=0)

        #Label
        self.watermark_text = Label(text="Watermark Text:")
        self.watermark_text.grid(column=0, row=0)

        self.success_text = Label(text='')
        self.success_text.grid(column=0, row=2, columnspan=2)
        #Buttons
        browse_btn = Button(text='Browse', command=self.browse_file)
        browse_btn.grid(column=0, row=1)

        watermark_btn = Button(text='Watermark Image', command=self.watermark_image)
        watermark_btn.grid(column=1, row=1)
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
            txt.text((250, 250), self.watermark_input.get(), font=fnt, fill=(255, 255, 255, 128))

            base_img.save(self.filename[:-4] + '-watermarked.png' )
            base_img.show()

            self.success_text.config(text='Saved into' + self.filename[:-4] + '-watermarked.png')
