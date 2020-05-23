from tkinter import *
import parser

expression = ""

root = Tk()
root.title("Calculadora Levi")
root.geometry("400x600")
root.resizable(False,False)
root.configure(background = "gray42")

# Caracteristicas para los botones

color_boton = "gray99"
width_boton = 10
high_boton = 3



equation = StringVar()

display = Entry(root,font = ("arial",20,"bold"),width = 22,borderwidth = 10, background = "Gray100", textvariable = equation)
display.place (height = 90)
display.grid(row = 0,column = 0,columnspan = 4 ,padx = 25, pady = 20)

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


def clear():
    global operator
    operator = ""
    equation.set("0")

clear()

# Numeros y botones

Button(root, text ="1",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(1)).grid(row = 2,column = 0,pady = 10)
Button(root, text ="2",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(2)).grid(row = 2,column = 1,pady = 10)
Button(root, text ="3",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(3)).grid(row = 2,column = 2,pady = 10)

Button(root, text ="4",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(4)).grid(row = 3,column = 0,pady = 10)
Button(root, text ="5",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(5)).grid(row = 3,column = 1,pady = 10)
Button(root, text ="6",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(6)).grid(row = 3,column = 2,pady = 10)

Button(root, text ="7",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(7)).grid(row = 4, column = 0,pady = 10)
Button(root, text ="8",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(8)).grid(row = 4, column = 1,pady = 10)
Button(root, text ="9",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(9)).grid(row = 4, column = 2,pady = 10)

# Botones Numericos

Button(root, text ="AC",bg = color_boton, width = width_boton, height = high_boton, command = lambda: clear_display()).grid(row = 5, column = 0,pady = 10)
Button(root, text ="0",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_numbers(0)).grid(row = 5, column = 1,pady = 10)
Button(root, text ="%",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_operation("%")).grid(row = 5, column = 2,pady =10)

# Botones para ejercer las operaciones matematicas

Button(root, text = "+",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_operation("+")).grid(row= 6, column = 0,pady = 10)
Button(root, text = "-",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_operation("-")).grid(row= 6, column = 1,pady = 10)
Button(root, text = "*",bg = color_boton, width = width_boton, height = high_boton, command = lambda:get_operation("*")).grid(row= 6, column = 2,pady = 10)
Button(root, text = "/",fg = "white", bg = "black" , width = width_boton, height = high_boton, command = lambda:get_operation("/")).grid(row= 6, column = 3,pady = 10)

Button(root, text = "⌫",fg = "white", bg = "black" , width = width_boton, height = high_boton, command = lambda: undo()).grid(row= 2, column = 3,columnspan = 2, pady = 10)
Button(root, text = "exp",fg = "white", bg = "black" , width = width_boton, height = high_boton, command = lambda:get_operation("**")).grid(row= 3,column = 3,pady = 10)
Button(root, text = "^2",fg = "white", bg = "black" , width = width_boton, height = high_boton, command =lambda:get_operation("**2")).grid(row= 4, column = 3,pady = 10)
Button(root, text = "√",fg = "white", bg = "black" , width = width_boton, height = high_boton, command =lambda:get_operation("sqrt")).grid(row= 5, column = 3,pady = 10)
Button(root, text = "(",fg = "white", bg = "black" , width = width_boton, height = high_boton, command = lambda:get_operation("(")).grid(row= 7, column = 0,pady = 10)
Button(root, text = ")",fg = "white", bg = "black" , width = width_boton, height = high_boton, command = lambda:get_operation(")")).grid(row= 7, column = 1,pady = 10)
Button(root, text = "[",fg = "white", bg = "black" , width = width_boton, height = high_boton, command = lambda:get_operation("[")).grid(row= 7, column = 2,pady = 10)
Button(root, text = "]",fg = "white", bg = "black" , width = width_boton, height = high_boton, command = lambda:get_operation("]")).grid(row= 7, column = 3, pady = 10)
Button(root, text = "=",fg = "white", bg = "black", width = width_boton, height = high_boton, command = lambda:calculate()).grid(row= 8, column = 0, sticky = W+E, columnspan = 5)


root.mainloop()
 
