import sqlite3 as sq3
from tkinter import messagebox
from tkinter import *

global currentpoll

def operator_main():

    conn=sq3.connect('main.db',timeout = 15) #main database
    cur=conn.cursor() #main cur

    def poll_creator():

        poll_name=StringVar()
        candid_name=StringVar()

        def proceed():
            p_name = poll_name.get()
            c_name = candid_name.get()

            c_name = c_name.split(",")

            cur.execute("INSERT INTO Buffer VALUES(?,?,?)",(p_name,"no","notDecided"))

            cur.execute("""CREATE TABLE IF NOT EXISTS PollDetails (Poll_name TEXT, Candidate_Names TEXT, Votes INTEGER)""")
            conn.commit()

            base_votes = 0

            for i,var in enumerate(c_name):
                cur.execute("INSERT INTO PollDetails VALUES (?,?,?)",(p_name,c_name[i],base_votes))
                conn.commit()

            cur.execute("""SELECT * FROM PollDetails""")
            #print(cur.fetchall())
            messagebox.showinfo("Success","A new poll has been created")
            poll_create.destroy()

        poll_create=Toplevel()
        poll_create.geometry('700x500')
        poll_create.title('Create a new poll')
        Label(poll_create,text='Enter Details',font='Helvetica 12 bold').grid(row=1,column=2)
        Label(poll_create,text='Enter Poll name: ').grid(row=2,column=1)
        Entry(poll_create,width=30,textvariable=poll_name).grid(row=2,column=2) #poll name
        Label(poll_create,text='(eg: General Election)').place(x=354,y=25)
        Label(poll_create,text='Enter Candidates: ').grid(row=3,column=1)
        Entry(poll_create,width=45,textvariable=candid_name).grid(row=3,column=2) #candidate name
        Label(poll_create,text='Note: Candidate names should be separated by commas').grid(row=4,column=2)
        Label(poll_create,text='eg: candidate1,candate2,candidate3....').grid(row=5,column=2)
        Button(poll_create,text='Proceed',command=proceed).grid(row=6,column=2)

    def poll_editor():

        conn=sq3.connect('main.db',timeout = 15) #main database
        cur=conn.cursor() #main cur

        def delete_poll():

            deleted_var = llistbox.get(ANCHOR)


            answer = messagebox.askyesno(title='Confirmation',
                          message='Are you sure that you want to Delete this')
            if answer:

                if deleted_var != "":

                    llistbox.delete(ANCHOR)
                    cur.execute("DELETE FROM PollDetails WHERE Poll_name = ?",(deleted_var,))
                    conn.commit()
                else:
                    pass

        def refresh():

            llistbox.delete(0,END)
            llistbox2.delete(0,END)

            cur.execute("""SELECT * FROM PollDetails""")
            conn.commit()
            x = cur.fetchall()

            poll_name_var =[]
            candidate_names_arr = []

            for i,val in enumerate(x):
                v = x[i][0]
                if v in poll_name_var:
                    pass
                else:
                    poll_name_var.append(v)
                candidate_names_arr.append(x[i][1])

            for i in poll_name_var:
                llistbox.insert(END,i)


        def delete_cand():

            del_cand = llistbox2.get(ANCHOR)
            answer = messagebox.askyesno(title='Confirmation',
                          message='Are you sure that you want to Delete this')
            if answer:
                if del_cand != "":

                    llistbox2.delete(ANCHOR)
                    cur.execute("DELETE FROM PollDetails WHERE Candidate_Names = ?",(del_cand,))
                    conn.commit()
                else:
                    pass

        def select():

            llistbox2.delete(0,END)
            candidate_names_arr3 = []

            selected_var = llistbox.get(ANCHOR)

            cur.execute("SELECT * FROM PollDetails WHERE Poll_name = (?)",(selected_var,))
            conn.commit()
            x = cur.fetchall()

            for i,val in enumerate(x):
                candidate_names_arr3.append(x[i][1])


            for i in candidate_names_arr3:
                llistbox2.insert(END,i)


        p_editor_page=Toplevel()
        p_editor_page.geometry('700x500')
        p_editor_page.title('Current Poll details')

        Label(p_editor_page,text='Current Poll Details!!',font='Helvetica 12 bold').grid(row=1,column=2)

        Button(p_editor_page,text='Select',command = select).grid(row=11,column=2)
        Button(p_editor_page,text='Delete Poll',command = delete_poll).grid(row=12,column=2)
        Button(p_editor_page,text='Delete Candidate',command = delete_cand).grid(row=11,column=3)
        Button(p_editor_page,text='Refersh',command = refresh).grid(row=12,column=3)

        cur.execute("""SELECT * FROM PollDetails""")
        conn.commit()
        x = cur.fetchall()

        poll_name_var =[]
        candidate_names_arr = []


        llistbox = Listbox(p_editor_page)
        llistbox.grid(row = 10,column = 2)

        llistbox2 = Listbox(p_editor_page)
        llistbox2.grid(row = 10,column = 3)

        for i,val in enumerate(x):
            v = x[i][0]
            if v in poll_name_var:
                pass
            else:
                poll_name_var.append(v)
            candidate_names_arr.append(x[i][1])

        for i in poll_name_var:
            llistbox.insert(END,i)

    def data_modifier():


        conn=sq3.connect('main.db',timeout = 15) #main database
        cur=conn.cursor() #main cur


        def refresh():
            voterdetails.delete(0,END)
            sv = voterlist.get(ANCHOR)
            sv = sv[0]
            cur.execute("SELECT * FROM UserDetails WHERE Voter_ID_no = (?)",(sv,))
            conn.commit()
            x = cur.fetchall()

            v = x[0]

            for i,val in enumerate(v):
                #arr.append(x[i])
                voterdetails.insert(END,v[i])

        def reset_all():

            answer = messagebox.askyesno("Confirm?","Do you want to reset votes for all users?")
            if answer:
                sql = "UPDATE UserDetails SET voted = ?"
                cur.execute(sql,("no",))
                conn.commit()
                messagebox.showinfo("Sucess","All voters can cast their votes now")

        def alter():
            alter_var = votertitles.get(ANCHOR)
            index = None
            if alter_var in titles:
                index = titles.index(alter_var)

                if alter_var == "" and alter_var not in titles :
                    messagebox.showerror("Error","Select a valid field")
                else:
                    answer = messagebox.askyesno("Confirm",f"Do you want to alter {alter_var}")

                    if answer:
                        val = alter_entry.get()
                        if val == "":
                            messagebox.showerror("Error","This field cannot be empty")
                        else:

                            if alter_var == "First_name":

                                sql = "UPDATE UserDetails SET First_name = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")


                            elif alter_var == "Last_name":

                                sql = "UPDATE UserDetails SET Last_name = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")

                            elif alter_var == "Voter_ID_no":

                                sql = "UPDATE UserDetails SET Voter_ID_no = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")

                            elif alter_var == "Age":

                                sql = "UPDATE UserDetails SET Age = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")

                            elif alter_var == "Gender":

                                sql = "UPDATE UserDetails SET Gender = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")

                            elif alter_var == "Aadhar_no":

                                sql = "UPDATE UserDetails SET Aadhar_no = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")
                            elif alter_var == "Location":

                                sql = "UPDATE UserDetails SET Location = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")

                            elif alter_var == "UserID":

                                sql = "UPDATE UserDetails SET UserID = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")

                            elif alter_var == "Password":

                                sql = "UPDATE UserDetails SET Password = ? WHERE Voter_ID_no = ?"
                                cur.execute(sql,(val,selectedvar))
                                conn.commit()
                                messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")

                            elif alter_var == "voted":
                                if val not in ["yes","no"]:
                                    messagebox.showerror("Error","Invalid Input")
                                else:
                                    sql = "UPDATE UserDetails SET voted = ? WHERE Voter_ID_no = ?"
                                    cur.execute(sql,(val,selectedvar))
                                    conn.commit()
                                    messagebox.showinfo("Sucess",f"{alter_var} was set to {val} successfully")

                            else:
                                messagebox.showerror("Error","Please contact the admin")
        def display():

            global selectedvar

            voterdetails.delete(0,END)
            selectedvar = voterlist.get(ANCHOR)
            selectedvar = selectedvar[0]
            cur.execute("SELECT * FROM UserDetails WHERE Voter_ID_no = (?)",(selectedvar,))
            conn.commit()
            x = cur.fetchall()

            v = x[0]

            for i,val in enumerate(v):
                #arr.append(x[i])
                voterdetails.insert(END,v[i])

        global alter_entry
        alter_entry = StringVar()

        data_modifier = Toplevel()
        data_modifier.geometry('700x500')
        data_modifier.title("Poll modifier")


        Label(data_modifier,text='Modify the user data',font='Helvetica 12 bold').grid(row=1,column=2)
        Button(data_modifier,text='Display',command=display).grid(row=6,column=1)
        Button(data_modifier,text='Alter',command=alter).grid(row=6,column=2)
        Button(data_modifier,text='Refresh',command=refresh).grid(row=6,column=3)

        Label(data_modifier,text="Enter the new data:").grid(row = 8,column = 1)
        Entry(data_modifier,textvariable = alter_entry,width = 20).grid(row = 8,column = 2)

        Label(data_modifier,text = "Reset everyone vote!: ").grid(row = 9,column = 1)
        Button(data_modifier,text = "Reset",command = reset_all).grid(row = 9,column = 2)




        cur.execute("""SELECT Voter_ID_no FROM UserDetails""")
        x = cur.fetchall()

        voterlist = Listbox(data_modifier)
        voterlist.grid(row = 2,column = 1)

        votertitles = Listbox(data_modifier)
        votertitles.grid(row = 2,column = 2)

        titles = ["First_name", "Last_name",
            "Voter_ID_no", "Age","Gender","Aadhar_no","Location","UserID","Password","voted"]

        for i in titles:
            votertitles.insert(END,i)

        voterdetails = Listbox(data_modifier)
        voterdetails.grid(row=2,column = 3)

        for i in x:
            voterlist.insert(END,i)

    def voters_registered():

        conn=sq3.connect('main.db',timeout = 15) #main database
        cur=conn.cursor() #main cur

        global currentpoll

        def conclude():

            conn=sq3.connect('main.db',timeout = 15) #main database
            cur=conn.cursor() #main cur

            answer = messagebox.askyesno("Conclude?","Do you want to conclude the poll")

            if answer:
                anchor = polls.get(ANCHOR)
                cur.execute("SELECT Candidate_Names from PollDetails WHERE Poll_name = ?",(anchor,))
                x = cur.fetchall()
                conn.commit()

                cur.execute("SELECT Votes from PollDetails WHERE Poll_name = ?",(anchor,))
                y = cur.fetchall()
                conn.commit()

                can_arr = []
                votes_arr = []
                for i,v in enumerate(x):
                    can_arr.append(x[i][0])
                for i,val in enumerate(y):
                    votes_arr.append(y[i][0])

                i = votes_arr.index(max(votes_arr))
                print("The Winner is:",can_arr[i])

                v = can_arr[i]

                cur.execute("UPDATE Buffer SET Winner = ? WHERE Current_poll = ?",(v,anchor))
                conn.commit()

                currentpoll = anchor

                cur.execute("SELECT Current_poll from Buffer")
                conn.commit()
                val = cur.fetchall()

                arr = []
                for i,v in enumerate(val):
                    arr.append(val[i][0])

                for i in arr:
                    cur.execute("UPDATE Buffer SET active = ? WHERE Current_poll = ?",("no",i))
                    conn.commit()

                cur.execute("UPDATE Buffer SET active = ? WHERE Current_poll = ?",("yes",anchor))
                conn.commit()

                sql = "UPDATE UserDetails SET voted = ?"
                cur.execute(sql,("yes",))
                conn.commit()
                messagebox.showinfo("Note","Voter perms from all users has been revoked")

                messagebox.showinfo("Success","The Poll has been updated")

                voters_reg.destroy()
            else:
                pass

        def display():

            candids.delete(0,END)
            votes.delete(0,END)

            anchor = polls.get(ANCHOR)
            cur.execute("SELECT Candidate_Names from PollDetails WHERE Poll_name = ?",(anchor,))
            x = cur.fetchall()
            conn.commit()

            cur.execute("SELECT Votes from PollDetails WHERE Poll_name = ?",(anchor,))
            y = cur.fetchall()
            conn.commit()

            arr = []
            votes_arr = []
            for i,v in enumerate(x):
                arr.append(x[i][0])
            for i,val in enumerate(y):
                votes_arr.append(y[i][0])
            for i in arr:
                candids.insert(END,i)
            for i in votes_arr:
                votes.insert(END,i)

        def activate():
            anchor = polls.get(ANCHOR)
            currentpoll = anchor
            cur.execute("SELECT Current_poll from Buffer")
            conn.commit()
            val = cur.fetchall()

            arr = []
            for i,v in enumerate(val):
                arr.append(val[i][0])

            for i in arr:
                cur.execute("UPDATE Buffer SET active = ? WHERE Current_poll = ?",("no",i))
                conn.commit()

            cur.execute("UPDATE Buffer SET active = ? WHERE Current_poll = ?",("yes",anchor))
            conn.commit()

            messagebox.showinfo("Success","The Poll has been updated")

        voters_reg = Toplevel()
        voters_reg.geometry('700x500')
        voters_reg.title("Voting Details")

        Label(voters_reg,text='Vote count, Poll Activation and Poll Conclusion',font='Helvetica 12 bold').grid(row=1,column=2)

        polls = Listbox(voters_reg)
        polls.grid(row=3,column = 1)

        candids = Listbox(voters_reg)
        candids.grid(row = 3,column = 2)

        votes = Listbox(voters_reg)
        votes.grid(row = 3,column = 3)

        cur.execute("""SELECT Poll_name FROM PollDetails""")
        x = cur.fetchall()

        #print(x)
        arr = []
        for i,val in enumerate(x):
            if x[i][0] not in arr:
                arr.append(x[i][0])
            else:
                pass
        #print(arr)

        for i in arr:
            polls.insert(END,i)

        Label(voters_reg,text = "Poll Name",font = 4).grid(row = 7, column = 1)
        Label(voters_reg,text = "Candidates",font = 4).grid(row = 7, column = 2)
        Label(voters_reg,text = "Votes Count",font = 4).grid(row = 7, column = 3)


        Button(voters_reg,text = "Set poll as active",command = activate).grid(row = 8,column = 1)
        Button(voters_reg,text = "Display",command = display).grid(row = 9,column = 1)
        Button(voters_reg,text = "Conclude",command = conclude).grid(row = 8,column = 3)

    op_page = Toplevel()
    op_page.geometry('700x500')
    op_page.title("Operators Only!")

    Button(op_page,text='Create a new poll!',command=poll_creator).grid(row=2,column=1)
    Button(op_page,text='Edit Poll details',command=poll_editor).grid(row=2,column=2)
    Button(op_page,text='Alter the user details',command=data_modifier).grid(row=2,column=3)
    Button(op_page,text='Voting details',command=voters_registered).grid(row=2,column=4)
