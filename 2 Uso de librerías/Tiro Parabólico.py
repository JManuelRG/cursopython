# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:41:21 2021

@author: José Manuel
"""

#Tiro Parabólico Simulador
from tkinter import *
import numpy as np
from math import sin,cos,pi
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

####################################################################
# Función para graficar (Botón)
def graficar():
    global canvas,toolbar
    # Leer Variables
    try:
        vo = float(cajavelocidad.get())
        angulo = float(cajaangulo.get())
    except:
        messagebox.showinfo(message="Los valores introducidos deben ser numéricos ",
                            title="Error en la lectura de datos")
    
    A = angulo*pi/180  # Ángulo en radianes
    g = 9.80665 #m/s^2 aceleración de la gravedad
    vxo = vo*cos(A)
    vyo = vo*sin(A)
    
    # Altura máxima
    h=vo**2*sin(A)**2/(2*g)
    
    #Alcance
    R=vo**2*sin(2*A)/(g)

    # tiempo de vuelo
    tv=2*vo*sin(A)/g

    #Trayectoria Generada
    t=np.linspace(0,tv,100) # vector de tiempo
    y=vyo*t-(1/2)*g*t**2 # parábola descrita (altura)
        
    # Lienzo del gráfico   
    fig = Figure(figsize=(5,4),dpi=100)
    
    canvas = FigureCanvasTkAgg(fig, master=marco_graf)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, marco_barra)# barra de iconos
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    ax1=fig.add_subplot(111) # AXES , AXIS
    ax1.plot(t,y)
    ax1.set_xlabel('tiempo (t), segundos')
    ax1.set_ylabel('altura (h), metros')
    ax1.set_title('Tiro Parabólico.')
    fig.suptitle('Trayectoria Descrita.', fontsize=12)
    ax1.grid()
    
    #Activar botones
    boton['state']='disabled'
    botonnuevo['state']='normal'
    
############################################################################
#Ventana Principal
ventana = Tk()
ventana.title('Tiro Parabólico')
ventana.geometry('1200x600')

# Marco Entrada de Datos:
marco_entrada = Frame(master=ventana,
                      background="#ffffff",
                      width=600,
                      height=600, 
                      highlightbackground="black",
                      highlightthickness=1)
#relief styles = flat, sunken, raised, groove, ridge

marco_entrada.grid(row=0, 
                   column=0, 
                   columnspan=2, 
                   rowspan=5)
##########################################################################
# Marco Entrada de Datos
# Entrada de Datos
LTitulo = Label(master=marco_entrada,
                text="Ingresa los datos iniciales del tiro:", 
                relief=GROOVE,
                font=("Arial",15),
                fg='blue')
LTitulo.grid(row=2, column=0, columnspan=2)

Lenunciado = Label(master=marco_entrada,
                text="Un jugador lanza un balón con las siguientes características. \n Analice la trayectoria del balón",
                font=("Arial",15),
                fg='black')
Lenunciado.grid(row=1, column=0, columnspan=2)

Lvelocidad = Label(master=marco_entrada, 
                   text="Velocidad Inicial (m/s)", 
                   font=("Arial",15),
                   fg='blue')
Lvelocidad.grid(row = 4, column=0)

cajavelocidad = Entry(master=marco_entrada,
                      font=("Arial",15),
                      fg='black')
                      
cajavelocidad.grid(row = 4, column=1)

Langulo = Label(master=marco_entrada, 
                text="Ángulo de incidencia(°)", 
                font=("Arial",15),
                fg='blue')
                      
Langulo.grid(row = 6, column=0)

cajaangulo = Entry(master=marco_entrada,
                   font=("Arial",15),
                   fg='black')
                      
cajaangulo.grid(row = 6, column=1)

# Botón Calcular
boton = Button(master=marco_entrada, 
               text="Calcular Trayectoria",
               font=("Arial",15),
               fg='blue',
               relief=GROOVE,
               command=graficar)

boton.grid(row=7, column=0, columnspan=2) 

# Botón Nuevo Cálculo
def nuevo():
    boton['state']='normal'
    botonnuevo['state']='disabled'
    cajaangulo.delete(0,END)
    cajavelocidad.delete(0,END)
    canvas.get_tk_widget().destroy()
    toolbar.destroy()
    marco_graf.config(width=600,
                   height=600)
    
botonnuevo = Button(master=marco_entrada, 
               text="Nuevo Cálculo",
               font=("Arial",15),
               fg='blue',
               relief=GROOVE,
               command=nuevo)
botonnuevo['state']='disabled'
botonnuevo.grid(row=8, column=0, columnspan=2) 

# Botón Salir
def salir():
    ventana.destroy()
botonsalir = Button(master=marco_entrada, 
               text="Salir",
               font=("Arial",15),
               fg='blue',
               relief=GROOVE,
               command=salir)

botonsalir.grid(row=9, column=0, columnspan=2) 

##########################################################################
# Marco de Gráfico
marco_graf = Frame(master=ventana, 
                   relief=GROOVE,
                   #background="#fffff0",
                   width=600,
                   height=600, 
                   #highlightbackground="black",
                   highlightthickness=1)
marco_graf.grid(row=0, 
                column=2, 
                columnspan=5, 
                rowspan=5)

# Marco Barra de Herramientas Gráfico
marco_barra = Frame(master=ventana, 
                   relief=GROOVE,
                   #background="#fffff0",
                   width=600,
                   height=200, 
                   highlightbackground="black",
                   highlightthickness=1)
marco_barra.grid(row=6, 
                column=2, 
                columnspan=5, 
                rowspan=2)



# Continuo
ventana.mainloop() 
