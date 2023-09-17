from tkinter import *
from tkinter import Entry , Button , Frame , messagebox
import sqlite3 as sql
import pandas as pd
import random

class Main_Window:

    def __init__(self,root):
        def focus_next_entry(event):
            current_widget = event.widget

            if current_widget == Job_Entry:
                Add_Button.invoke()
            else:
                current_widget.tk_focusNext().focus()
            return "break"
        
        def Save_as_excel():
            global df
            db = sql.connect('form.db')
            query = 'select * from form'
            df = pd.read_sql_query(query,db)
            df.to_excel('sql.xlsx', sheet_name='Sheet1' , startcol=0 , startrow=0)
            db.close()
            messagebox.showinfo("save", "Saved Successfully At sql.xlsx", parent=window)
        
        def add():
            global name
            global email
            global age
            global phone
            global job
            name = Name_Entry.get()
            age = Age_Entry.get()
            email = Email_Entry.get()
            phone = Phone_Entry.get()
            job = Job_Entry.get()

            user_id = ''.join(random.choice('0123456789') for _ in range(8))
            
            db = sql.connect('form.db')
            cr = db.cursor()
            cr.execute('create table if not exists form(Id text, Name text, Email text, Age integer, Phone text, Job text)')
            cr.execute(f'INSERT INTO form (Id, Name, Email, Age, Phone, Job) VALUES ({user_id}, "{name}", "{email}", {age}, "{phone}", "{job}")')
            db.commit()
            db.close()
            
            messagebox.showinfo("Add", "Added Successfully", parent=window)
            
            Name_Entry.delete(0,END)
            Age_Entry.delete(0,END)
            Email_Entry.delete(0,END)
            Phone_Entry.delete(0,END)
            Job_Entry.delete(0,END)
            
        def clear():
            db = sql.connect('form.db')
            cr = db.cursor()
            cr.execute('DELETE FROM form;')
            db.commit()
            db.close()
            messagebox.showinfo("clear", "Database is Cleared", parent=window)
            
        def show_df(df):
            nwn = Toplevel()
            nwn.title("Form")
            nwn.iconbitmap('D:/programming/python/dataform/dataform.ico')
            scrollbar = Scrollbar(nwn)
            scrollbar.pack(side=RIGHT, fill=Y)
            text_widget = Text(nwn, yscrollcommand=scrollbar.set)
            text_widget.pack(expand=True, fill=BOTH)
            scrollbar.config(command=text_widget.yview)
            text_widget.insert(END, df.to_string(index=False))
            text_widget.configure(state='disabled')
            
        def show():
            db = sql.connect('form.db')
            query = 'select * from form'
            df = pd.read_sql_query(query,db)
            db.close()
            show_df(df)
            
        self.root = root
        self.root.title("Form")
        self.root.geometry('580x600+0+0')
        
        Main_Frame = Frame(self.root , bg='#464646' , bd=2 , relief='solid')
        Main_Frame.place(x=30 , y=25 , width=520 , height=550)
        Form_Frame = Frame(Main_Frame , background='#CECAD6' , bd=2 , relief='solid')
        Form_Frame.place(x=27 , y=150 , height=320 , width=460)
        
        Title_Label = Label(Main_Frame ,text='Data Entry Form',font=("Arial bold" , 15) ,bd=2 ,relief='solid' , fg='white',bg='#928F97' )
        Title_Label.place(x=97 , y=50 , width=300 , height=70)
        
        
        Name_Label = Label(Form_Frame , bg='#CECAD6' , text='Name: ' , font=('bold' , 12))
        Name_Label.place(x=10 , y=20)
        Name_Entry = Entry(Form_Frame )
        Name_Entry.place(x=70 , y=23 , width=350 , height=20)
        
        Email_Label = Label(Form_Frame , bg='#CECAD6' , text='Email: ' , font=('bold' , 12))
        Email_Label.place(x=10 , y=50)
        Email_Entry = Entry(Form_Frame )
        Email_Entry.place(x=70 , y=53 , width=350 , height=20)      
        
        Age_Label = Label(Form_Frame , bg='#CECAD6' , text='Age: ' , font=('bold' , 12))
        Age_Label.place(x=10 , y=80)
        Age_Entry = Entry(Form_Frame )
        Age_Entry.place(x=70 , y=83 , width=350 , height=20)
        
        Phone_Label = Label(Form_Frame , bg='#CECAD6' , text='Phone: ' , font=('bold' , 12))
        Phone_Label.place(x=10 , y=110)
        Phone_Entry = Entry(Form_Frame )
        Phone_Entry.place(x=70 , y=113 , width=350 , height=20)
        
        Job_Label = Label(Form_Frame , bg='#CECAD6' , text='Job: ' , font=('bold' , 12))
        Job_Label.place(x=10 , y=140)
        Job_Entry = Entry(Form_Frame )
        Job_Entry.place(x=70 , y=143 , width=350 , height=20)
        
        Add_Button = Button(Form_Frame , text='Add Data' , command=add)
        Add_Button.place(x=80 , y=190 , width=100 , height=40)
        Save_Button = Button(Form_Frame , text='Save as Excel' , command=Save_as_excel)
        Save_Button.place(x=240 , y=190 , width=100 , height=40)
        Clear_Button = Button(Form_Frame , text='Clear' ,command=clear)
        Clear_Button.place(x=80 , y=250 , width=100 ,height=40)
        
        Show_Button = Button(Form_Frame , text='Show' ,command=show)
        Show_Button.place(x=240 , y=250 , width=100 ,height=40)
        
        Name_Entry.bind("<Return>", focus_next_entry)
        Email_Entry.bind("<Return>", focus_next_entry)
        Age_Entry.bind("<Return>", focus_next_entry)
        Phone_Entry.bind("<Return>", focus_next_entry)
        Job_Entry.bind("<Return>", focus_next_entry)
        
        
if __name__ == "__main__":
    
    window = Tk()
    window.configure(background='#464646')
    window.iconbitmap('D:/programming/python/dataform/dataform.ico')
    app = Main_Window(window)
    window.mainloop()