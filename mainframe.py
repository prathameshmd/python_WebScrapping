import tkinter
from tkinter import *
from tkinter import messagebox


root = tkinter.Tk()
root.resizable(0,0)

root.title("Calculator")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 250
h = 400
x = int(ws/2 - w/2)
y = int(hs/2 - h/2)
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

data = StringVar()
A = 0
val = ""
operator = ""

def btn1_isclicked():
      global val
      val = val + "1"
      data.set(val)
def btn2_isclicked():
      global val
      val = val + "2"
      data.set(val)
def btn3_isclicked():
      global val
      val = val + "3"
      data.set(val)            
def btn4_isclicked():
      global val
      val = val + "4"
      data.set(val)

def btn5_isclicked():
      global val
      val = val + "5"
      data.set(val)

def btn6_isclicked():
      global val
      val = val + "6"
      data.set(val)

def btn7_isclicked():
      global val
      val = val + "7"
      data.set(val)

def btn8_isclicked():
      global val
      val = val + "8"
      data.set(val)

def btn9_isclicked():
      global val
      val = val + "9"
      data.set(val)

def btn0_isclicked():
      global val
      val = val + "0"
      data.set(val)

def btn_plusclicked():
      global A
      global val
      global operator
      A = int(val)
      operator = "+"
      val = val + "+"
      data.set(val)

def btn_subclicked():
      global A
      global val
      global operator
      A = int(val)
      operator = "-"
      val = val + "-"
      data.set(val)

def btn_mulclicked():
      global A
      global val
      global operator
      A = int(val)
      operator = "*"
      val = val + "x"
      data.set(val)

def btn_divclicked():
      global A
      global val
      global operator
      A = int(val)
      operator = "/"
      val = val + "/"
      data.set(val)

def c_pressed():
      global val
      global A
      global operator
      val = ""
      A = 0
      opertor = ""
      data.set(val)     

def result():
      global val
      global A
      global operator
      val2 = val
      if operator == "+":
            x = int((val2.split("+")[1]))
            c = A + x
            data.set(c)
            val = str(c)
      elif operator == "-":
            x = int((val2.split("-")[1]))
            c = A - x
            data.set(c)
            val = str(c)
      elif operator == "*":
            x = int((val2.split("x")[1]))
            c = A * x
            data.set(c)
            val = str(c)
      elif operator == "/":
            x = int((val2.split("/")[1]))
            if x == 0:
                  messagebox.showerror("Error","Not Allowed !! Infinity")
                  val = ""
                  A = 0
                  data.set(val)
            else:
                  c = int(A / x)
                  data.set(c)
                  val = str(c)      




lbl = Label(
      root,
      text = "Label",
      font = ("Verdana",20),
      anchor = SE,
      textvariable = data,
      background = "#ffffff",
      fg = "#000000"
)
lbl.pack(expan = True, fill = "both")


butnrow1 = Frame(root,bg="#000000")
butnrow1.pack(expand = True, fill = "both")

butnrow2 = Frame(root)
butnrow2.pack(expand = True, fill = "both")

butnrow3 = Frame(root)
butnrow3.pack(expand = True, fill = "both")

butnrow4 = Frame(root)
butnrow4.pack(expand = True, fill = "both")

btn1 = Button (butnrow1, text = "1", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn1_isclicked)
btn1.pack(side = LEFT, expand = True, fill = "both")
btn2 = Button (butnrow1, text = "2", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn2_isclicked)
btn2.pack(side = LEFT, expand = True, fill = "both")
btn3 = Button (butnrow1, text = "3", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn3_isclicked)
btn3.pack(side = LEFT, expand = True, fill = "both")
btn4 = Button (butnrow1, text = "+", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn_plusclicked)
btn4.pack(side = LEFT, expand = True, fill = "both")


btn5 = Button (butnrow2, text = "4", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn4_isclicked)
btn5.pack(side = LEFT, expand = True, fill = "both")
btn6 = Button (butnrow2, text = "5", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn5_isclicked)
btn6.pack(side = LEFT, expand = True, fill = "both")
btn7 = Button (butnrow2, text = "6", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn6_isclicked)
btn7.pack(side = LEFT, expand = True, fill = "both")
btn8 = Button (butnrow2, text = "-", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn_subclicked)
btn8.pack(side = LEFT, expand = True, fill = "both")


btn9 = Button (butnrow3, text = "7", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn7_isclicked)
btn9.pack(side = LEFT, expand = True, fill = "both")
btn10 = Button (butnrow3, text = "8", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn8_isclicked)
btn10.pack(side = LEFT, expand = True, fill = "both")
btn11 = Button (butnrow3, text = "9", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn9_isclicked)
btn11.pack(side = LEFT, expand = True, fill = "both")
btn12 = Button (butnrow3, text = "x", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn_mulclicked)
btn12.pack(side = LEFT, expand = True, fill = "both")


btn13 = Button (butnrow4, text = "C", font = ("Verdana",22),relief = GROOVE, border = 0,command = c_pressed)
btn13.pack(side = LEFT, expand = True, fill = "both")
btn14 = Button (butnrow4, text = "0", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn0_isclicked)
btn14.pack(side = LEFT, expand = True, fill = "both")
btn15 = Button (butnrow4, text = "=", font = ("Verdana",22),relief = GROOVE, border = 0, command  = result)
btn15.pack(side = LEFT, expand = True, fill = "both")
btn16 = Button (butnrow4, text = "/", font = ("Verdana",22),relief = GROOVE, border = 0,command = btn_divclicked)
btn16.pack(side = LEFT, expand = True, fill = "both")




root.mainloop()