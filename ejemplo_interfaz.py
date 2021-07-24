#Importar librerías
from tkinter import *
import tkinter as tk
from tkinter.ttk import *

def funcionDatos():
    newWindow = tk.Toplevel(root)
    newWindow.geometry('250x450')
    lbl = Label(newWindow, text="Ingrese número decimal:")
    lbl.grid(column=1, row=1)
    txt = Entry(newWindow,width=10)
    txt.grid(column=3, row=1)
    
    btn = Button(newWindow, text="Calcular")
    btn.grid(column=1, row=3)

# Configuración de la raíz
root = Tk()
root.title("Calculadora PyLadies")
root.geometry('350x500')
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Datos",command=funcionDatos) #Maria
filemenu.add_command(label="IMC") #Yojahida
filemenu.add_command(label="Edad") #Katherine
filemenu.add_command(label="Descuento") #Mayda
filemenu.add_command(label="Fecha") #Katherine
filemenu.add_command(label="Longitud") #Katherine
filemenu.add_command(label="Área") #Margaret
filemenu.add_command(label="Volumen") #
filemenu.add_command(label="Temperatura") #Crhis
filemenu.add_command(label="Velocidad") #Kaly y Yessenia
filemenu.add_command(label="Tiempo") #Yessenia
filemenu.add_command(label="Masa") #
filemenu.add_command(label="Sistema numérico") #Margaret
filemenu.add_command(label="Inversión") #
filemenu.add_command(label="Moneda") #
filemenu.add_command(label="Préstamo") #María
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de PyLadies")

menubar.add_cascade(label="Opciones", menu=filemenu)
menubar.add_cascade(label="PyLadies", menu=helpmenu)

# Label
lbl = Label(root, text="Bienvenida", font=("Arial Bold", 10))
lbl.grid(column=5, row=2)

lblMensaje = Label(root, text="", font=("Arial Bold", 10))
lblMensaje.grid(column=5, row=4)

def funcionMostrarTexto():
     lblMensaje.configure(text="Iniciemos !!")

# Button
btn = Button(root, text="Clic aquí",command=funcionMostrarTexto)
btn.grid(column=5, row=3)

#Función para capturar dato del textbox
def funcionCapturarDato():

    dato = "Hola " + txt.get()
    lblResultado.configure(text = dato)

lblNombre = Label(root, text="¿Cuál es tu nombre?", font=("Arial Bold", 10))
lblNombre.grid(column=5, row=9)
# TextBox
txt = Entry(root,width=20)
txt.grid(column=5, row=10)

btnMostrar = Button(root, text="Enviar", command=funcionCapturarDato)
btnMostrar.grid(column=5, row=11)

lblResultado = Label(root, text="", font=("Arial Bold", 10))
lblResultado.grid(column=5, row=12)

lblCombo = Label(root, text="Seleccione una opción", font=("Arial Bold", 10))
lblCombo.grid(column=0, row=13)
lblSeleccion = Label(root, text="", font=("Arial Bold", 10))
lblSeleccion.grid(column=0, row=16)
def funcionCapturarCmb():
    seleccion = "Usted seleccionó la opción " + combo.get()
    lblSeleccion.configure(text = seleccion)
btnCombo = Button(root, text="Mostrar Seleccion", command=funcionCapturarCmb)
btnCombo.grid(column=0, row=15)
#Combobox
combo = Combobox(root,width=5)
combo['values']= (1, 2, 3, 4, 5)
combo.current(1) #set the selected item
combo.grid(column=0, row=14)



# Finalmente bucle de la aplicación
root.mainloop()


