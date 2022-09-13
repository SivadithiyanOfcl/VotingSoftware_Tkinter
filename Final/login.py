import tkinter as tk
import sqlite3 as sq3
from tkinter import messagebox
from voter import *
from operator_file import *



def login(u,p,cp):
    global cursor
    global currentpoll
    global username_var
    global password_var

    username_var = u
    password_var = p
    currentpoll = cp
    #mo = "@operator"
    #pw = "operator123*"

    conn=sq3.connect('main.db',timeout = 15) #main database
    cursor=conn.cursor() #main cursor

    #Database Interactions

    '''Name of the operator details table: OperatorDetails'''

    cursor.execute('''SELECT * FROM OperatorDetails''')
    val = cursor.fetchall()
    pw = val[0][1]
    ui = val[0][0]

    cursor.execute("""SELECT UserID,Password FROM UserDetails""")
    voter_val = cursor.fetchall()

    voter_id_names = []
    voter_pw = []

    for i,name in enumerate(voter_val):
        voter_id_names.append(voter_val[i][0])
        voter_pw.append(voter_val[i][1])


    if username_var == "":
        messagebox.showerror("Empty Field","User ID field is empty")

    elif password_var == "":
        messagebox.showerror("Empty Field","Password field is empty")

    elif ui == username_var:
        if pw == password_var:
            operator_main()
        else:
            messagebox.showerror("Wrong Password","Please enter the Valid Password!")

    elif username_var in voter_id_names:

        index = voter_id_names.index(username_var)
        if password_var == voter_pw[index]:
            vote_main(currentpoll,username_var)
        else:
            messagebox.showerror("Wrong Password","Please enter the Valid Password!")
    else:
        messagebox.showerror("Invalid Entry","Enter a valid Username")
