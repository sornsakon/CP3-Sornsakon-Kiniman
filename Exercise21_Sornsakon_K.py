from tkinter import *
import math

def leftClickButton(event):
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    labelBMI.configure(text="BMI : "+str(BMI))
    if BMI >= 30:
        labelResult2.configure(text="อ้วนมาก")
    elif BMI >= 25:
        labelResult2.configure(text="อ้วน")
    elif BMI >= 23:
        labelResult2.configure(text="น้ำหนักเกิน")
    elif BMI >= 18.6:
        labelResult2.configure(text="ปกติ")
    elif BMI <= 18.5:
        labelResult2.configure(text="ผอม")
MainWindow = Tk()
labelHeight = Label(MainWindow, text="Height (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow, text="Weight (kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "Compute")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelBMI = Label(MainWindow,text="BMI")
labelBMI.grid(row=2,column=1)
labelResult = Label(MainWindow,text="Result")
labelResult.grid(row=3,column=0)
labelResult2 = Label(MainWindow)
labelResult2.grid(row=3,column=1)


MainWindow.mainloop()