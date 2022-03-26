from matplotlib.figure import Figure
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image,ImageTk

win=Tk()
win.geometry('500x330')
win.title('IRIS')
win.resizable(False,False)

Label(win,text='Sepal Length').grid(row=0,column=0)
entry_sepal_length=Entry(win,width=5)
entry_sepal_length.grid(row=0,column=1) #Pack ayrildi ki get fonskiyonunu cagirabilelim!!!!!!

entry_sepal_length.focus()

Label(win,text='Sepal Width').grid(row=1,column=0)
entry_sepal_width=Entry(win,width=5)
entry_sepal_width.grid(row=1,column=1)

Label(win,text='Petal Length').grid(row=2,column=0)
entry_petal_length=Entry(win,width=5)
entry_petal_length.grid(row=2,column=1)

Label(win,text='Petal Width').grid(row=3,column=0)
entry_petal_width=Entry(win,width=5)
entry_petal_width.grid(row=3,column=1)

frame1=Frame(win,height=100,width=200)
frame1.place(x=180,y=0)
defaultt=Label(frame1,text='Type values..',font=18,bd=1)
defaultt.grid(row=0,column=0)

imgframe=Frame(win,height=100,width=200,highlightthickness=3)
imgframe.place(x=0,y=110)
img=Image.open('iris.png').resize((500,223),Image.ANTIALIAS) #imagesize 1000x447
my_img=ImageTk.PhotoImage(img)
a1=Label(imgframe,image=my_img)
a1.grid(row=0,column=0)



data=datasets.load_iris()
x=data['data']
y=data['target']
x_train,x_test,y_train,y_test=train_test_split(x,y)
df_x=pd.DataFrame(data=data['data'],columns=data['feature_names'])



def predict():
    defaultt.destroy()
    
    knn=KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train,y_train)
    
    x_predict=knn.predict([[float(entry_sepal_length.get()),float(entry_sepal_width.get()),float(entry_petal_length.get()),float(entry_petal_width.get())]])

    if x_predict==[0]:
        a=Label(frame1,text='Iris Setosa',font=18,bd=1)
        a.grid(row=0,column=0)
        

    if x_predict==1:
        b=Label(frame1,text='Iris Versicolor',font=18,bd=1)
        b.grid(row=0,column=0)

    if x_predict==2:
        c=Label(frame1,text='Iris Virginica',font=18,bd=1)
        c.grid(row=0,column=0)

    #==VALIDATION===
    validation=knn.predict(x_test)
    percentage=round(np.mean(validation==y_test)*100,2)
    
    rate=Label(frame1,text='Validation Rate: %{}'.format(percentage),font=18,bd=1)
    rate.grid(row=2,column=0)
    #==VALIDATION===

    
    def clear():
        defaultt.grid(row=0,column=0)
        if (buttonxx['text']=='Clear'):
            entry_petal_length.delete(0,'end')
            entry_petal_width.delete(0,'end')
            entry_sepal_length.delete(0,'end')
            entry_sepal_width.delete(0,'end')
            entry_sepal_length.focus()
            rate.destroy()
            buttonxx.config(text='Predict',command=predict)
            if x_predict==[0]:
                a.destroy()               
            if x_predict==[1]:
                b.destroy()
            if x_predict==[2]:
                c.destroy()
            

    buttonxx.config(text='Clear',command=clear)

def graph():
    
    sns.pairplot(df_x)
    plt.show()


buttonxx=Button(win,text='Predict',command=predict)
buttonxx.grid(row=4,column=1)

pltbuton=Button(win,text='Graph It',command=graph)
pltbuton.grid(row=4,column=0)




win.mainloop()
