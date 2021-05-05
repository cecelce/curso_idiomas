# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:01:56 2021
@author: Damian
"""
'''
Un instituto de idiomas ofrece cursos de inglés, francés y mandarín.
Necesita un programa que le permita al estudiante elegir uno de los 3 cursos que desee estudiar.
**La aplicación mostrará después de cada registro la cantidad de estudiantes que tiene cada curso.
Condiciones:  Utilizar clases  La clase creada debe tener atributos
 La clase creada debe tener como mínimo los métodos para ingresar datos,
        calcular cuántos estudiantes ingresaron al instituto
        e imprimir resultados.
extra: guarda todo lo ingresado en un fichero en el disco para poder volver a cargarlo la proxima vez
'''
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
 
#para guardar y habrir ficheros en el disco
import io #supuestamente se necesita para open(fichero) pero el compilador marca que no se usa nada de esta libreria
from pickle import load
from pickle import dump
 
#para agregar detalles en imprimir_listado en el archivo de texto
from datetime import datetime
 
 
 
class Estudiante():
 
    def __init__ (self, nombre_est, apellido_est):
        self.nombre=nombre_est
        self.apellido=apellido_est
 
#--fin Estudiante
 
 
class CursoIdioma():
 
    def __init__ (self):
        self.listaCurso=[]
 
    def ingresar(self,nodoEstudiante):         # ingresa un estudiante al curso
        self.listaCurso.append(nodoEstudiante)
 
    def lista_para_imprimir(self):         #retorna un string con todos los estudiantes en lineas diferentes
        cadena=""
 
        for i in self.listaCurso:
            cadena=cadena + "Nombre: {} Apellido: {}\n".format(i.nombre, i.apellido)
 
        return cadena
 
    def calcularCant(self):                     #Retorna la cantidad de alumnos en este curso
        return len(self.listaCurso)
 
#-fin CursoIdiomas
 
class TodosLosCursos():
    def __init__ (self):
        self.ingles=CursoIdioma()
        self.frances=CursoIdioma()
        self.mandarin=CursoIdioma()
 
 
def agrega_nuevo_alumno(): #es llamada por el boton "Agregar nuevo"
    obj_curso=curso
 
    nombre=entrada_nomb.get()
    apellido=entrada_apell.get()
    valor_radio=val_radio.get() #1 = Ingles  2 = Frances  3 = Mandarin
 
    if  nombre == "":
        print(messagebox.showinfo(message="Igrese un nombre", title="Advertencia") )
    else:
        if apellido =="":
            print(messagebox.showinfo(message="Igrese un apellido", title="Advertencia") )
        else:
            if valor_radio == 0:
                print(messagebox.showinfo(message="Seleccione un curso", title="Advertencia") )
            else:
                # agrega el estudiante
                alumno_nuevo=Estudiante(nombre,apellido)
 
                if valor_radio == 1:
                    obj_curso.ingles.ingresar(alumno_nuevo)
                    var_etiq_ing.set(obj_curso.ingles.calcularCant()) #actualiza la etiqueta de cantidad
                    radio_ingles.deselect()
                else:
                    if valor_radio == 2:
                        obj_curso.frances.ingresar(alumno_nuevo)
                        var_etiq_fran.set(obj_curso.frances.calcularCant() )
                        radio_frances.deselect()
                    else:
                        if valor_radio == 3:
                            obj_curso.mandarin.ingresar(alumno_nuevo)
                            var_etiq_mand.set(obj_curso.mandarin.calcularCant() )
                            radio_mandarin.deselect()
 
                print(messagebox.showinfo(message="Alumno ingresado", title="Notificacion") )
                texto_nombre.set("")
                texto_apellido.set("")
                val_radio.set(0)
 
#--fin agrega_nuevo_alumno
 
 
#Cuando se apreta el boton "Imprimir"
#imprime toda la informacion de los cursos con sus alumnos en la caja de texto texto_impresion
 
def imprimir_listado():
    obj_curso=curso
 
    c_i =obj_curso.ingles.calcularCant()
    c_f =obj_curso.frances.calcularCant()
    c_m =obj_curso.mandarin.calcularCant()
 
    txt="En total hay {} estudiantes ingresados.\n".format(c_i+c_f+c_m)
    if c_i > 0: #si hay registros
        txt=txt+"Para el curso de Ingles se anotaron {} alumnos y son los siguientes:\n".format(c_i)
        txt=txt+obj_curso.ingles.lista_para_imprimir()+"\n"
    if c_f > 0:
        txt=txt+"Para el curso de Frances se anotaron {} alumnos y son los siguientes:\n".format(c_f)
        txt=txt+obj_curso.frances.lista_para_imprimir()+"\n"
    if c_m > 0:
        txt=txt+"Para el curso de Mandarin se anotaron {} alumnos y son los siguientes:\n".format(c_m)
        txt=txt+obj_curso.mandarin.lista_para_imprimir()+"\n"
 
    texto_impresion.delete("1.0","end")
    texto_impresion.insert(END, txt)
 
    #imprime en un archivo de texto,
    #se habre el fichero en modo "append" agregando la fecha y hora como cabecera para el nuevo registro
    archivo_txt=open(ruta_fichero_texto,'a')
    tx='**************************** \n' #cabecera de cada
    tx=tx+'Registro tomado el '+ str(now.date()) + "\n" +'a las '+ str(now.time()) + "\n\n" + txt + "\n\n"
 
    archivo_txt.write(tx)
    archivo_txt.close()
    del(archivo_txt)
 
 
 
 
 
 
##-imprime_listado
 
 
def habrir_fichero():
    try:
        fichero_binario=open(ruta_fichero_binario,"rb")
        bol=messagebox.askyesno(message="Si ya cargo datos, se sobreescribiran\n ¿Desea continuar?", title="Cargar nuevos")
 
        if bol:
 
            obj_curso=load(fichero_binario)
            global curso  #de esta forma puedo modificar una variable global desde una funcion
            curso=obj_curso
 
#actualiza las etiquetas de cantidad
            var_etiq_ing.set(obj_curso.ingles.calcularCant() )
            var_etiq_fran.set(obj_curso.frances.calcularCant() )
            var_etiq_mand.set(obj_curso.mandarin.calcularCant())
 
            fichero_binario.close()
            del(fichero_binario)
 
            print(messagebox.showinfo(message="Fichero cargado", title="Notificacion") )
 
    except FileNotFoundError:
        messagebox.showinfo(message="No se ha guardado ningun fichero todavia", title="Alerta")
 
 
#guarda en archivo binario
def guardar_fichero(obj_curso):
 
 
    fichero_binario=open(ruta_fichero_binario,"wb")
    dump(obj_curso, fichero_binario)
 
    fichero_binario.close()
    del(fichero_binario)
 
    print(messagebox.showinfo(message="Fichero guardado", title="Notificacion") )
 
 
 
# inicializacion de variables----------------
 
root = Tk()
root.title("Alta de alumnos")
root.geometry("510x400")
#root.resizable(0, 0)
 
 
texto_nombre = StringVar()
texto_apellido = StringVar()
 
 
curso=TodosLosCursos()
#curso.ingles, curso.frances, curso.mandarin
 
val_radio= IntVar()
 
var_etiq_ing= StringVar()
var_etiq_fran= StringVar()
var_etiq_mand= StringVar()
 
#al no especificar una ruta se guarda en el mismo directorio donde esta el codigo
#si se usa anaconda, usa directorios virtuales C:\VTRoot\HarddiskVolume2\
 
ruta_fichero_binario="lista_cursos.bin"
ruta_fichero_texto="lista_cursos.txt"
 
now = datetime.now()
 
# inicializacion de variables----------------
 
 
 
#caja de texto donde se guarda lo que se imprimira
 
texto_impresion = scrolledtext.ScrolledText(root, undo=True, width=60, height=15, wrap='word')
texto_impresion['font'] = ('consolas', '10')
texto_impresion.place(x=40, y=140)
 
 
 
 
#----   En algun momento tendria q tratar de usar frames para ordenar los objetos
 
etiqueta_nomb = Label(root, text="Nombre:")
etiqueta_nomb.place(x=20, y=20)
 
etiqueta_apell = Label(root, text="Apellido:")
etiqueta_apell.place(x=20, y=40)
 
entrada_nomb = Entry(root, textvariable=texto_nombre)
entrada_nomb.place(x=80, y=20)
entrada_nomb.focus()
 
entrada_apell = Entry(root, textvariable=texto_apellido)
entrada_apell.place(x=80, y=40)
 
#-
 
boton_agregar = Button(root, text="Agregar nuevo", command=lambda:[agrega_nuevo_alumno()] )
boton_agregar.place(x=40, y=60)
 
 
 
boton_imprimir = Button(root, text="Imprimir", command=lambda:[imprimir_listado()] )
boton_imprimir.place(x=40, y=100)
 
 
boton_abrir_fichero = Button(root, text="Abrir un fichero", command=lambda:[habrir_fichero()] )
boton_abrir_fichero.place(x=170, y=100)
 
boton_guardar_fichero = Button(root, text="Guardar en un fichero", command=lambda:[guardar_fichero(curso)] )
boton_guardar_fichero.place(x=290, y=100)
 
 
 
 
#-----botones para elegir a que carrera se anota
 
radio_ingles = Radiobutton(root, text="Ingles", value=1, variable=val_radio)
radio_ingles.deselect()
radio_ingles.place(x=220, y=20)
 
radio_frances = Radiobutton(root, text="Frances", value=2, variable=val_radio)
radio_frances.deselect()
radio_frances.place(x=220, y=40)
 
radio_mandarin = Radiobutton(root, text="Mandarin", value=3, variable=val_radio)
radio_mandarin.deselect()
radio_mandarin.place(x=220, y=60)
 
 
#---etiquetas que guardan la cantidad de alumnos anotados en cada curso
 
etiqueta_cantidad = Label(root, text="Cantidad por curso:")
etiqueta_cantidad.place(x=300, y=0)
 
etiqueta_cantidad_ing = Label(root, textvariable=var_etiq_ing)
var_etiq_ing.set("0")
etiqueta_cantidad_ing.place(x=340, y=20)
 
etiqueta_cantidad_fra = Label(root, textvariable=var_etiq_fran)
var_etiq_fran.set("0")
etiqueta_cantidad_fra.place(x=340, y=40)
 
etiqueta_cantidad_man = Label(root, textvariable=var_etiq_mand)
var_etiq_mand.set("0")
etiqueta_cantidad_man.place(x=340, y=60)
 
 
#-----
 
root.mainloop()
