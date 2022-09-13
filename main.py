from tkinter import *
import sqlite3 as sq3
from tkinter import messagebox


#importing all the files

from exit import *
from login import *
from operatorpage import *
from register import *
from voterpage import *


#Creating the main database
conn=sq3.connect('main.db',timeout = 15) #main database
cursor=conn.cursor() #main cursor


#Creating the main page
root = Tk()
root.title("Voting")
root.geometry("700x500")
root.resizable(False,False)

#Creating global variables

global currentpoll
global username_var
global winner

#Creating a table to store all current poll data

cursor.execute("""CREATE TABLE IF NOT EXISTS CPoll (Current_poll TEXT, active TEXT)""")
conn.commit()
cursor.execute("SELECT Current_poll from CPoll WHERE active = ?",("yes",))
cp = []
cp = cursor.fetchall()
if cp =="":
    currentpoll = "No active polls"
else:
    currentpoll = cp[0][0]


#Creating a table to store poll winner list

cursor.execute("""CREATE TABLE IF NOT EXISTS WinnerList (Poll_name TEXT, Winner TEXT)""")
conn.commit()

cursor.execute("SELECT * FROM WinnerList WHERE Poll_name = ?",(currentpoll,))
win = []
win = cursor.fetchall()

if win == "" or win == "Test":
    winner = ""
else:
    winner = win[0][0]

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

#Main loop

if __name__ == "__main__":

    #create a database table
    conn=sq3.connect('main.db',timeout = 15) #main database
    cursor=conn.cursor() #main cursor

    root.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
