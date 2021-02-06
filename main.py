import tkinter as tk

root = tk.Tk()
root.geometry("510x700")
#root.resizable(0, 0)

# Top Input Label
InputLabel = tk.Label(root, text="Example", font=("Courier", 15), width=42, height=5, borderwidth=2, relief="solid")

#InputLabel.config(text="5")
#InputLabel.cget("text")

# numClick function for inputting numbers 0-9 into equation
def numClick(num):
    print(num)

# Number Buttons
Button7 = tk.Button(root, text="7", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(7))
Button8 = tk.Button(root, text="8", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(8))
Button9 = tk.Button(root, text="9", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(9))
Button4 = tk.Button(root, text="4", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(4))
Button5 = tk.Button(root, text="5", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(5))
Button6 = tk.Button(root, text="6", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(6))
Button1 = tk.Button(root, text="1", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(1))
Button2 = tk.Button(root, text="2", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(2))
Button3 = tk.Button(root, text="3", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(3))
Button0 = tk.Button(root, text="0", font=("Courier", 50), borderwidth=10, relief="groove", command=lambda: numClick(0))

# Operations
EqualButton = tk.Button(root, text="=", font=("Courier", 50), borderwidth=10, width=5, relief="groove")
AddButton = tk.Button(root, text="+", font=("Courier", 50), borderwidth=10, width=3, relief="groove")

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

# Computation variables
equation = None # To hold equations to be used in 
output = None # To store the answer (output) of equation

root.mainloop()