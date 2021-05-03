# version 2 de clases
# los cursos son las clases que contienen a los alumnos,

#? tengo la idea de usar al objeto del Instituto que contenga todos los alumnos y a cada alumno asignarle los cursos como atributo

import winsound


class NodoAlumno():
    def __init__(self, nom, ape):
        self.dni = 0
        self.nombre = nom
        self.apellido = ape      
        
    #retorna los atributos del objeto
    def informe(self):
        #cad=[self.nombre, self.apellido]        
        cad = "Nombre: {}  Apellido: {} \n".format(self.nombre, self.apellido)        
        return cad
    
#  --fin NodoAlumno


class CursoIdioma():

    def __init__(self, nombre_del_curso):
        self.nombreCurso = nombre_del_curso
        self.listaCurso = []  
        
    def nombre(self):
        return self.nombreCurso

    # ingresa un estudiante al curso
    def ingresar(self, nodo):        
        self.listaCurso.append(nodo)

    #  Retorna la cantidad de alumnos en este curso
    def informe_de_inscriptos(self):
        return "En el curso de {} hay {} inscriptos: \n".format(self.nombre(), len(self.listaCurso) )
   
    # retorna un string con todos los estudiantes en lineas diferentes
    def informe_alumnos(self):       
        if len(self.listaCurso) == 0:
            cad = "No hay alumnos anotados en."+self.nombre() + "\n \n"
        else:
            cad = self.informe_de_inscriptos()
            for i in self.listaCurso:
                cad = cad + i.informe()
            cad += "\n"
        return cad


#  --------fin CursoIdioma

# La clase principal que controla los alumnos y los cursos dictados en él 
class nuevoInstituto():
    def __init__(self, nombre):
        self.nombre_insti = nombre
        self.cursos  = {}  # 1: Ingles, 2: Italiano, etc
        self.alumnos = {}  # numero de legajo es el id para los alumnos guardados

     
    #  recive como parametro solo los nombres de cada carrera
    def crea_carreras(self, *lista_con_idiomas):  # ("Ingles", "Italiano", "Mandarin", etc)
        c = 1
        lis_idioma=list(lista_con_idiomas)[0] 
        #extraigo la lista de parametros y trabajo con cada uno
        for i in range(len(lis_idioma)):
            self.cursos[c] = CursoIdioma(lis_idioma[i])     # llena el dicc cursos
            c += 1

    #  devuelve el string con los registros del curso pasado por indice
    def informe_del_curso(self, indice_curso):
        return self.cursos[indice_curso].informe_alumnos() 

    #  devuelve el informe completo de alumnos
    def todos_los_informes(self):     
        st = ""
        for i in self.cursos.keys():
            st+= self.informe_del_curso(i)
        return st

    #  retorna una lista con nombres de los cursos registrados
    def listado_cursos(self):        
        lista = []
        for clave in self.cursos:
            lista.append(self.cursos[clave].nombre())
        return lista
   
    
    #  opcion del menu para agregar nuevo alumno
    def ingreso_de_alumnos(self):
        continuar=""
        while continuar !="y" :           
           
      #! todavia queda comprobar que no ingrese datos repetidos, pidiendo DNI por ej
            # no se permiten datos vacios
            while True:
                un_nombre = input("Ingresa nombre: " )
                if un_nombre != '':
                    break            
            while True:
                un_apellido = input ("Ingresa apellido: ")
                if un_apellido != '':
                    break

            alumno = NodoAlumno(un_nombre, un_apellido)            

            sig=True
            print("elija la clase donde se anotara:")
            st = ""
            
            lis = self.listado_cursos()
            # print(lis)          
            # input()
            for i in range(len(lis)):
                st += f"{str(i+1)}: {lis[i-1]}\n"
            print(st)

            while sig:
                try:
                    opcion_curso = int(input())
                    self.cursos[opcion_curso].ingresar(alumno)
                    print(self.cursos[opcion_curso].informe_de_inscriptos()) 

                    sig=False
                except:
                    winsound.Beep(3900, 600)
                    print("ingresar numeros validos")

            continuar = input("Para terminar el registro presione la 'y' ")


    # ingreso algunos datos para que ya tenga
    def carga_registros_de_prueba(self):
        n = 1
        for i in range(1,len(self.cursos.keys())+1 ):
            for e in range(n):
                alumno = NodoAlumno(f"nom_ing{n}", f"ape_ing{n}")     
                self.cursos[i].ingresar(alumno)
            n += 1
        

#  primer menu con las opciones principales de la app
def menu_principal(insti):
    seguir=True
    while seguir:
        print(" Presione:\n 1: para ingresar alumnos \n 2: imprimir todo el registro \n Otro caracter para salir")
        
        op = input()        
        if op == "1":
            insti.ingreso_de_alumnos()            
        else:
            if op == "2":
                print(insti.todos_los_informes())
            else:
                seguir=False

def main():  
    instituto_lenguas=nuevoInstituto("Instituto Multilingue")
    instituto_lenguas.crea_carreras(["Ingles", "Italiano","Mandarin"])
    instituto_lenguas.carga_registros_de_prueba()

    menu_principal(instituto_lenguas)

if __name__ == "__main__":
    main()
