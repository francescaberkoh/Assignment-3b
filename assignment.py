'''
Created on Mar 17, 2019
Created for: ICS3U
@author: Francesca Berkoh
This is the pizza progrom
'''
#open window
from tkinter import *

root = Tk()

# create a function that when called on will calculate the subtoal, hst and final price
def calculation():
    size_input = TextBox.get() #pulls info from textboxes
    size_p = int(size_input)
    
    t_input = TextBox2.get()
    top = int(t_input)
    
    HST = 0.13
    if size_p ==1:
        subtotal = 6.00
    elif size_p == 2:
        subtotal = 10.00
    
    if top == 1:
        subtotal = subtotal + 1.00
    elif top == 2:
        subtotal = subtotal +1.75
    elif top == 3:
        subtotal = subtotal + 2.50
    elif top == 4:
        subtotal = subtotal + 3.25
        
    final_HST = HST * subtotal
    dec_hst = str("%.2f" % final_HST) #takes it to only 2 decimal places
    
    final_cost= subtotal + final_HST
    dec_cost = str("%.2f" % final_cost) 
    
    subtotal_Label = Label(root, text="Subtotal:" + " "+"$"+ str("%.2f" % subtotal))
    subtotal_Label.pack()
    
    HST_Label = Label(root, text="HST:" + " "+"$"+ dec_hst)
    HST_Label.pack()
    
    total_Label = Label(root, text="Total Cost::" + " "+"$"+ dec_cost)
    total_Label.pack()
    

#Create the widgets
Label1 = Label(root, text="Enter the size of your pizza (Small = 1) (large=2)")
Label1.pack()

TextBox = Entry(root)
TextBox.pack()

Label2 = Label(root, text="Enter the amount of toppings (max=4):")
Label2.pack()

TextBox2 = Entry(root)
TextBox2.pack()

Button1 = Button(root, text= "cost", command=calculation)
Button1.pack()
#starts the code
root.mainloop()