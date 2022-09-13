import tkinter as tk
import sqlite3 as sq3
from tkinter import messagebox
from tkinter import *

conn=sq3.connect('main.db',timeout = 15) #main database
cur=conn.cursor()

global currentpoll

def vote_main(cp,un):

    username_var = un
    currentpoll = cp

    def cast_vote():
        def proceed():

            anchor = llistbox3.get(ANCHOR)

            conn=sq3.connect('main.db',timeout = 15) #main database
            cur=conn.cursor()


            cur.execute("SELECT Votes FROM PollDetails WHERE Candidate_Names = ?",(anchor,))
            conn.commit()

            vote_count = cur.fetchall()
            vote_count = vote_count[0][0]

            confirm = messagebox.askyesno("Cast your vote?","Are you sure?")
            if confirm:

                conn=sq3.connect('main.db',timeout = 15) #main database
                cur=conn.cursor()

                cur.execute("UPDATE PollDetails SET Votes = ? WHERE Candidate_Names = ?",(vote_count+1,anchor))
                conn.commit()

                messagebox.showinfo("Success","You vote has been registered!")

                cur.execute("UPDATE UserDetails SET voted = ? WHERE UserID = ?",("yes",username_var))
                conn.commit()

                messagebox.showinfo("Note","You have used your vote!.. Contact the operator if you want to reset your vote")

                cast_page.destroy()

            else:
                messagebox.showerror("Error","Please retry")

        cast_page=Toplevel()
        cast_page.geometry('700x500')
        cast_page.title('Cast your vote!')

        conn=sq3.connect('main.db',timeout = 15) #main database
        cur=conn.cursor()

        cur.execute("SELECT voted from UserDetails WHERE UserID = ?",(username_var,))
        conn.commit()

        voting_status = cur.fetchall()
        voting_status = voting_status[0][0]

        if voting_status == "yes":
            messagebox.showerror("Error","You have already voted!")
            cast_page.destroy()

        elif voting_status =="no":

                Label(cast_page,text='Enter Details',font='Helvetica 12 bold').grid(row=1,column=2)
                Label(cast_page,text='Choose the candidate: ').grid(row=2,column=1)

                llistbox3 = Listbox(cast_page)
                llistbox3.grid(row = 3,column = 2)

                cur.execute("SELECT * FROM PollDetails WHERE Poll_name = ?",(currentpoll,))
                conn.commit()
                x = cur.fetchall()
                candidate_names_arr2 = []
                for i,val in enumerate(x):
                    candidate_names_arr2.append(x[i][1])

                for i in candidate_names_arr2:
                    llistbox3.insert(END,i)

                Label(cast_page,text='Double check before casting your vote. Cannot be reversed!').grid(row=3,column=1)
                Button(cast_page,text='Proceed',command=proceed).grid(row=4,column=2)
                Label(cast_page,text="Your voting status is: ").grid(row = 7,column = 1)
                Label(cast_page,text=voting_status).grid(row = 7,column = 1)

    def poll_details():

        conn=sq3.connect('main.db',timeout = 15) #main database
        cur=conn.cursor()

        p_display_page=Toplevel()
        p_display_page.geometry('700x500')
        p_display_page.title('Current Poll details')


        Label(p_display_page,text='Current Poll Details!!',font='Helvetica 12 bold').grid(row=1,column=2)

        candidate_names_arr = []

        if currentpoll == "Default":
            messagebox.showerror("Poll Error","Poll hasn't been set up. Please contact the operator")
            p_display_page.destroy()

        else:

            cur.execute("SELECT * FROM PollDetails WHERE Poll_name  = ?",(currentpoll,))
            conn.commit()
            x = cur.fetchall()

            if x ==[]:
                pass
            else:
                for i,val in enumerate(x):
                    candidate_names_arr.append(x[i][1])

            Label(p_display_page,text='Current Poll Name: ',font='Helvetica 8 bold').grid(row=2,column=1)
            if currentpoll == None:
                Label(p_display_page,text="No polls are active",font='Helvetica').grid(row=2,column=2)

            else:
                Label(p_display_page,text=currentpoll,font='Helvetica').grid(row=2,column=2)

            Label(p_display_page,text='Candidates: ',font='Helvetica 8 bold').grid(row=3,column=1)

            for i,v in enumerate(candidate_names_arr):
                Label(p_display_page,text=candidate_names_arr[i]).grid(row=3+(i+1),column=2)

    def view_results():

        conn=sq3.connect('main.db',timeout = 15) #main database
        cur=conn.cursor()

        result_page=Toplevel()
        result_page.geometry('700x500')
        result_page.title('Voter page')

        Label(result_page,text='Results',font='Helvetica 12 bold').grid(row=1,column=2)

        cur.execute("SELECT Winner FROM Buffer WHERE Current_poll = (?)",(currentpoll,))
        conn.commit()
        temp = cur.fetchall()

        if currentpoll == "Default":
            messagebox.showerror("Poll Error","Poll hasn't been set up. Please contact the operator")
            result_page.destroy()

        else:

            if temp == "" or temp == []:
                Label(result_page,text='The poll hasnt been concluded',font='Helvetica 10 bold').grid(row=2,column=2)
                Label(result_page,text = "Current Poll",font = 8).grid(row = 3,column = 1)
                Label(result_page,text = currentpoll,font = 8).grid(row = 3,column = 2)

            else:
                temp = temp[0][0]
                Label(result_page,text='The poll has ended!',font='Helvetica 10 bold').grid(row=2,column=3)
                Label(result_page,text = "Winner",font = 8).grid(row = 3,column = 2)
                Label(result_page,text = temp,font = 8).grid(row = 3,column = 3)
                Label(result_page,text = "Poll Name",font = 8).grid(row = 4,column = 2)
                Label(result_page,text = currentpoll,font = 8).grid(row = 4,column = 3)

    voter_page=Toplevel()
    voter_page.geometry('700x500')
    voter_page.title('Voter page')

    conn=sq3.connect('main.db',timeout = 15) #main database
    cur=conn.cursor()

    cur.execute("SELECT voted from UserDetails WHERE UserID = ?",(username_var,))
    conn.commit()

    voting_status = cur.fetchall()
    voting_status = voting_status[0][0]

    global trash

    if voting_status == "yes":
        trash = "Already Voted/Time Ended"
    else:
        trash = "No votes casted yet."


    Label(voter_page,text="Your voting status is: ").grid(row = 1,column = 1)
    Label(voter_page,text=trash).grid(row = 2,column = 1)

    Label(voter_page,text = 'Menu: -->').grid(row = 3,column = 1)
    Button(voter_page,text='Cast your Vote!',command=cast_vote).grid(row=3,column=2)
    Button(voter_page,text='Current Poll details',command=poll_details).grid(row=3,column=3)
    Button(voter_page,text='View results!',command=view_results).grid(row=3,column=4)
