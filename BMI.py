#import tkinter library
from tkinter import *
from tkinter import messagebox

'''Tkinter Entry widgets are used to display a single line text that is generally taken in the form of user Input.
We can clear the content of Entry widget by defining a method delete(0, END) which aims to clear all the content in the range.'''

def reset_entry():
    age_ab.delete(0,'end')
    height_ab.delete(0,'end')
    weight_ab.delete(0,'end')
    
#functions to display results
def calculate_bmi():
    kg = int(weight_ab.get())#gets the user weight, convert it to integers, and then stores the value in the variable kg
    m = int(height_ab.get())/100 #gets the user height, converts it into integers, divides the result with 100 so that centimeters become meters, and then stores it in a variable m.
    bmi = kg/(m*m) #bmi formula
    bmi = round(bmi, 1) #before round off the result was appearing in multiple decimal values. But after using the round function it looks simplified & easy to read.
    bmi_index(bmi) #We have called the bmi_index() function to compare the BMI value with the BMI categories.

    
#In this function, the final result displayed depending upon the BMI value & BMI category it belongs to.
def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('bmi', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('bmi', 'something went wrong!')   
        
#Create an instance of tkinter frame or window
ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x300')
ws.config(bg='blue')

'''A variable defined using IntVar() function holds integer data where we can set integer data and can retrieve it as well using 
getter and setter methods. These variables can be passed to various widget parameters, for example, the variable parameter of 
Radio Button and CheckBox Button, textvariable parameter of Label Widget, etc'''

var = IntVar()

#Tkinter frame is a top-level widget. It is placed on the parent window and is used to group other widgets.
#It improves the UI/UX of the application. Python Frames are also called panels.
frame = Frame(
    ws,
    padx=10, #The padx puts some space between the button widgets and between the closeButton and the right border of the root window.
    pady=10, #The pady puts some space between the button widgets and the borders of the frame and the borders of the root window.
    bg='skyblue'
)

#When set to true, widget expands to fill any space not otherwise used in widget's parent.
frame.pack(expand=True)

# create a Label widget
age_bc = Label(
    frame,
    text="Enter Age (2 - 120)",
    font=('Helvetica',10,'bold'),
    bg='skyblue'
)
age_bc.grid(row=1, column=1)

age_ab = Entry(
    frame, 
)
age_ab.grid(row=1, column=2, pady=5)

# create a Label widget for gender
gen_bc = Label(
    frame,
    text=' Gender',
    font=('Helvetica',10,'bold'),
     bg='skyblue'
)
gen_bc.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

#create a radio button for male
male_cd = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1,
    font=('Helvetica',10,'bold'),
     bg='skyblue'
)
male_cd.pack(side=LEFT)

#create a radio button for female
female_cd = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2,
    font=('Helvetica',10,'bold'),
     bg='skyblue'
)
female_cd.pack(side=RIGHT)

#create a lablel widget for height
height_bc = Label(
    frame,
    text="Enter Height (cm)  ",
    font=('Helvetica',10,'bold'),
     bg='skyblue'
)
height_bc.grid(row=3, column=1)

#create a lablel widget for weight
weight_bc = Label(
    frame,
    text="Enter Weight (kg)  ",
    font=('Helvetica',10,'bold'),
     bg='skyblue'

)
weight_bc.grid(row=4, column=1)

height_ab = Entry(
    frame,
)
height_ab.grid(row=3, column=2, pady=5)

weight_ab = Entry(
    frame,
)
weight_ab.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

#create buttons calculate,reset,exit

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi,
    font=('Helvetica',10,'bold'),
     bg='pink'
    
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry,
    font=('Helvetica',10,'bold'),
     bg='red'
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy(),
    font=('Helvetica',10,'bold'),
     bg='yellow'
)
exit_btn.pack(side=RIGHT)

# Start the GUI
ws.mainloop()