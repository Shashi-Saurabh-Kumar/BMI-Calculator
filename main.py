Bmi calculator 
-------------
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt

#list of data
case_data=[]
bmi_data=[]
characters=[]

def calculator():
    Height=H.get()
    Weight=W.get()
    
    #exception messages for 0 or negative values
    if Height==0 or Weight==0:
        messg.set("Height/Weight can't be 0")
        return None
        
    elif Weight<0:
        messg.set("Enter valid weight")
        return None
    
    elif Height<0:
        messg.set("Enter valid height")
        return None

    else:
        messg.set("")
        
    #exception handling for divided by 0    
    try:
        BMI=Weight/(Height*Height)
        print("Your BMI is = "+str(round(BMI,1)))
        num.set(str(round(BMI,1)))
        bmi_data.append(round(BMI,1))
        characters.append(chr(len(case_data)+97))
        if BMI<18.5:
            print("Case: Underweight")
            result.set("Underweight")
            r_output.config(foreground="#FFF",background="#00F")
            case_data.append("Underweight")            
            
        elif BMI<25 and BMI>=18.5:
            print("Case: Normal")
            result.set("Normal")
            r_output.config(foreground="#FFF",background="#0F0")
            case_data.append("Normal")

        elif BMI<30 and BMI>=25:
            print("Case: Overweight")
            result.set("Overweight")
            r_output.config(foreground="#000",background="#FF0")
            case_data.append("Overweight")

        elif BMI<35 and BMI>=30:
            print("Case: Obesity Class 1")
            result.set("Obesity Class 1")
            r_output.config(foreground="#FFF",background="#F90")
            case_data.append("Obesity Class 1")

        elif BMI<40 and BMI>=35:
            print("Case: Obesity Class 2")
            result.set("Obesity Class 2")
            r_output.config(foreground="#FFF",background="#F00")
            case_data.append("Obesity Class 2")
            
        elif BMI>=40:
            print("Case: Obesity Class 3")
            result.set("Obesity Class 3")
            r_output.config(foreground="#FFF",background="#70F")
            case_data.append("Obesity Class 3")

        else:
            print("unidentified")
            result.set("unidentified")
            
    except ZeroDivisionError:
        print("Invalid")
        
def listofbmi():
    lob=Toplevel(bmi_app)
    lob.title("BMI records")
    lob.resizable(False,False)
    lob.geometry("290x230")
    Lb=ttk.Treeview(lob)
    
    #list of previous measures
    Lb["columns"]=("BMI Value","Case")
    Lb.column("#0",width=60)
    Lb.column("Case",anchor='center', width=100)
    Lb.column("BMI Value",anchor='center', width=120)

    Lb.heading("#0",text="",anchor="w")
    Lb.heading("Case",text="Case",anchor="center")
    Lb.heading("BMI Value",text="BMI Value",anchor="center")

    for i in range(len(case_data)):
        Lb.insert(parent="",index="end",text=chr(i+97),values=(bmi_data[i],case_data[i]))

    Lb.pack()


def graph_b():
    plt.bar(characters,bmi_data,color="orange",edgecolor="black")
    plt.xlabel("Person")
    plt.ylabel("BMI Values")
    plt.grid(axis="y")
    for i in range(len(bmi_data)):
        plt.text(i,bmi_data[i],bmi_data[i])
    plt.show()


#window
bmi_app = tk.Tk()

#title
bmi_app.title("BMI Calculator")
bmi_app.geometry("260x280")
bmi_app.resizable(False,False)

#entry details
result=tk.StringVar()
num=tk.StringVar()
messg=tk.StringVar()
H=tk.DoubleVar()
W=tk.DoubleVar()

h_detail=ttk.Entry(bmi_app,textvariable = H,justify="center")
h_detail.grid(row=1,column=1,pady=5,sticky="e")

w_detail=ttk.Entry(bmi_app,textvariable = W,justify="center")
w_detail.grid(row=2,column=1,pady=5,sticky="e")

#labels
tl= ttk.Label(bmi_app, text="BMI")
tl.grid(row=0,column=1)

h_label=ttk.Label(bmi_app,text="Height (metre)")
h_label.grid(row=1,column=0,sticky="w")
w_label=ttk.Label(bmi_app,text="Weight (kg)")
w_label.grid(row=2,column=0,sticky="w")

r_label=ttk.Label(bmi_app,text="Case")
r_label.grid(row=4,column=0,sticky="e")

r_output=ttk.Label(bmi_app,text="null",textvariable=result,font=("DM sans",10,"bold"))
r_output.grid(row=4,column=1,pady=5,sticky="e")

r_num_label=ttk.Label(bmi_app,text="Value")
r_num_label.grid(row=5,column=0,sticky="e")
r_num=ttk.Label(bmi_app,text="0",textvariable=num,font=("DM sans",10,"bold"))
r_num.grid(row=5,column=1,pady=5,sticky="e")

message_label=ttk.Label(bmi_app,text="null",textvariable=messg,font=("DM sans",10,"bold"))
message_label.grid(row=8, column=1, pady=5,sticky="e")

#buttons
cal = ttk.Button(bmi_app, text="Calculate BMI", width = 20,command=calculator)
cal.grid(row=3,column=1,pady=5,sticky="e")

lbb = ttk.Button(bmi_app, text="Previous records", width = 20,command=listofbmi)
lbb.grid(row=6,column=1,pady=5,sticky="e")

graph_bmi= ttk.Button(bmi_app, text="Record graphs", width = 20,command=graph_b)
graph_bmi.grid(row=7, column=1, pady=5,sticky="e")


#run
bmi_app.mainloop()
