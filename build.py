from tkinter import *
from functionality import ButtonFunctionality

class Build:
    def __init__(self):
        self.root = Tk()
        self.title = self.root.title('Image Resizer')


    def label_entry(self, labelText):
        label = Label()
        label.config(text=labelText)
        label.pack()

        entry = Entry()
        entry.pack()


        return entry



    def build_page(self):
        imgPath =  self.label_entry('Image Path')

        newImgPath = self.label_entry('New Image Path')

        xSize = self.label_entry('X:')

        ySize = self.label_entry('Y:')



        enterBtn = Button()
        enterBtn.config(text='Resize', command=lambda: ButtonFunctionality.enter_btn_functionality(ButtonFunctionality.create_size_tuple(xSize.get(), ySize.get()), imgPath.get(), newImgPath.get()))
        enterBtn.pack()

        self.root.mainloop()



