from tkinter import *
import tkinter.messagebox
from pass_gen import generatePassword
root = Tk()

class form:
    def __init__(self,master):
        self.master=master
        master.title('Registration Form')
        master.config(background='#ffe6f0')
        master.geometry('500x500')
        self.fn = StringVar()
        self.ln = StringVar()
        self.dob = StringVar()
        self.var = StringVar()
        self.email = StringVar()
        self.passw= StringVar()
        self.var_c1 = 'Java'
        self.var_c2 = 'Python'
        self.var_c3 = 'C++'
        self.radio_var = StringVar()

        heading = Label(master, text='Registration Form', relief=SOLID, width=20, font='arial 19 bold', fg='#b30047', bg='#ffe6f0')
        heading.place(x=90, y=10)

        fname = Label(master, text="FirstName :",width=20,font=("bold", 10),bg='#ffe6f0')
        fname.place(x=80,y=70)
        efname =Entry(master,textvar=self.fn)
        efname.place(x=240,y=70)

        lname = Label(master, text="LastName :",width=20,font=("bold", 10),bg='#ffe6f0')
        lname.place(x=80,y=110)
        elname = Entry(master,textvar=self.ln)
        elname.place(x=240,y=110)
        date = Label(master, text="DOB :",width=20,font=("bold", 10),bg='#ffe6f0')
        date.place(x=80,y=140)
        edob = Entry(master,textvar=self.dob)
        edob.place(x=240,y=140)
        email=Label(master, text="Email :",width=20,font=("bold", 10),bg='#ffe6f0')
        email.place(x=80,y=170)
        em = Entry(master,textvar=self.email)
        em.place(x=240,y=170)
        password=Label(master, text="Password :",width=20,font=("bold", 10),bg='#ffe6f0')
        password.place(x=80,y=320)
        ps = Entry(master,textvar=self.passw)
        ps.place(x=240,y=320)
        

        Country = Label(master, text="Country :",width=20,font=("bold", 10),bg='#ffe6f0')
        Country.place(x=75,y=200)

        List=["Nepal","India",'America','China',"Canada",'Japan','South Africa']
        droplist=OptionMenu(master,self.var,*List)
        self.var.set("Select Country")
        droplist.config(width=15)
        droplist.place(x=238,y=200)
        Lang = Label(master, text="Prog Language :",width=20,font=("bold", 10),bg='#ffe6f0')
        Lang.place(x=95,y=240) 

        c1 = Checkbutton(master, text="java", variable=self.var_c1).place(x=235,y=240)  
        c2 = Checkbutton(master, text="python", variable=self.var_c2).place(x=290,y=240)  
        c3 = Checkbutton(master, text='C++', variable=self.var_c3).place(x =350, y=240)
        Gender = Label(master, text="Gender :",width=20,font=("bold", 10),bg='#ffe6f0')
        Gender.place(x=73,y=290)

        r1=Radiobutton(master, text="Male", variable=self.radio_var, value="Male").place(x=230,y=290)  
        r2=Radiobutton(master, text="Female", variable=self.radio_var, value="Female").place(x=290,y=290) 


        genpass = Button(master, text='password generation', command=self.password)
        genpass.place(x=200,y=360)
        
        Submit=Button(master, text='Submit',width=12,bg='#ff4d94',fg='white',command=self.printent)
        Submit.place(x=130,y=400)
        quit=Button(master, text='Quit',width=12,bg='#ff4d94',fg='white',command=exit).place(x=280,y=400)
    

    def password(self):
        passwords = generatePassword(6)
        tkinter.messagebox.showinfo('password', f'''The Password Generated is : {passwords}''')

    def printent(self):
        first = self.fn.get()
        second = self.ln.get()
        dob1 = self.dob.get()
        var1 = self.var.get()
        var3 = self.var_c1
        var3 = self.var_c2 
        var3 = self.var_c3
        var4  = self.radio_var.get()

        print(f'The full name is {first} {second}')
        print(f'Your age is {dob1}')
        print(f'Your country is {var1}')
        print(f'Your selected programming language is {var3}')
        print(f'Your gender is {var4}')
        tkinter.messagebox.showinfo('Congratulations!!', 'User has successfully signed up!')
        


app=form(root)
root.mainloop()
