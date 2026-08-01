from tkinter import *

######################
def Train():
    """GUI"""
    import tkinter as tk
    from tkinter import ttk
    import numpy as np
    import pandas as pd
    from PIL import Image, ImageTk
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("College Admission Prediction")
    root.configure(background="Burlywood")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    image2 = Image.open('2.jpg')
    image2 = image2.resize((w, h))

    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0)
    
    
# N - ratio of Nitrogen content in soil
# P - ratio of Phosphorous content in soil
# K - ratio of Potassium content in soil
# temperature - temperature in degree Celsius
# humidity - relative humidity in %
# ph - ph value of the soil
# rainfall - rainfall in mm

    department = IntVar()
    Year = IntVar()
    Round1 = DoubleVar()
    Round2 = DoubleVar()
    Round3 = DoubleVar()
    CET = DoubleVar()
    Round1Number = DoubleVar()
    Round2Number = DoubleVar()
    Round3Number = DoubleVar()
    

    # ===================================================================================================================

    def Detect():
        e1 = department.get()
        print(e1)
        e2 = Year.get()
        print(e2)
        e3 = Round1.get()
        print(e3)
        e4 = Round2.get()
        print(e4)
        e5 = Round3.get()
        print(e5)
        e6 = CET.get()
        print(e6)
        e7 = Round1Number.get()
        print(e7)
        e8 = Round2Number.get()
        print(e8)
        e9 = Round3Number.get()
        print(e9)
        
        #########################################################################################

        from joblib import dump, load
        a1 = load('collegeDT.joblib')
        v = a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8,e9]])
        print(v)
        if v[0]==1:
            print("IIT")
            IIT = tk.Label(root, text=" \n COEP, Pune- College Of Engineering Pune \n VJTI, Mumbai \n ICT, Mumbai- Institute Of Chemical Technology \n GHRCE, Nagpur- G.H. Raisoni College Of Engineering \n SPIT, Mumbai- Sardar Patel Institute Of Technology", background="#2F4F4F", foreground="white", font=('times', 20, ' bold '), width=50,height=10)
            IIT.place(x=400, y=500)

        elif v[0]==2:
            print("ICT")
            ICT = tk.Label(root, text="Rank 2nd \n ICT,Mumbai - Institute of Chemical Technology", background="#2F4F4F", foreground="white",font=('times', 20, ' bold '),width=50,height=10)
            ICT.place(x=400, y=500)
            
         
        elif v[0]==3:
            print("VNIT")
            VNIT = tk.Label(root, text="Rank 3rd \n VNIT,Nagpur - Visvesvaraya National Institute of Technology", background="#2F4F4F", foreground="white",font=('times', 20, ' bold '),width=50,height=10)
            VNIT.place(x=400, y=500)
            
        elif v[0]==4:
            print("AGCE")
            VNIT = tk.Label(root, text="Rank 4th \n COEP,Pune - College of Engineering Pune", background="black", foreground="#2F4F4F",font=('times', 20, ' bold '),width=50,height=10)
            VNIT.place(x=400, y=500)
            
        
        else:
            print("COEP")
            COEP = tk.Label(root, text="Rank 5th \n MIT-WPU - Maharashtra Institute of Technology \n World Peace University", background="#2F4F4F", foreground="white",font=('times', 20, ' bold '),width=50,height=10)
            COEP.place(x=400, y=500)    
            
        
               
    def window():
        root.destroy() 
              
    
    def change_button_color(event):
        event.widget.config(background="gray")  
        
   # Change the background color to gray
              
    l1 = tk.Label(root, text="department", background="Bisque", font=('times', 20, ' bold '), width=15)
    l1.place(x=500, y=100)
    Admit=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=department)
    Admit.place(x=800,y=100)

  

    # l2= tk.Label(root, text="Year", background="Bisque", font=('times', 20, ' bold '), width=15)
    # l2.place(x=500, y=150)
    # gre = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=Year)
    # gre.place(x=800, y=150)

    # l3 = tk.Label(root, text="Round1", background="Bisque", font=('times', 20, ' bold '), width=15)
    # l3.place(x=500, y=200)
    # gpa = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=Round1)
    # gpa.place(x=800, y=200)

    # l4 = tk.Label(root, text="Round2", background="Bisque",font=('times', 20, ' bold '), width=15)
    # l4.place(x=500, y=250)
    # ses = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=Round2)
    # ses.place(x=800, y=250)

    # l5 = tk.Label(root, text="Round3", background="Bisque", font=('times', 20, ' bold '), width=15)
    # l5.place(x=500, y=300)
    # Gender = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=Round3)
    # Gender.place(x=800, y=300)

    l6 = tk.Label(root, text="CET", background="Bisque", font=('times', 20, ' bold '), width=15)
    l6.place(x=500, y=150)
    Race = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=CET)
    Race.place(x=800, y=150)

    l7 = tk.Label(root, text="JEE", background="Bisque",font=('times', 20, ' bold '), width=15)
    l7.place(x=500, y=200)
    Rank = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=Round1Number)
    Rank.place(x=800, y=200)
    
    l8 = tk.Label(root, text="10thmarks", background="Bisque",font=('times', 20, ' bold '), width=15)
    l8.place(x=500, y=250)
    Rank = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=Round2Number)
    Rank.place(x=800, y=250)
    
    l8 = tk.Label(root, text="12thmarks", background="Bisque",font=('times', 20, ' bold '), width=15)
    l8.place(x=500, y=300)
    Round = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 20), textvar=Round3Number)
    Round.place(x=800, y=300)

    button1 = tk.Button(root, text="Submit", command=Detect, background="black", 
                    font=('times', 20, 'bold'), width=10, fg="white")
    button1.place(x=500, y=400)
    button1.bind("<Button-1>", change_button_color)  # Bind the button to change its color when clicked

    button2 = tk.Button(root, text="Exit", command=window, background="black", 
                        font=('times', 20, 'bold'), width=10, fg="white")
    button2.place(x=700, y=400)
    button2.bind("<Button-1>", change_button_color)  
  

    # button1 = tk.Button(root, text="Submit", command=Detect,background="black",font=('times', 20, ' bold '), width=10, fg="white")
    # button1.place(x=500, y=600)
    
    # button2 = tk.Button(root, text="Exit", command=window,background="black",font=('times', 20, ' bold '), width=10, fg="white")
    # button2.place(x=700, y=600)

    root.mainloop()


Train()
