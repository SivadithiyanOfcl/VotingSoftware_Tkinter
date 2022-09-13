from tkinter import *
import sqlite3 as sq3
from tkinter import messagebox
from exit import *

def register():

    first_name = StringVar()
    last_name = StringVar()
    vote_ID_no = StringVar()
    age = StringVar()
    gender = StringVar()
    aadhar = StringVar()
    location = StringVar()
    userID = StringVar()
    password_input = StringVar()
    password_conf = StringVar()

    def register_user():
        vo_id = "@voter"
        #Declaring variables to get the input from the respective entry function

        first = first_name.get()
        last = last_name.get()
        v_id = vote_ID_no.get()
        age_var = age.get()

        gen = gender.get()
        aa_no = aadhar.get()
        loc = location.get()
        id_var = userID.get()
        pw_var = password_input.get()
        pw_conf = password_conf.get()

        if first == "" or last =="" or v_id =="" or age_var =="" or gen =="" or aa_no =="" or loc == "":
            messagebox.showerror("Empty Field","One or more of these fields are empty.Please enter a valid entry")

        elif len(aa_no) != 16:
            messagebox.showerror("Wrong Aadhar Number","Must contain 16 digits exactly")

        elif len(age_var) > 3:
            messagebox.showerror("Wrong Age","Please share your secrets for longevity ")

        elif int(age_var) < 18:
            messagebox.showerror("Only voter above or at the age of 18 can vote!","\nYou are too young to vote, Try to enter the correct age!")

        elif vo_id not in id_var:
            messagebox.showerror("Invalid User ID","Enter a valid User ID. Please double check the details")

        elif pw_var != pw_conf:
            messagebox.showerror("Password Missmatch","Enter the same password in both fields")

        elif aa_no in a_details:
            messagebox.showerror("Duplicate Aadhar Number","This number is already registered")

        else:

        #Storing the regsiter input data into main.db unser UserDetails
            cur.execute("INSERT INTO UserDetails VALUES (?,?,?,?,?,?,?,?,?,?)",(first,last,v_id,age_var,gen,
            aa_no,loc,id_var,pw_var,"no"))
            conn.commit()

            register_page.destroy()

    register_page = Toplevel()
    register_page.resizable(False,False)
    register_page.geometry('700x500')
    register_page.title("Register")

    Label(register_page,text='Enter Details',font='Helvetica 12 bold').grid(row=1,column=2)
    Label(register_page,text='Enter First name: ').grid(row=2,column=1)
    Entry(register_page,width=30,textvariable=first_name).grid(row=2,column=2)

    Label(register_page,text='Enter Last name: ').grid(row=3,column=1)
    Entry(register_page,width=30,textvariable=last_name).grid(row=3,column=2)

    Label(register_page,text='Enter your Voter ID number(5 digits): ').grid(row=4,column=1)
    Entry(register_page,width=30,textvariable = vote_ID_no).grid(row=4,column=2)

    Label(register_page,text='Enter Age: ').grid(row=5,column=1)
    Entry(register_page,width=30,textvariable=age).grid(row=5,column=2)

    Label(register_page,text='Enter Gender: ').grid(row=6,column=1)
    Entry(register_page,width=30,textvariable=gender).grid(row=6,column=2)

    Label(register_page,text='Enter Aadhar no: ').grid(row=7,column=1)
    Entry(register_page,width=30,textvariable=aadhar).grid(row=7,column=2)

    Label(register_page,text='Enter Location: ').grid(row=8,column=1)
    Entry(register_page,width=30,textvariable=location).grid(row=8,column=2)

    Label(register_page,text='Enter a User ID: ').grid(row=9,column=1)
    Entry(register_page,width=30,textvariable=userID).grid(row=9,column=2)

    Label(register_page,text='Enter a Password: ').grid(row=10,column=1)
    Entry(register_page,width=30,textvariable=password_input).grid(row=10,column=2)

    Label(register_page,text='Confirm Password: ').grid(row=11,column=1)
    Entry(register_page,width=30,textvariable=password_conf).grid(row=11,column=2)

    Label(register_page,text='Must contain the word: @voter... Example: siva123@voter').grid(row=12,column=1)

    Button(register_page,text='Register',command=register_user).grid(row=13,column=2)

    exitButton = Button(register_page,text = "Exit",command = exit)
    exitButton.place(x=650,y=470)
