# Source Generated with Decompyle++
# File: front_apti.pyc (Python 3.10)

import tkinter as tk
from tkinter import messagebox
from pass_gen import generatePassword
mail = 'abc@gmail.com'
word = '2A4dd45'

class AptitudeSolver:
    
    def __init__(self, master):
        self.master = master
        master.title('Aptitude Solver')
        master.config(background='#ffe6f0')
        master.geometry('500x400')
        self.label = tk.Label(master, text='WELCOME TO THE APTITUDE SOLVER',font=('Arial', 14, 'bold'))
        self.label.pack(pady=20)
        self.label = tk.Label(master, text='LOGIN USING YOUR EMAIL ID AND PASSWORD',font= ('Arial', 14, 'bold'))
        self.label.pack(pady=20)
        self.email_label = tk.Label(master, text='Enter your email id:')
        self.email_label.pack()
        self.email_entry = tk.Entry(master)
        self.email_entry.pack()
        self.pass_label = tk.Label(master, text='Enter your password:')
        self.pass_label.pack()
        self.pass_entry = tk.Entry(master, show='*')
        self.pass_entry.pack()
        self.login_button = tk.Button(master, text='Login', command=self.login)
        self.login_button.pack(pady=0)
        self.sign_button = tk.Button(master, text='sign Up', command=self.signin)
        self.sign_button.pack(pady=0)
        self.quit_button = tk.Button(master, text='Quit', command=self.master.quit)
        self.quit_button.pack(pady=20)

    
    def login(self):
        if self.email_entry.get() == mail and self.pass_entry.get() == word:
            self.login_window = tk.Toplevel(self.master)
            self.login_window.title('Aptitude Solver')
            self.label = tk.Label(self.login_window, text='WELCOME TO THE APTITUDE SOLVER', font=('Arial', 14, 'bold'))
            self.label.pack(pady=20)
            self.set_theory_button = tk.Button(self.login_window, text='Set Theory', command=self.set_theory, activebackground='red', activeforeground='yellow')
            self.set_theory_button.flash()
            self.set_theory_button.pack(pady=5)
            self.ap_button = tk.Button(self.login_window, text='AP Question', command=self.ap)
            self.ap_button.pack(pady=5)
            self.gp_button = tk.Button(self.login_window, text='GP Question', command=self.gp)
            self.gp_button.pack(pady=5)
            self.hp_button = tk.Button(self.login_window, text='HP Question', command=self.hp)
            self.hp_button.pack(pady=5)
            self.perm_comb_button = tk.Button(self.login_window, text='Permutation and Combination', command=self.perm_comb)
            self.perm_comb_button.pack(pady=5)
            self.quit_button = tk.Button(self.login_window, text='Quit', command=self.master.quit)
            self.quit_button.pack(pady=20)
            return None
        else:
            messagebox.showinfo('Invalid', 'Invalid EMAIL or PASSWORD')

    
    def signin(self):
        '''self.signin_window = tk.Toplevel(self.master)
        self.signin_window.title('Sign in')
        self.label = tk.Label(self.signin_window, text='WELCOME TO THE APTITUDE SOLVER', font=('Arial', 14, 'bold'))
        self.label.pack(pady=20)
        self.label1 = tk.Label(self.signin_window, text='Sign in using your email and password', font=('Arial', 14, 'bold'))
        self.label1.pack(pady=20)
        self.email_label = tk.Label(self.signin_window, text='Enter your email id:')
        self.email_label.pack()
        self.email_entry = tk.Entry(self.signin_window)
        self.email_entry.pack()
        self.pass_label = tk.Label(self.signin_window, text='Enter your password:')
        self.pass_label.pack()
        self.pass_entry = tk.Entry(self.signin_window)
        self.pass_entry.pack()
        self.sign_button = tk.Button(self.signin_window, text='sign Up', command=self.signin)
        self.sign_button.pack(pady=0)
        self.genpass = tk.Button(self.signin_window, text='password generation', command=self.password)
        self.genpass.pack(pady=10)'''
        from registrationform1 import form
        

    
    def password(self):
        passwords = generatePassword(6)
        messagebox.showinfo('password', f'''The Password Generated is : {passwords}''')

    
    def set_theory(self):
        messagebox.showinfo('Set Theory', 'This is where you would implement the set theory functionality.')

    
    def ap(self):
        self.ap_window = tk.Toplevel(self.master)
        self.ap_window.title('AP Question')
        self.ap_label = tk.Label(self.ap_window, text='Enter the values for the AP question:')
        self.ap_label.pack(pady=10)
        self.a_label = tk.Label(self.ap_window, text='First term (a):')
        self.a_label.pack()
        self.a_entry = tk.Entry(self.ap_window)
        self.a_entry.pack()
        self.d_label = tk.Label(self.ap_window, text='Common difference (d):')
        self.d_label.pack()
        self.d_entry = tk.Entry(self.ap_window)
        self.d_entry.pack()
        self.n_label = tk.Label(self.ap_window, text='Number of terms (n):')
        self.n_label.pack()
        self.n_entry = tk.Entry(self.ap_window)
        self.n_entry.pack()
        self.l_label = tk.Label(self.ap_window, text='last term (l):')
        self.l_label.pack()
        self.l_entry = tk.Entry(self.ap_window)
        self.l_entry.pack()
        self.sum_n_terms_button = tk.Button(self.ap_window, text='Sum of n terms', command=self.sum_n_terms)
        self.sum_n_terms_button.pack(pady=10)
        self.sum_n_and_last_button = tk.Button(self.ap_window, text='Sum of n terms and last term', command=self.sum_n_and_last)
        self.sum_n_and_last_button.pack(pady=10)
        self.nth_term_button = tk.Button(self.ap_window, text='Find nth term', command=self.nth_term)
        self.nth_term_button.pack(pady=10)
        self.close_button = tk.Button(self.ap_window, text='Close', command=self.ap_window.destroy)
        self.close_button.pack(pady=20)

    
    def sum_n_terms(self):
        a = int(self.a_entry.get())
        d = int(self.d_entry.get())
        n = int(self.n_entry.get())
        sum_n=n/2*(2*a+(n-1)*d)
        messagebox.showinfo('SUM OF N TERMS OF THIS AP IS: ',sum_n)
        

    
    def sum_n_and_last(self):
        a = int(self.a_entry.get())
        l = int(self.l_entry.get())
        n = int(self.n_entry.get())
        sum_nl=n/2*(a+l)
        messagebox.showinfo('SUM OF N TERMS OF THIS AP IS: ',sum_nl)

    
    def nth_term(self):
        a = int(self.a_entry.get())
        d = int(self.d_entry.get())
        n = int(self.n_entry.get())
        nth=a+(n-1)*d
        messagebox.showinfo('Nth TERM OF THIS AP IS: ',nth)

    
    def gp(self):
        self.gp_window = tk.Toplevel(self.master)
        self.gp_window.title('GP Question')
        self.gp_label = tk.Label(self.gp_window, text='Enter the values for the GP question:')
        self.gp_label.pack(10)
        messagebox.showinfo('GP Question', 'This is where you would implement the GP question functionality.')

    
    def hp(self):
        messagebox.showinfo('HP Question', 'This is where you would implement the HP question functionality.')

    
    def perm_comb(self):
        messagebox.showinfo('Permutation and Combination', 'This is where you would implement the permutation and combination functionality.')


root = tk.Tk()
app = AptitudeSolver(root)
root.mainloop()
