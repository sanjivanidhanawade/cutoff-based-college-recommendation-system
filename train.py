from subprocess import call
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from joblib import dump

root = tk.Tk()
root.title("Academic Matcher")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

image2 = Image.open('2.jpg')
image2 = image2.resize((w, h))

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

label_l2 = tk.Label(root, text="Welcome to Academic Matcher", 
                    font=("times", 30, 'bold','italic'), background="black", fg="white", 
                    width=70, height=1)
label_l2.place(x=0, y=10)

data = pd.read_csv("train.csv")
data = data.dropna()

# def Data_Preprocessing():
#     global data


#     x = data.drop(['Category'], axis=1)
#     y = data['Category']

#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10)
    
#     load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, 
#                     background="gray", foreground="white", 
#                     text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
#     load.place(x=250, y=130)

def Model_Training():
    global data
    data = pd.read_csv("train.csv")
    data = data.dropna()


    x = data.drop(['class'], axis=1)
    y = data['class']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)

    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root, text=str(repo), width=45, height=20, bg='khaki', fg='black', 
                      font=("Tempus Sanc ITC",14))
    label4.place(x=400, y=130)
    
    label5 = tk.Label(root, text="Accuracy : "+str(ACC)+"%\nModel saved as college31.joblib", 
                      width=45, height=3, bg='khaki', fg='black', 
                      font=("Tempus Sanc ITC",14))
    label5.place(x=400, y=560)
    
    dump(svcclassifier, "college31.joblib")
    print("Model saved as college31.joblib")

def Model_Training1():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    global data
    data = pd.read_csv("train.csv")
    data = data.dropna()

    x = data.drop(['class'], axis=1)
    y = data['class']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=1)
    rf_classifier.fit(x_train, y_train)

    y_pred = rf_classifier.predict(x_test)

    print("=" * 40)
    print("==========")
    print("Classification Report : ", classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    
    ACC = accuracy * 100
    repo = classification_report(y_test, y_pred)
    
    label4 = tk.Label(root, text=str(repo), width=45, height=20, bg='khaki', fg='black', 
                      font=("Tempus Sanc ITC",14))
    label4.place(x=400, y=130)
    
    label5 = tk.Label(root, text="Accuracy : "+str(ACC)+"%\nModel saved as college.joblib", 
                      width=45, height=3, bg='khaki', fg='black', 
                      font=("Tempus Sanc ITC",14))
    label5.place(x=400, y=560)
    
    dump(rf_classifier, "college.joblib")
    print("Model saved as college.joblib")
    
def Model_Training3():
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    global data
    data = pd.read_csv("train.csv")
    data = data.dropna()

    x = data.drop(['class'], axis=1)
    y = data['class']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

    dt_classifier = DecisionTreeClassifier(random_state=1)
    dt_classifier.fit(x_train, y_train)

    y_pred = dt_classifier.predict(x_test)

    print("=" * 40)
    print("==========")
    print("Classification Report : ", classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    
    ACC = accuracy * 100
    repo = classification_report(y_test, y_pred)
    
    label4 = tk.Label(root, text=str(repo), width=45, height=20, bg='khaki', fg='black', 
                      font=("Tempus Sanc ITC",14))
    label4.place(x=400, y=130)
    
    label5 = tk.Label(root, text="Accuracy : "+str(ACC)+"%\nModel saved as collegeDT.joblib", 
                      width=45, height=3, bg='khaki', fg='black', 
                      font=("Tempus Sanc ITC",14))
    label5.place(x=400, y=560)
    
    dump(dt_classifier, "collegeDT.joblib")
    print("Model saved as collegeDT.joblib")
    
    
def predication():
    call(["python", "Check_Prediction.py"])
    root.destroy()

def window():
    root.destroy()

button4 = tk.Button(root, foreground="white", background="blue", font=("Times", 14, "bold"),
                    text="Prediction", command=predication, width=20, height=2)
button4.place(x=10, y=220)

exit_button = tk.Button(root, text="Exit", command=window, width=20, height=2, 
                        font=('times', 15, ' bold '), bg="red", fg="white")
exit_button.place(x=10, y=320)

# button3 = tk.Button(root, foreground="white", background="orange", font=("Times", 14, "bold"),
#                     text="SVM", command=Model_Training, width=20, height=2)
# button3.place(x=10, y=220)

# button5 = tk.Button(root, foreground="white", background="orange", font=("Times", 14, "bold"),
#                     text="RF", command=Model_Training1, width=20, height=2)
# button5.place(x=10, y=320)

# button5 = tk.Button(root, foreground="white", background="orange", font=("Times", 14, "bold"),
#                     text="DT", command=Model_Training3, width=20, height=2)
# button5.place(x=10, y=420)

root.mainloop()
