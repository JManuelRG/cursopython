# -*- coding: utf-8 -*-
"""
Construccion de Diagramas Equilibrio
Líquido Vapor
Dr. José Manuel Rivera Garnica
IPN
"""
#Explicación del código:
# https://youtu.be/A2xVUiFpkD0
#Importar librerías
import matplotlib.pyplot as plt #Librería de graficación
from math import log10 #Importar Logaritmo de Librería matemática
import numpy as np #Librería numérica

#Encabezado
print("CONSTRUCCIÓN DE DIAGRAMAS TERMODINÁMICOS DE EQUILIBRIO LÍQUIDO-VAPOR PARA MEZCLAS BINARIAS.")
print("Autor: José Manuel Rivera Garnica <jmriverag@ipn.mx>")
print("Instituto Politécnico Nacional.\n")
print("Este programa genera diagramas de equilibrio L-V para mezclas binarias utilizando La Ec. de Antoine, Ley de Raoult, Ley de Dalton y las condiciones de equilibrio del sistema.\n")
print("ENTRADA: Componentes, Unidades de T y P, valor de T para el diagrama P-x-y y valor de P para el diagrama T-x-y.")
print("SALIDA: Diagrama de equilibrio T-x-y a Pcte y Diagrama de Equilibrio P-x-y a Tcte en formato png con 1024 dpi.")
print("Vectores con los datos tabulados almacenados como variables.")

#Solicitar nombre de los componentes de la mezcla
def comp():
    global comp1, comp2
    print("\nENTRADA DE COMPONENTES DE LA MEZCLA:")
    comp1=str(input("Escribe el nombre del componente 1 de la mezcla = "))
    comp2=str(input("Escribe el nombre del componente 2 de la mezcla = "))

#Solicitar los valores de la ecuación de Antoine
def leerctes():
  global a1,b1,c1,a2,b2,c2
  print("\nENTRADA DE CONSTANTES DE ANTOINE.")
  print("Escribe los valores de las constantes de la Ec. de Antoine para ", comp1)
  a1=float(input("A= "))
  b1=float(input("B= "))
  c1=float(input("C= "))
  print("Escribe los valores de las constantes de la Ec. de Antoine para ", comp2)
  a2=float(input("A= "))
  b2=float(input("B= "))
  c2=float(input("C= "))	


#Leer unidades de medición
def unidades():
  global unit, unip
  print("\nENTRADA DE UNIDADES DE MEDICIÓN.")
  unit=str(input("Escribe las unidades a usar para la Temperatura = "))
  unip=str(input("Escribe las unidades a usar para la Presión = "))
	
def psat(A,B,C,T):
	p = 10**(A-B/(T+C))
	return p

def tsat(A,B,C,P):
	tempsat = B/(A-log10(P))-C
	return tempsat	

#Ejecución de las funciones de entrada de datos
comp()
leerctes()
unidades()

#Diagrama de Pxy
print("\nVALORES DE ENTRADA PARA LA CONSTRUCCIÓN DEL DIAGRAMA P-x-y")
Tpxy=float(input(f"Escribe el valor de la temperatura constante del sistema T({unit}) ="))
n=50 #Num de puntos a calcular
#Crear vectores de composiciones en la fase líquida
xp1=np.linspace(0,1,n)
xp2=1-xp1
L=len(xp1) #Num de elementos en xp1
#Inicializar vectores de Presión y composición en la fase vapor
Pxy=[0]*L
yp1=[0]*L
yp2=[0]*L
#Calcular valores de Psat de cada componente
Psat1=psat(a1,b1,c1,Tpxy)
Psat2=psat(a2,b2,c2,Tpxy)
#Generar Valores de Presión del sistema L-V
for i in range(n):
  Pxy[i]=xp1[i]*Psat1+xp2[i]*Psat2
  yp1[i]=xp1[i]*Psat1/Pxy[i]
  yp2[i]=1-yp1[i]

#Variables a graficar
#xp1 vs Pxy y yp1 vs Pxy

#Gráfico Txy
print("\nVALORES DE ENTRADA PARA LA CONSTRUCCIÓN DEL DIAGRAMA T-x-y")
Ptxy=float(input(f"Escribe el valor de la presión constante del sistema P({unip}) ="))
Tsat1=tsat(a1,b1,c1,Ptxy)
Tsat2=tsat(a2,b2,c2,Ptxy)
#Crear vecctor temperatura
Txy=np.linspace(Tsat1,Tsat2,n)
L=len(Txy)
#Inicializar vectores de Presión
Psat1=np.zeros(L)
Psat2=np.zeros(L)
xt1=np.zeros(L)
yt1=np.zeros(L)
#Cálculo de presiBones de saturación de cada componente para cada valor de temperatura
for i in range(n):
    Psat1[i]=psat(a1,b1,c1,Txy[i])
    Psat2[i]=psat(a2,b2,c2,Txy[i])
    xt1[i]=(Ptxy-Psat2[i])/(Psat1[i]-Psat2[i])
    yt1[i]=xt1[i]*Psat1[i]/Ptxy
yt2=1-yt1
xt2=1-xt1

#Variables a graficar
#xt1 vs Txy y yt1 vs Txy

#Funcion para graficar y exportar archivo como imagen png
def graficar(tipo, x1,y1,lbl1,x2,y2,lbl2):
    plt.plot(x1,y1, label=lbl1)
    plt.plot(x2,y2, label=lbl2)
    plt.xlabel(f'Composiciones en la fase L (x), y la fase V (y) de {comp1}')
    if tipo == "P-x-y":
        plt.ylabel(f'Presión, {unip}')
        plt.title(f'Diagrama {tipo} para la mezcla {comp1}-{comp2} a {Tpxy} {unit}')
    elif tipo == "T-x-y":
        plt.ylabel(f'Temperatura, {unit}')
        plt.title(f'Diagrama {tipo} para la mezcla {comp1}-{comp2} a {Ptxy} {unip}')
    plt.legend() #Escribir Leyendas de datos
    # Mostrar líneas de cuadrícula mayores color gris oscuro
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # Mostrar líneas de cuadrícula menores color gris claro
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    #Exportar a archivo png de alta resolución
    if tipo == "P-x-y":
        plt.savefig(f'Diagrama {tipo} {comp1}-{comp2} a {Tpxy} {unit}.png',dpi=1024)
        plt.show() #Mostrar en área de trabajo
        plt.clf() #Borrar valores de gráfico
    elif tipo == "T-x-y":
        plt.savefig(f'Diagrama {tipo} {comp1}-{comp2} a {Ptxy} {unip}.png',dpi=1024)
        plt.show() #Mostrar en área de trabajo
        plt.clf() #Borrar valores de gráfico
    
#Generar Gráficos
#Gráfico P-x-y
#xp1 vs Pxy y yp1 vs Pxy
graficar("P-x-y", xp1, Pxy, "P-x fase L", yp1, Pxy, "P-y fase V")

#Gráfico T-x-y
#xt1 vs Txy y yt1 vs Txy
graficar("T-x-y", xt1, Txy, "T-x fase L", yt1, Txy, "T-y fase V")

print("\nSalida del Programa:")
print("Los diagramas del sistema fueron generados en la carpeta de trabajo de python con los siguientes nombres:")
print(f'Diagrama P-x-y {comp1}-{comp2} a {Tpxy} {unit}.png')
print(f'Diagrama T-x-y {comp1}-{comp2} a {Ptxy} {unip}.png')
