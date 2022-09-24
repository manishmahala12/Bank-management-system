'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import tkinter as tk   # we will use tkinter library that will help us in GUI development
from tkinter import messagebox
from time import gmtime, strftime # we will use time library to get exact time 

def is_number(s):
    try:  # this will return a floating point number
        float(s)
        return 1
    except ValueError:  # this will handle value error
        return 0

def check_acc_number(num):  # in this function we will check if an account number is valid or not.
	try:   
		pin=open(num + ".txt",'r')
		
	except FileNotFoundError: #if account number is not valid then it will show this message.
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
		
	pin.close()
	return 

def home_return(master): # this function will use to take user back home or at main menu.
	master.destroy()
	Main_Menu()
	
def write(master,name,oc,pin): # this function will create an user account.
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""): #it will check if given data by user is correct or not.
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	f = open("Accnt_Record.txt",'r') # after create an account "Accnt_Record.txt" file will open.account number will increase by 1 and this account number will assign to the user
	accnt_no = int(f.readline())
	accnt_no += 1
	f.close()

	f = open("Accnt_Record.txt",'w') 
	f.write(str(accnt_no))
	f.close()

	fdet = open(str(accnt_no)+".txt","w") # this will create a file with account number and all data of user will store in it.
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')  # In this file we will store the transaction details of the user.
	frec.write("Date                             Credit      Debit     Balance\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name): #this function will show the credit amount

	if(is_number(amt)==0): #if user write the amount value incorrect then it will show error.
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet = open(accnt+".txt",'r')
	pin = fdet.readline()
	camt = int(fdet.readline())
	fdet.close()
	amt1 = int(amt)  # here users amount will update (previous amount + credited amount)
	cb = amt1 + camt
	fdet = open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n") #here we will add date ,when amount credited.
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name): # this function will show debited amount.

	if(is_number(amt)==0): #if user write the amount value incorrect then it will show error.
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):  # here we will check if debit value is greater then current balance or not.
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amt1=int(amt)  # here users amount will update (previous amount - debited amount)
		cb=camt-amt1
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n") #here we will add date ,when amount debited.
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return
		
def Cr_Amt(accnt,name): # function will display credit amount window.
    
	creditwn=tk.Tk()
	creditwn.geometry("600x300")  # define the size of window 
	creditwn.title("Credit Amount")
	creditwn.configure(bg="SteelBlue1") # give the background colour
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))  #configured the font and size of that text.
	l_title.pack(side="top")
	l1=tk.Label(creditwn,relief="raised",font=("Times",16),text="Enter Amount to be credited: ")
	e1=tk.Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(creditwn,text="Credit",font=("Times",16),relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))

def De_Amt(accnt,name): # function will display debit amount window
	debitwn=tk.Tk()
	debitwn.geometry("600x300")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(debitwn,bg="blue")
	l_title=tk.Message(debitwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(debitwn,relief="raised",font=("Times",16),text="Enter Amount to be debited: ")
	e1=tk.Entry(debitwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(debitwn,text="Debit",font=("Times",16),relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))

def disp_bal(accnt): # this function will display the function
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)

def disp_tr_his(accnt): # this function will use to display Transaction history window
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="SteelBlue1")
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History:",font=("Times",16),padx=100,pady=20,width=1000,bg="blue4",fg="SteelBlue1",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for line in frec:  #we will open the file and stores the date, time, credit, debit and balance info
		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

def logged_in_menu(accnt,name): # this function will display home page .
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("CopyAssignment Bank | Welcome - " + name)
	rootwn.configure(background='SteelBlue1')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(rootwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	label=tk.Label(text="Logged in as: "+name,relief="raised",bg="blue3",font=("Times",16),fg="white",anchor="center",justify="center")
	label.pack(side="top")
	img2=tk.PhotoImage(file="credit.gif")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="debit.gif")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="balance1.gif")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="transaction.gif")
	myimg5=img5.subsample(2,2)
	b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))  # will use this Button() widget to display 5 buttons on the window.
	b2.image=myimg2
	b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
	b3.image=myimg3
	b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
	b4.image=myimg4
	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
	b5.image=myimg5
	
	img6=tk.PhotoImage(file="logout.gif")
	myimg6=img6.subsample(2,2)
	b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
	b6.image=myimg6
	b2.place(x=100,y=150)  # use place() to place the buttons at different places.
	b3.place(x=100,y=220)
	b4.place(x=900,y=150)
	b5.place(x=900,y=220)
	b6.place(x=500,y=400)

def logout(master):  # this function will handle logout
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

def check_log_in(master,name,acc_num,pin): # this function will handle login.
	if(check_acc_nmb(acc_num)==0): # this will checks if the account number, pin and name are in the current format or not. And if wrong then takes the user to the Main menu.
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(acc_num,name)

def log_in(master): # this function will display login window.
    
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("600x300")
	loginwn.title("Log in")
	loginwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(loginwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(loginwn,text="Enter Name:",font=("Times",16),relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(loginwn)
	e1.pack(side="top")
	l2=tk.Label(loginwn,text="Enter account number:",font=("Times",16),relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(loginwn)
	e2.pack(side="top")
	l3=tk.Label(loginwn,text="Enter your PIN:",font=("Times",16),relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(loginwn,show="*")
	e3.pack(side="top")
	b=tk.Button(loginwn,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	b1=tk.Button(text="HOME",font=("Times",16),relief="raised",bg="blue4",fg="white",command=lambda: home_return(loginwn))
	b1.pack(side="top")
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))

def Create(): # this function will show create account window
	
	crwn=tk.Tk()
	crwn.geometry("600x300")
	crwn.title("Create Account")
	crwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(crwn,bg="blue")
	l_title=tk.Message(crwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(crwn,text="Enter Name:",font=("Times",16),relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(crwn)
	e1.pack(side="top")
	l2=tk.Label(crwn,text="Enter opening credit:",font=("Times",16),relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(crwn)
	e2.pack(side="top")
	l3=tk.Label(crwn,text="Enter desired PIN:",font=("Times",16),relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(crwn,show="*")
	e3.pack(side="top")
	b=tk.Button(crwn,text="Submit",font=("Times",16),command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	crwn.bind("<Return>",font=("Times",16),command=lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	return

def Main_Menu():  #this Function will display Main Menu window & call to Main Menu:
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Bank Management System - 	CopyAssignment")
	rootwn.configure(background='SteelBlue1')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(text="BANK MANAGEMENT SYSTEM ",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Verdana","40","bold"))
	l_title.pack(side="top")
	imgc1=tk.PhotoImage(file="new.gif")
	imglo=tk.PhotoImage(file="login.gif")
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)

	b1=tk.Button(image=imgc,command=Create)
	b1.image=imgc
	b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
	b2.image=imglog
	img6=tk.PhotoImage(file="quit.gif")
	myimg6=img6.subsample(2,2)

	b6=tk.Button(image=myimg6,command=rootwn.destroy)
	b6.image=myimg6
	b1.place(x=800,y=300)
	b2.place(x=800,y=200)	
	b6.place(x=920,y=400)

	rootwn.mainloop()

Main_Menu()
