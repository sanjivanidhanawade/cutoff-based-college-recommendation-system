
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="skyblue")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("College Admission Prediction")
video_label =tk.Label(root)
video_label.pack()
#read video to display on label
player = tkvideo("y.mp4", video_label,loop = 1, size = (w, h))
player.play()

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('7.jpg')
# image2 = image2.resize((1370, 650), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=85)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="ACADEMIC MATCHER- THE COLLEGE PREDICTOR",font=("Times New Roman", 25, 'bold'),
                    background="black", fg="white", width=45, height=1)
label_l1.place(x=2, y=20)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=9, height=1,font=('times', 15, ' bold '), bg="skyblue", fg="white")
button1.place(x=900, y=20)

button2 = tk.Button(root, text="Register",command=reg,width=9, height=1,font=('times', 15, ' bold '), bg="skyblue", fg="white")
button2.place(x=1050, y=20)

button3 = tk.Button(root, text="Exit",command=window,width=9, height=1,font=('times', 15, ' bold '), bg="black", fg="white")
button3.place(x=1200, y=20)

root.mainloop()