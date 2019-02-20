#!/usr/bin/env python3

# Sean Reid
# Using Pillow and Tkinter to create an image manipulation GUI app
# Can roate the jpg image either 90 degree clockwise or counter-clockwise

import PIL.Image
from tkinter import filedialog
from tkinter import *


tk = Tk()
tk.title("Imagine Manipulation Application")


def main():
	label = Label(tk, text="Select an option from the menu.")
	label.pack()

	e = Entry(tk)
	e.pack()

	close_button = Button(tk, text="Close", command=tk.quit)
	close_button.pack()


	# set up our menu
	menubar = Menu(tk)

	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Load Image", command=lambda: loadImage(e))
	filemenu.add_command(label="Rotate 90 Clockwise", command=lambda: rotate90C(e))
	filemenu.add_command(label="Rotate 90 Counter-Clockwise", command=lambda: rotate90C_C(e))
	filemenu.add_command(label="Quit", command=tk.quit)
	menubar.add_cascade(label="File", menu=filemenu)

	tk.config(menu=menubar)

	tk.mainloop()


# load our image into the application
def loadImage(e):
	filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	e.insert(0, filename)

# rotate the picture 90 degrees clockwise
def rotate90C(e):
	filename = e.get()
	myImage = PIL.Image.open(filename)
	ninetyClockwise = myImage.rotate(90)
	ninetyClockwise.save('myImage90.jpg')
	ninetyClockwise.show()

# rotate the image 90 degrees counter-clockwise
def rotate90C_C(e):
	filename = e.get()
	myImage = PIL.Image.open(filename)
	ninetyCC = myImage.rotate(270)
	ninetyCC.save('myImage90CC.jpg')
	ninetyCC.show() 

def clearFrame(frame):
	for widget in frame.winfo_children():
		widget.destroy()

if __name__ == '__main__':
	main()