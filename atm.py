import random
import json
from tkinter import *

# -------------------- LOAD & SAVE --------------------

def load_data():
    global acc_details
    try:
        with open("accounts.json", "r") as file:
            acc_details = json.load(file)
            acc_details = {int(k): v for k, v in acc_details.items()}
    except:
        acc_details = {}

def save_data():
    with open("accounts.json", "w") as file:
        json.dump(acc_details, file, indent=4)

# -------------------- ACCOUNT FUNCTIONS --------------------

def create_acc():
    for widget in root.winfo_children():
        widget.destroy()

    while True:
        acc_no_generated = random.randint(10000, 99999)
        if acc_no_generated not in acc_details:
            break
    
    l1=Label(root, text="Enter the Details ",fg="blue", font=("Arial", 30, "bold","italic"))
    l1.place(x=600, y=100)

    def for_submit_button_for_name_password():
        acc_details[acc_no_generated] = {
            "name": name.get(),
            "password": int(password_.get()),
            "money": 0
        }

        save_data()
        l3=Label(root, text="Your account is created successfully",fg="blue", font=("Arial", 18, "bold"))
        l2=Label(root, text=f"Your account number is :{acc_no_generated}",fg="blue", font=("Arial", 18, "bold"))
        l2.place(x=560, y=400)
        l3.place(x=540, y=450)


    name_lable=Label(root,text="Enter your name : ")
    name_lable.place(x=610, y=200)
    name=Entry(root)
    name.place(x=710, y=201)

    password_lable=Label(root,text="Enter your pin : ")
    password_lable.place(x=620, y=250)
    password_=Entry(root)
    password_.place(x=710, y=251)
    
    btn2=Button(root, text="Submit", command=for_submit_button_for_name_password , bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    btn2.place(x=820, y=300)

    back_btn=Button(root, text="Back", command=welcome_page , bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    back_btn.place(x=400, y=70)


def view_acc():
    for widget in root.winfo_children():
        widget.destroy()

    l1=Label(root, text="Enter the Details of your Account ",fg="blue", font=("Arial", 30, "bold","italic"))
    l1.place(x=450, y=100)

    def matching_accountno_password():
        passw_text=passw_.get()
        acc_no_text=acc_no_.get()
        acc_no = int(acc_no_text)
        passw = int(passw_text)
        if acc_no in acc_details:
            if passw == acc_details[acc_no]["password"]:
                for_changing_in_acc(acc_no)
            else:
                l3=Label(root, text="Invalid password",fg="blue", font=("Arial", 18, "bold"),)
                l3.place(x=560, y=400)
        else:
            l3=Label(root, text="Your account not found",fg="blue", font=("Arial", 18, "bold"))
            l3.place(x=560, y=400)


    acc_no_lable=Label(root,text="Enter your account number : ")
    acc_no_lable.place(x=550, y=200)
    acc_no_=Entry(root)
    acc_no_.place(x=710, y=201)

    # acc_no = int(input("Enter your account number: "))
    password_check_label=Label(root,text="Enter your pin : ")
    password_check_label.place(x=620, y=250)
    passw_=Entry(root)
    passw_.place(x=710, y=251)

    btn4=Button(root,text="Submit",command=matching_accountno_password ,bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    btn4.place(x=820, y=300)

    back_btn=Button(root, text="Back", command=welcome_page , bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    back_btn.place(x=400, y=70)


# -------------------- TRANSACTION MENU --------------------

def for_changing_in_acc(acc_no):
    for widget in root.winfo_children():
        widget.destroy()

    wel_label=Label(root, text=f"Welcome Mr.{acc_details[acc_no]['name']}",fg="blue", font=("Arial", 35, "bold"))
    wel_label.place(x=540, y=200)

    btn5 = Button(root, text="Check Balance", command=lambda: check_balance(acc_no), bg="#1f76c9",fg="white",font=("Arial", 20, "bold"))
    btn5.place(x=650, y=400)

    btn6 = Button(root, text="Deposit", command=lambda: deposit(acc_no), bg="#1f76c9",fg="white",font=("Arial", 20, "bold"))
    btn6.place(x=1000, y=400)

    btn7 = Button(root, text="Withdraw", command=lambda: withdraw(acc_no), bg="#1f76c9",fg="white",font=("Arial", 20, "bold"))
    btn7.place(x=360, y=400)

    back_btn=Button(root, text="Log Out", command=view_acc , bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    back_btn.place(x=400, y=70)


# -------------------- TRANSACTIONS --------------------

def deposit(acc_no):
    for widget in root.winfo_children():
        widget.destroy()

    def add():
        money=int(money_.get())
        acc_details[acc_no]["money"] += money
        save_data()
        l4=Label(root,text=f"Successfully deposite the amount of {money}",fg="blue", font=("Arial", 25, "bold"))
        l4.place(x=450, y=350)

    money_lable=Label(root,text="Enter your amount : ")
    money_lable.place(x=550, y=200)
    money_=Entry(root)
    money_.place(x=710, y=200)

    btn = Button(root, text="Deposit", command=add,bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    btn.place(x=800,y=250)

    back_btn=Button(root, text="Back",  command=lambda: for_changing_in_acc(acc_no), bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    back_btn.place(x=400, y=70)


def withdraw(acc_no):
    for widget in root.winfo_children():
        widget.destroy()

    def add():
        money=int(money_.get())
        acc_details[acc_no]["money"] -= money
        save_data()
        l4=Label(root,text=f"Successfully withdraw the amount of {money}",fg="blue", font=("Arial", 25, "bold"))
        l4.place(x=450, y=350)

    money_lable=Label(root,text="Enter your amount : ")
    money_lable.place(x=550, y=200)
    money_=Entry(root)
    money_.place(x=710, y=200)

    btn = Button(root, text="Withdraw", command=add,bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    btn.place(x=800,y=250)

    back_btn=Button(root, text="Back",  command=lambda: for_changing_in_acc(acc_no), bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    back_btn.place(x=400, y=70)


def check_balance(acc_no):
    for widget in root.winfo_children():
        widget.destroy()

    balance = acc_details[acc_no]["money"]

    l = Label(root, text=f"Your current balance is: {balance}",fg="blue", font=("Arial", 35, "bold"))
    l.place(x=450, y=200)

    back_btn=Button(root, text="Back",  command=lambda: for_changing_in_acc(acc_no), bg="#1f76c9",fg="white" , font=("Arial", 10, "bold"))
    back_btn.place(x=400, y=70)


load_data()


# -------------------------tkinter--------------------------------

# root created

root=Tk()
root.title("IRON BANK")
root.state("zoomed")


# WELCOME PAGE
def welcome_page(): 
    for widget in root.winfo_children():
        widget.destroy()
    
    l1=Label(root, text="Welcome to Iron Bank",fg="blue", font=("Arial", 60, "bold","italic"))
    l1.place(x=370, y=100)

    btn1=Button(root, text="Create Account", bg="#1f76c9",fg="white", command=create_acc,font=("Arial", 20, "bold"))
    btn1.place(x=440, y=400)
    l6=Label(root, text="Create new account",)
    l6.place(x=495, y=470)

    btn2=Button(root, text="Login into account", bg="#1f76c9",fg="white", command=view_acc,font=("Arial", 20, "bold"))
    btn2.place(x=900, y=400)
    l5=Label(root, text="Login into existing account",)
    l5.place(x=965, y=470)


welcome_page()
root.mainloop()
