####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
import tkinter
from my_package.analysis.visualize import plot_visualisation
from my_package.data.dataset import Dataset
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.rescale import RescaleImage
from my_package.data.transforms.rotate import RotateImage
from my_package.model import InstanceSegmentationModel
from my_package.data import dataset
from my_package.analysis import visualize
from my_package.data.transforms import flip, rescale, blur, crop, rotate
from PIL import Image,ImageTk
from msilib.schema import ComboBox
from tkinter import Button, Entry, Label, StringVar, Tk, filedialog 
from tkinter import ttk
from functools import partial
####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, dataset, segmentor):

	####### CODE REQUIRED (START) #######
	# This function should pop-up a dialog for the user to select an input image file.
    my_filetypes = [("jpeg files", '*.jpg')]
    file = fd.askopenfilename(title='Open file',initialdir='data/imgs',filetypes=my_filetypes)
    selectedimg=Image.open(file) 
	# Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
	# Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
	# Once the output is computed it should be shown automatically based on choice the dropdown button is at.
	# To have a better clarity, please check out the sample video.
    pred_boxes, pred_masks, pred_class, pred_score = segmentor(dataset[int(file[-5])]['image'])
    plot_visualisation(dataset[int(file[-5])]['image'],pred_masks,pred_boxes,pred_class,'./output/imgse.jpg','./output/imgb.jpg')
    im = Image.open(file)
    resc = RescaleImage((350, 350))
    im = resc(im)
    img = ImageTk.PhotoImage(im)
    panel = tkinter.Label(root, image = img)
    panel.image=img
    panel.grid(row=2, column=0)


	####### CODE REQUIRED (END) #######

# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):

	####### CODE REQUIRED (START) #######
	# Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
	# Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
	# Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.
    if clicked.get()=="Bounding-box":
        im = Image.open('./output/imgb.jpg')
        resc = RescaleImage((350, 350))
        im = resc(im)
        img = ImageTk.PhotoImage(im)
        panel = tkinter.Label(root, image = img)
        panel.image=img
        panel.grid(row=2, column=1)
    else:
        im = Image.open('./output/imgse.jpg')
        resc = RescaleImage((350, 350))
        im = resc(im)
        img = ImageTk.PhotoImage(im)
        panel = tkinter.Label(root, image = img)
        panel.image=img
        panel.grid(row=2, column=1)
	####### CODE REQUIRED (END) #######

# `main` function definition starts from here.
if __name__ == '__main__':

	####### CODE REQUIRED (START) ####### (2 lines)
	# Instantiate the root window.
	# Provide a title to the root window.
    root=Tk()
    root.title("PYTHON GUI")
	####### CODE REQUIRED (END) #######


	# Setting up the segmentor model.
    annotation_file = './data/annotations.jsonl'
    transforms = []

	# Instantiate the segmentor model.
    segmentor = InstanceSegmentationModel()
	# Instantiate the dataset.
    dataset = Dataset(annotation_file, transforms=transforms)

	
	# Declare the options.
    options = ["Segmentation", "Bounding-box"]
    clicked = StringVar()
    clicked.set(options[0])

    e = Entry(root, width=70)
    e.grid(row=0, column=0)

	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
    filebrowseButton = Button(root, text=" open image ", command=partial(fileClick, clicked,dataset,segmentor))
    filebrowseButton.grid(row=1, column=3)
	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button
    drop=ttk.Combobox(root,width=25,textvariable=clicked)
    drop['values']=options
    drop.grid(column=4,row=1)
  
    ####### CODE REQUIRED (END) #######
    
    # This is a `Process` button, check out the sample video to know about its functionality
    myButton = Button(root, text="Process", command=partial(process, clicked))
    myButton.grid(row=1, column=5)
    namelabel=Label(root,text="  ImageViewer ",font=("Arial Bold",10),padx=20)  
    namelabel.grid(row=0,column=0)
	
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
    root.mainloop()
	####### CODE REQUIRED (END) #######