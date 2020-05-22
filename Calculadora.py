from tkinter import *
import parser

expression = ""

root = Tk()
root.title("Calculadora Levi")
root.geometry("304x155")

equation = StringVar()

display = Entry(root, textvariable = equation)
display.place (height = 90)
display.grid(row = 1 , columnspan= 6, ipadx = 90, ipady = 3,sticky = W+E)

equation.set ("")


i = 0

# Para poder insertar los numeros.

def get_numbers(n):
    global  i
    display.insert(i,n)
    i+=1


# Para poder insertar los operadores matematicos

def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i,operator)
    i+= operator_length


# Para resetar los numeros de la calculadora

def clear_display():
    display.delete(0, END)

# Para borrar el numero que quieras

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0,display_new_state)
    else:
        clear_display()
        display.insert(0,'0')

# Para darte el valor total de la operación 

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0,result)
    except math_expression as indentifier:
        clear_display()
        display.insert(0,'Error')

# Numeros y botones

Button(root, text ="1", command = lambda:get_numbers(1)).grid(row = 2,column = 0,sticky = W+E,)
Button(root, text ="2",command = lambda:get_numbers(2)).grid(row = 2, column = 1,sticky = W+E)
Button(root, text ="3",command = lambda:get_numbers(3)).grid(row = 2, column = 2,sticky = W+E)

Button(root, text ="4",command = lambda:get_numbers(4)).grid(row = 3, column = 0,sticky = W+E)
Button(root, text ="5",command = lambda:get_numbers(5)).grid(row = 3, column = 1,sticky = W+E)
Button(root, text ="6",command = lambda:get_numbers(6)).grid(row = 3, column = 2,sticky = W+E)

Button(root, text ="7",command = lambda:get_numbers(7)).grid(row = 4, column = 0,sticky = W+E)
Button(root, text ="8",command = lambda:get_numbers(8)).grid(row = 4, column = 1,sticky = W+E)
Button(root, text ="9",command = lambda:get_numbers(9)).grid(row = 4, column = 2,sticky = W+E)

# Botones Numericos

Button(root, text ="AC",command = lambda: clear_display()).grid(row = 5, column = 0,sticky = W+E)
Button(root, text ="0", command  = lambda:get_numbers(0)).grid(row = 5, column = 1,sticky = W+E)
Button(root, text ="%", command = lambda:get_operation("%")).grid(row = 5, column = 2,sticky = W+E)

# Botones para ejercer las operaciones matematicas

Button(root, text = "+", command = lambda:get_operation("+")).grid(row= 2, column = 3,sticky = W+E)
Button(root, text = "-", command = lambda:get_operation("-")).grid(row= 3, column = 3,sticky = W+E)
Button(root, text = "*", command = lambda:get_operation("*")).grid(row= 4, column = 3,sticky = W+E)
Button(root, text = "/", command = lambda:get_operation("/")).grid(row= 5, column = 3,sticky = W+E)

Button(root, text = "⌫",fg = "white", bg = "black", bd = 1.2 , command = lambda: undo()).grid(row= 2, column = 4,sticky = W+E,columnspan = 2)
Button(root, text = "exp",fg = "white", bg = "black", bd = 1.2 , command = lambda:get_operation("**")).grid(row= 3,column = 4,sticky = W+E)
Button(root, text = "^2",fg = "white", bg = "black", bd = 1.2 , command = lambda:get_operation("**2")).grid(row= 3, column = 5,sticky = W+E)
Button(root, text = "(",fg = "white", bg = "black", bd = 1.2 , command = lambda:get_operation("(")).grid(row= 4, column = 4,sticky = W+E)
Button(root, text = ")",fg = "white", bg = "black", bd = 1.2 , command = lambda:get_operation(")")).grid(row= 4, column = 5,sticky = W+E)
Button(root, text = "[",fg = "white", bg = "black", bd = 1.2 , command = lambda:get_operation("[")).grid(row= 5, column = 4,sticky = W+E)
Button(root, text = "]",fg = "white", bg = "black", bd = 1.2 , command = lambda:get_operation("]")).grid(row= 5, column = 5,sticky = W+E)
Button(root, text = "=",fg = "white", bg = "black", bd = 1.2 , command = lambda:calculate()).grid(row= 6, column = 0 ,sticky = W+E, columnspan = 6)


root.mainloop()
 