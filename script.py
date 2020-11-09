"""
---------------------------------------------------------------
A program that stores the users appointments information:
---------------------------------------------------------------
Date,
Time,
Name,
Phone number,
About,
place 
---------------------------------------------------------------
User can:
--------------------------------------------------------------
> View all records
> Search an entry
> Add entry
> Update entry
> Delete
-------------------------------------------------------------
"""
from tkinter import *
import database

def view_all():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row) 

def search_in():
    list1.delete(0,END)
    for row in database.search(n1.get(),n2.get(),n3.get(),n4.get(),n5.get(),n6.get()):
        list1.insert(END,row)

def add_in():
    database.insert(n1.get(),n2.get(),n3.get(),n4.get(),n5.get(),n6.get())
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def select(event):
    global tup
    index=list1.curselection()[0]
    tup=list1.get(index)
    name_entry.delete(0,END)
    name_entry.insert(END,tup[1])
    about_entry.delete(0,END)
    about_entry.insert(END,tup[2])
    place_entry.delete(0,END)
    place_entry.insert(END,tup[3])
    phone_entry.delete(0,END)
    phone_entry.insert(END,tup[4])
    date_entry.delete(0,END)
    date_entry.insert(END,tup[5])
    time_entry.delete(0,END)
    time_entry.insert(END,tup[6])
    
def delete_in():

    database.delete(tup[1])
def update_in():
    
    database.update(n1.get(),n2.get(),n3.get(),n4.get(),n5.get(),n6.get())


window=Tk()

Name=Label(window,text="Name")
About=Label(window,text="About")
Place=Label(window,text="Place")
Phone=Label(window,text="Phone Number")
Date=Label(window,text="Date")
Time=Label(window,text="Time")

Name.grid(row=0,column=0,columnspan=2)
About.grid(row=2,column=0,columnspan=2)
Place.grid(row=4,column=0,columnspan=2)
Phone.grid(row=6,column=0,columnspan=2)
Date.grid(row=8,column=0,columnspan=2)
Time.grid(row=10,column=0,columnspan=2)

n1=StringVar()
name_entry=Entry(window,textvariable=n1,width=25)
name_entry.grid(row=0,column=4,columnspan=4)

n2=StringVar()
about_entry=Entry(window,textvariable=n2,width=45)
about_entry.grid(row=2,column=4,columnspan=10)

n3=StringVar()
place_entry=Entry(window,textvariable=n3,width=30)
place_entry.grid(row=4,column=4,columnspan=5)

n4=StringVar()
phone_entry=Entry(window,textvariable=n4)
phone_entry.grid(row=6,column=4,columnspan=2)

n5=StringVar()
date_entry=Entry(window,textvariable=n5)
date_entry.grid(row=8,column=4,columnspan=2)

n6=StringVar()
time_entry=Entry(window,textvariable=n6)
time_entry.grid(row=10,column=4,columnspan=1)

list1=Listbox(window,height=10,width=45)
list1.grid(row=12,column=0,columnspan=14,rowspan=11)

scroll1=Scrollbar(window)
scroll1.grid(row=12,column=12,rowspan=10)

list1.config(yscrollcommand=scroll1.set)
scroll1.config(command=list1.yview)
list1.bind('<<ListboxSelect>>',select)

b1=Button(window,text='View all',command=view_all)
b1.grid(row=12,column=14)

b2=Button(window,text='Search',command=search_in)
b2.grid(row=14,column=14)

b3=Button(window,text='Add new',command=add_in)
b3.grid(row=16,column=14)

b4=Button(window,text='Update',command=update_in)
b4.grid(row=18,column=14)

b5=Button(window,text='Delete',command=delete_in)
b5.grid(row=20,column=14)

b6=Button(window,text='Close',command=window.destroy)
b6.grid(row=22,column=14)


window.mainloop()