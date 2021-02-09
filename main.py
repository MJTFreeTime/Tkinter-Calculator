import tkinter as tk

root = tk.Tk()
root.geometry("510x700")
root.resizable(0, 0)

# Top Input Label
InputLabel = tk.Label(root, text="", font=("Courier", 15), width=42, height=5, borderwidth=2, relief="solid")

equation = ""
operatorOnly = False
numOnly = False
answer = False

# inputLogic function evaluates problems; it's the main source of error prevention
def inputLogic():
    global equation
    global numOnly

    # Set numOnly to True if it finds that the last character in equation was an operator, not and int; otherwise False
    try:
        if len(equation) >= 3:
            if equation[len(equation) - 2] != " ":
                int(equation[len(equation) - 2])
    except:
        numOnly = True
    else:
        numOnly = False

# inputMath function for inputting numbers 0-9 into equation
def inputMath(inp):
    global equation
    global answer
    inputLogic()

    # If numOnly is true we check if inp is an operator; if it is, then error, and if not, then concat inp onto InputLabel
    if numOnly:
        if len(inp) >= 3:
            print("You cannot enter two operators in a row!")
            return
    
    if answer == True:
        if len(inp) < 3:
            clearEquation()
        answer = False

    equation = equation + inp
    InputLabel.config(text=equation)

#computerMath function to compute the equation that's already in the InputLabel
def computeMath():
    global equation
    global answer
    inputLogic()

    equation = str(eval(equation))
    InputLabel.config(text=equation)
    answer = True

def clearEquation():
    global equation
    equation = ""
    InputLabel.config(text=equation)

# Number Buttons
Button7 = tk.Button(root, text="7", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("7"))
Button8 = tk.Button(root, text="8", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("8"))
Button9 = tk.Button(root, text="9", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("9"))
Button4 = tk.Button(root, text="4", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("4"))
Button5 = tk.Button(root, text="5", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("5"))
Button6 = tk.Button(root, text="6", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("6"))
Button1 = tk.Button(root, text="1", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("1"))
Button2 = tk.Button(root, text="2", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("2"))
Button3 = tk.Button(root, text="3", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("3"))
Button0 = tk.Button(root, text="0", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: inputMath("0"))

# Operations Buttons
EqualButton = tk.Button(root, text="=", font=("Courier", 50), borderwidth=10, width=5, relief="groove", command=computeMath)
AddButton = tk.Button(root, text="+", font=("Courier", 50), borderwidth=10, width=3, relief="groove", command=lambda: inputMath(" + "))
MinusButton = tk.Button(root, text="-", font=("Courier", 50), borderwidth=10, width=3, relief="groove", command=lambda: inputMath(" - "))
ClearButton = tk.Button(root, text="CLR", font=("Courier", 38), borderwidth=10, width=3, relief="groove", bg="red", command=clearEquation)

# Placements
InputLabel.place(x=0, y=0)

Button7.place(x=0, y=116)
Button8.place(x=116, y=116)
Button9.place(x=232, y=116)
Button4.place(x=0, y=256)
Button5.place(x=116, y=256)
Button6.place(x=232, y=256)
Button1.place(x=0, y=396)
Button2.place(x=116, y=396)
Button3.place(x=232, y=396)
Button0.place(x=0, y=536)

EqualButton.place(x=280, y=536)
AddButton.place(x=348, y=116)
MinusButton.place(x=348, y=256)
ClearButton.place(x=390, y=0)


root.mainloop()