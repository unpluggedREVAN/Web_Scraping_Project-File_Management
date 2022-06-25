#Elaborado por: Needler Bonilla Serrano
#               Jose Pablo Agüero Mora
#Fecha de Creación: 14/10/2021 3:00pm 
#Fecha de última Modificación: 03/11/2021 10:30am
#Versión: 3.9.6

###################### Sección de notas importantes ########################
# Nota 1: Se debe tener en cuenta que algunas de librerías requeridas      #
# necesitan de instalación previa, tales como names o fpdf.                #
#                                                                          #
# Nota 2: El nombre de los reportes html y el csv se generó a conveniencia #
# ya que no se solicitó un nombre en específico.                           #
#                                                                          #
# Nota 3: La página web ciertos momentos deja de funcionar correctamente   #
# por lo que si ocurre esto compruebe el estado del internet o espere      # 
# hasta que vuelva la conexión.                                            #
#                                                                          #
# Nota 4: No todas las ventanas cuentan con un botón "atras", debido a lo  #
# comentado en clase sobre el uso de la "x" como cierre.                   #
#                                                                          #
# Nota 5: A la hora de crear el archivo csv si no se cuenta con la versión #
# Office 2019 es posible que el formato visualizado sea diferente al que   #
# se diseñó en un inicio, por lo tanto para poder abrirlo correctamente,   #
# asegurarse de contar con esta versión o una más nueva.                   #
############################################################################

# Importe de librerías
from tkinter import *
from tkinter import ttk
import os
from os import remove
import tkinter as tk
from funciones import *
from archivos import *
import names
import re
import random

# Definición de funciones:

############################ Auxiliares de interfaz ###########################
def calculaGruposTK(cantidad):
    """
    Función:determina la cantidad de grupos encontrados en la bitácora y los mete en una lista.
    Entrada: Parámetro cantidad (numero de grupos)
    Salida: Lista con los grupos encontrados
    """
    listaGrupos = []
    cont = 1
    while cont <= cantidad:
        var = "Grupo " + str(cont)
        listaGrupos.append(var)
        cont += 1
    return listaGrupos

def extraeMayores():
    """
    Función: Busca en una lista elementos que no se repitan y los mete en otra lista.
    Entrada: N/D
    Salida: Lista de elementos rsin repetir.
    """
    extra = []
    for elemento in sinRepetidos:
        extra.append(elemento[3])
    return extra

def defineMayor():
    """
    Función: Busca el número de toda la lista.
    Entrada: N/D
    Salida: Numero mayor o maximo.
    """
    extra = extraeMayores()
    mayor = max(extra)
    return mayor

######################### Sección inserta n grupos ############################
def carne():
    """
    Función: Establece el formato que debe tener un carnet estudiantil y lo genera aleatoriamente.
    Entrada: N/D
    Salida: Carnet aleatorio  
    """
    año="20"+str(random.randint(17,21))+"0"
    sede=str(random.randint(1,5))
    aleatorio= str(random.randint(0000,9999))
    if len(aleatorio) == 3:
        aleatorio = "0" + aleatorio
    elif len(aleatorio) == 2:
        aleatorio = "00" + aleatorio
    elif len(aleatorio) == 1:
        aleatorio = "000" + aleatorio
    carne=año+sede+aleatorio
    return carne

def generaNombre():
    """
    Función: Genera de forma aleatoria un nombre y dos apellidos de una librería (names)
    Entrada: N/D
    Salida: Nombre generado aleatoriamente.
    """
    nombre=names.get_first_name()
    Papellido=names.get_last_name()
    Sapellido=names.get_last_name()

    nombre = nombre.lower()
    Papellido = Papellido.lower()
    Sapellido = Sapellido.lower()

    nomCompleto=[nombre,Papellido,Sapellido]
    nombre=tuple(nomCompleto)
    return nombre

def generaFrase():
    """
    Función: Genera las tuplas donde se deterrmina las posiciones de las frases y categorías.
    Entrada: N/D
    Salida: Sub fase con las tublas generadas.
    """
    subFrase = []
    cantCategorias = (len(clasificada)) - 1
    cat = random.randint(1, cantCategorias)
    elementos = len(clasificada[cat][1])
    frase = random.randint(1, elementos)
    tup = (cat+1, frase) 
    subFrase.append(tup)
    return subFrase

def calculaGrupo(cont, estudiantes):
    """
    Función: Valida que la cantidad de estudiantes sea mayor a cero.
    Entrada: Parámetros cont y estudiantes
    Salida: Cantidad de estudiantes por grupo
    """
    num = cont // estudiantes
    if cont % estudiantes == 0:
        num = num - 1
    return num + 1

def genBitacora(grupos, estudiantes):
    """
    Función: Rellena la lista principal con listas vacias según la cantidad de listas existentes.
    Entrada: Parámetros grupos y estudiantes.
    Salida: N/D
    """
    listas = grupos * estudiantes
    cont = 0
    while cont < listas:
        bitacora.append([])
        cont += 1

def verificaNumAux(num):
    """
    Función: Valida que el número ingresado sea entero y esté entre 0 y 10.
    Entrada: Parámetro num (Cantidad de grupos)
    Salida: Retorno de banderas True o False según la ocación.
    """
    try:
        num = int(num)
        if 0 < num < 10:
            return True
        else:
            return False
    except:
        return False

def estaRepetido(estudiante, sinRepetidos):
    """
    Función: Determina si el valor ingresado se repite en memoria.
    Entrada:  Parámetro estudiantes, sinRepetidos.
    Salida: Retorno de banderas True o False.
    """
    for elemento in sinRepetidos:
        if estudiante[0] == elemento[0]:
            return True
    return False

def eliminaRepetidos():
    """
    Funcion: Valida si los datos están repetidos y si es así, los estrae de la lista principal.
    Entrada: N/D
    Salida: N/D (Solo valida y genera un mensaje de retroalimentacion al usuario).
    """
    for estudiante in bitacora:
        if estaRepetido(estudiante, sinRepetidos) == False:
            sinRepetidos.append(estudiante)
    graba(sinRepetidos)

    tit = "Inserta n grupos"
    cont = "Se ha generado la bitácora satisfactoriamente."
    mensajeFrases (tit, cont)
    VentanaPrincipal(tk.NORMAL)
    
def ingresarContenido(estudiantes):
    """
    Funcion: Genera los perfiles o contenido de la bitácora con cada valor necesario y elimina los repetidos de esta misma.
    Entrada: Parámetro estidiantes.
    Salida: Llamado a función eliminaRepetidos.
    """
    cont = 1
    for elemento in bitacora:
        elemento.append(carne())
        elemento.append(generaNombre())
        elemento.append(generaFrase())
        elemento.append(calculaGrupo(cont, estudiantes))
        cont += 1
    return eliminaRepetidos()
       
def cantidadGrupos(pgrupos, pestudiantes):
    """
    Funcion: Genera una determinada cantidad de perfiles según la cantidad de grupos y estudiantes por grupo.
    Entrada: Parámetros pgrupos y pestudiantes.
    Salida: Llama a función ingresarContenido.
    """
    grupos = int(pgrupos)
    estudiantes = int(pestudiantes)
    genBitacora(grupos, estudiantes)
    return ingresarContenido(estudiantes)

sinRepetidos = []

if existeArchivo("BD") == True:
    bitacora = lee("BD")
    sinRepetidos = lee("BD")
else:
    bitacora = []
    sinRepetidos = []
    
diccionario = dict(clasificada)
      
def buscarFraseTupla(frase):
    """
    Funcion:Busca la frase deseada y determian su posición dentro de la bitacora.
    Entrada: Parámetro frase.
    Salida: Retorno de una tupla con las posiciones de la frase.
    """
    cont = 1
    for elemento in clasificada:
        if frase in elemento[1]:
            indiceCat = cont
            indiceFrase = (elemento[1].index(frase)) + 1
            return (indiceCat, indiceFrase)
        cont += 1
    
def crearTuplaNombre(completo):
    """
    Funcion: Genera una tupla con cada nombre completo ingresado eliminando sus espacios.
    Entrada: Parámetro completo.
    Salida: Retorno de la tupla con el nombre.
    """
    lista = completo.split(" ")
    tupla = tuple(lista)
    return tupla

############################ Ingresa 1 Estudiante ############################
def ingresarNombre(nombre):
    """
    Funcion: Valida que el nombre no esté vacío al momento de ser ingresado. (Combobox o Caja deplegable)
    Entrada: Parámetro nombre.
    Salida: Retorno de banderas.
    """
    if nombre == "":
        return False
    else:
        return True

def ingresarCarnet(carnet):
    """
    Funcion: Valida que el carnet ingresado cumpla con el formato establecido, si no. se desecha.
    Entrada: Parámetro carnet.
    Salida: Retorno debanderas True o False.
    """
    if re.search ("^(2017|2018|2019|2020|2021){1}0{1}[1-5]{1}\d{4}$", carnet):
        return True
    else:
        return False
        
def calcularPosFrase(categoria, frase):
    """
    Funcion: Mete en una lista y calcula la posicion de la frase en la bitacora mediante la cateforía y frase juntas.
    Entrada: Parámetros categoria y frase.
    Salida: Retorno de lista con las tuplas de las posiciones.
    """
    for elemento in clasificada:
        if categoria == str(elemento[0]):
            cat = clasificada.index(elemento) + 1
            for i in elemento[1]:
                if frase == i:
                    fr = elemento[1].index(i) + 1
    return (cat, fr)

def arreglaGrupo(pgrupo):
    """
    Funcion: Determina el inio de lectura del parámetro pgrupo en el cuadro desplegable.
    Entrada: Parámetro pgrupo.
    Salida: Retorno de posición.
    """
    return int(pgrupo[-1])

def insertarEstudiante(carne, pnombre, categoria, frase, pgrupo):
    """
    Funcion: Inserta un estudiantes guardando en una lista sus valores uno por uno y validando repetidos.
    Entrada: Parámetros carne, pnombre, categoria, frase y pgrupo
    Salida: Mensaje de retroa limentación al finalizar la inserción.
    """
    nuevoEstudiante = []
    
    carnet = carne
    nombre = pnombre
    nombreCompleto = crearTuplaNombre(nombre)
    catFraseLista = []
    catFrase = calcularPosFrase(categoria, frase)
    catFraseLista.append(catFrase) 
    grupo = arreglaGrupo(pgrupo)

    nuevoEstudiante.append(carnet)
    nuevoEstudiante.append(nombreCompleto)
    nuevoEstudiante.append(catFraseLista)
    nuevoEstudiante.append(grupo)

    sinRepetidos.append(nuevoEstudiante)
    graba(sinRepetidos)
    tit = "Registrado"
    cont = "El estudiante ha sido registrado correctamente."
    mensajeFrases (tit, cont)

######################## Sección agregar frase motivadora #######################
def existeCarnet(carnet):
    """
    Funcion: Valida que el canet ingresado no se repita dentro de la bitacora.
    Entrada: Parámetro carnet.
    Salida: Retorno de función (Bandera True) y Retorno de bandera False.
    """
    for elemento in sinRepetidos:
        if carnet == elemento[0]:
            return sinRepetidos.index(elemento)
    return False

def agregarFrase(confirmacion4, ventana4, carne, categoria, frase):
    """
    Funcion: Agrega una frase a la sublista de frases en bitácora.
    Entrada: Parámetros - carne, categoria, frase.
    Salida: Edita la sublista de frases respectiva en memoria secundaria.
    """
    carnet = carne
    catFrase = calcularPosFrase(categoria, frase)
    indice = existeCarnet(carnet)
    sinRepetidos[indice][2].append(catFrase)
    graba(sinRepetidos)

    confirmacion4.destroy()
    ventana4.destroy()

    tit = "Agregar frase"
    cont = "Se agregó la frase satisfactoriamente."
    mensajeFrases (tit, cont)
    VentanaPrincipal(tk.NORMAL)
        
################################ Sección eliminar ############################
def eliminarEstudiante(confirmaElimar,carne):
    """
    Funcion: Elimina el estudiante indicado de la lista general.
    Entrada: Parámetros - confirmaElimar,carne
    Salida: Edita/elimina el estudiante de memoria secundaria.
    """
    indice = existeCarnet(carne)
    del sinRepetidos[indice]
    graba(sinRepetidos)
    tit="Elimina Estudiante"
    cont="El estudiante ha sido eliminado de la bitacora."
    mensajeFrases(tit,cont)
    confirmaElimar.destroy ()
    eliminar()
        
############################# Sección Tkinter #####################################
# Home Page
def VentanaPrincipal(y):
    """
    Funcion: Despliega la interfaz gráfica del menú principal.
    Entrada: Parámetro - y, estado de los botones.
    Salida: N/D
    """

    if existeArchivo("frasesMotivadoras") == True and existeArchivo("BD") == False:
        x = tk.NORMAL
    else:
        x = tk.DISABLED

    #ventana
    canvas=Canvas(ventana,width= 546,height=536,bg="#212020")
    canvas.place(x=0,y=0)
    
    #Etiquetas
    canvas.create_text((275),50,fill="white",font= "Arial 12 bold",text="Bienvenido, Selecione su opción deseada en el menú desplegable.")
    
    #Botones
    bVentana1 = Button(canvas,text = "Extraer Frases Motivadoras", command = lambda:[determinaFrases()], state = tk.NORMAL)#command = Ventana1) #Se asigna una ventana destino
    bVentana1.place(x=200,y=100)

    bVentana2 = Button(canvas,text = "Insertar n Grupos",command = insertar, state = x)
    bVentana2.place(x=225,y=160)
    
    bVentana3 = Button(canvas,text = "Insertar 1 Estudiante",command = estudiante, state = y)
    bVentana3.place(x=218,y=220)
    
    bVentana4 = Button(canvas,text = "Agregar Frase Motivadora",command = ventana4, state = y)
    bVentana4.place(x=200,y=280)

    bVentana5 = Button(canvas,text = "Eliminar Estudiantes",command = eliminar, state = y)
    bVentana5.place(x=220,y=340)
    
    bVentana6 = Button(canvas,text = "Reportes",command = reporte, state = y)
    bVentana6.place(x=245,y=400)

    bAtras = Button(canvas,text = "   Salir   ",command = lambda: [salirPrincipal(ventana)], state = tk.NORMAL)
    bAtras.place(x=245,y=460)
    
def salirPrincipal(ventana):
    """
    Funcion: Cierra el menú principal / termina el programa.
    Entrada: Parámetro - ventana.
    Salida: N/D
    """
    ventana.destroy()
    
#--------------------------------Insertar n grupos-------------------------------------
#ventanas
def insertar ():
    """
    Funcion: Despliega ventana de insertar n grupos.
    Entrada: Cajas de texto de carnet y nombre.
    Salida: Lleva a la función de validación.
    """
    insertar = Toplevel()
    insertar.minsize(500, 300)
    insertar.resizable(width=NO,height=NO)
    insertar.title("Insertar n Grupos")
    insertar.config( bg= "#212020",cursor="circle")
    
    #Etiquetas
    mensaje = Label(insertar, text="Complete los datos solicitados para insertar una cantidad de")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=20)

    mensaje1 = Label (insertar,text = "grupos de estudiantes deseada.")
    mensaje1.config(font=('Arial 12'))
    mensaje1.config(fg="white",bg="#212020")
    mensaje1.place(x=120,y=40)
    
    cantGrupos = Label (insertar,text = "Cantidad de Grupos:")
    cantGrupos.config(font=('Arial 12'))
    cantGrupos.config(fg="white",bg="#212020")
    cantGrupos.place(x=18,y=100)

    cantEstudiantes = Label (insertar,text = "Cantidad de Estudiantes:")
    cantEstudiantes.config(font=('Arial 12'))
    cantEstudiantes.config(fg="white",bg="#212020")
    cantEstudiantes.place(x=18,y=140)
    
    #Cuadros de texto Ventana 2
    cedula = ttk.Entry(insertar,width=25)
    cedula.place(x=320, y=100)
    
    nombre = ttk.Entry(insertar,width=25)
    nombre.place(x=320, y=140)

    #Botón
    Insert=Button (insertar,text="Insertar n Grupos", command = lambda:[verificaInsertaN(insertar, cedula.get(), nombre.get())]).place(x=200,y=230)

    insertar.mainloop()

def verificaEstu(pestudiantes):
    """
    Funcion: Valida que la entrada de estudiantes sea un entero mayor a 0.
    Entrada: Parámetro - pestudiantes.
    Salida: Booleano.
    """
    try:
        num = int(pestudiantes)
        if num > 0:
            return True
        else:
            return False
    except:
        return False

def verificaInsertaN(insertar, grupos, estudiantes):
    """
    Funcion: Valida las entradas de ingresa n grupos.
    Entrada: Parámetro - insertar, grupos, estudiantes.
    Salida: Mensaje de error o llamada a la función de conexión.
    """
    if verificaNumAux(grupos) == True and verificaEstu(estudiantes) == True:
        cierraVentana(insertar, int(grupos), int(estudiantes))
    else:
        tit = "Valor incorrecto"
        cont = "N grupos debe ser menor a 10 y estudiantes un entero positivo."
        mensajeFrases (tit, cont)
    
def cierraVentana (insertar, pgrupos, pestudiantes):  
    """
    Funcion: Cierra la ventana de insertar n grupos y llama a procesamiento.
    Entrada: Paráetro - insertar, pgrupos, pestudiantes.
    Salida: N/D
    """
    insertar.destroy()
    cantidadGrupos(pgrupos, pestudiantes)

#-----------------------------Insertar un estudiante--------------------------------
def estudiante():
    """
    Funcion: Despliega la ventana para ingresar un estudiante.
    Entrada: Carnet, nombre completo, categoría, frase y grupo.
    Salida: Llama a la función de validación.
    """
    estudiante = Toplevel()
    estudiante.minsize(500,300)
    estudiante.resizable(width=NO,height=NO)
    estudiante.title("Insertar 1 Estudiante")
    estudiante.config( bg= "#212020",cursor="circle")

    #Etiquetas
    mensaje = Label(estudiante, text="Complete los datos solicitados para insertar un estudiante.")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=20)
    
    ecedula = Label(estudiante, text="Ingresar Carné :")
    ecedula.config(font=('Arial 12'))
    ecedula.config(fg="white",bg="#212020")
    ecedula.place(x=18,y=60)
    
    enombre = Label(estudiante, text="Ingresar Nombre y Apellidos :")
    enombre.config(font=('Arial 12'))
    enombre.config(fg="white",bg="#212020")
    enombre.place(x=18,y=100)
    
    ecategoria = Label(estudiante, text="Seleccione Categoría :")
    ecategoria.config(font=('Arial 12'))
    ecategoria.config(fg="white",bg="#212020")
    ecategoria.place(x=18,y=140)
    
    efrase = Label(estudiante, text="Seleccione Frase :")
    efrase.config(font=('Arial 12'))
    efrase.config(fg="white",bg="#212020")
    efrase.place(x=18,y=180)
    
    egrupo = Label(estudiante, text="Seleccione Grupo :")
    egrupo.config(font=('Arial 12'))
    egrupo.config(fg="white",bg="#212020")
    egrupo.place(x=18,y=220)

    #Cuadros de texto
    carne = ttk.Entry(estudiante,width=25)
    carne.place(x=320, y=60)
    
    nombre = ttk.Entry(estudiante,width=25)
    nombre.place(x=320, y=100)

    #Cuadros de selección
    opciones = dict(clasificada)
    opGrupos=defineMayor ()
    opcioneGgrupos = calculaGruposTK(opGrupos)
    
    def on_combobox_select(event):
        """
        Funcion: Establece la conexión para que las frases dependan de la categoría.
        Entrada: Parámetro - event.
        Salida: Cambia los elementos de la segunda caja según la primera.
        """
        frase.set("")
        frase.config(values=opciones[categoria.get()])

    categoria = ttk.Combobox(estudiante, width="45", state="readonly", values=tuple(opciones.keys()))
    categoria. place (x=183,y=140)
    categoria.bind("<<ComboboxSelected>>", on_combobox_select)
    
    frase = ttk.Combobox(estudiante, width="45", state="readonly")
    frase. place (x=183,y=180)

    grupo=ttk.Combobox (estudiante, width="15", state="readonly")
    grupo["values"]=opcioneGgrupos
    grupo. place (x=363,y=220)

    #Botón
    insertEstudiante = Button (estudiante,text="Insertar Estudiante", command = lambda:[verificaEstudiante(estudiante,carne.get(), nombre.get(), categoria.get(), frase.get(), grupo.get())])
    insertEstudiante.place(x=200,y=250)

    estudiante.mainloop()

def verificaEstudiante(estudiante,carne, nombre, categoria,frase, grupo):
    """
    Funcion: Valida todas las entradas de la ventana ingresa un estudiante.
    Entrada: Parámetro - estudiante,carne, nombre, categoria,frase, grupo.
    Salida: Mensajes de error o llama a la función de conexión.
    """
    if categoria != "" and frase != "" and grupo != "":
        if ingresarCarnet(carne) ==True:
            if existeCarnet (carne) ==False:
                if ingresarNombre(nombre) ==True:
                    cierraVentanaEst(estudiante,carne, nombre, categoria,frase, grupo)
                else:
                    tit="Datos incorrectos"
                    cont="El Nombre no coinciden con el formato solicitado."
                    mensajeFrases(tit,cont)
            else:
                tit="Datos incorrectos"
                cont="El Carnét ya existe en la base de datos, ingrese otro."
                mensajeFrases(tit,cont)
        else:
            errorCarnet ()
    else:
        tit="Datos incorrectos"
        cont="Debe ingresar todos los datos solicitados."
        mensajeFrases(tit,cont)

def errorCarnet():
    estudiante = Toplevel()
    estudiante.minsize(500,300)
    estudiante.resizable(width=NO,height=NO)
    estudiante.title("Datos incorrectos")
    estudiante.config( bg= "#212020",cursor="circle")
    
    #Etiquetas
    mensaje = Label(estudiante, text="El Carnet no coinciden con el formato solicitado: 20#-0#-####")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=20)

    formato = Label(estudiante, text="Año - Sede - Aleatorio")
    formato.config(font=('Arial 12'))
    formato.config(fg="white",bg="#212020")
    formato.place(x=20,y=40)
    
    formato = Label(estudiante, text="Año 20## :  2017, 2018, 2019, 2020 y 2021")
    formato.config(font=('Arial 12'))
    formato.config(fg="white",bg="#212020")
    formato.place(x=20,y=60)
    
    formato = Label(estudiante, text="Sede 0# : 01, 02, 03, 04 y 05 ")
    formato.config(font=('Arial 12'))
    formato.config(fg="white",bg="#212020")
    formato.place(x=20,y=100)

    formato = Label(estudiante, text="01- Campus Tecnológico Central Cartago.")
    formato.config(font=('Arial 12'))
    formato.config(fg="white",bg="#212020")
    formato.place(x=20,y=120)

    formato = Label(estudiante, text="02- Campus Tecnológico Local San Carlos.")
    formato.config(font=('Arial 12'))
    formato.config(fg="white",bg="#212020")
    formato.place(x=20,y=140)
                    
    formato = Label(estudiante, text="03- Campus Tecnológico Local San José.")
    formato.config(font=('Arial 12'))
    formato.config(fg="white",bg="#212020")
    formato.place(x=20,y=160)
    
    formato = Label(estudiante, text="04- Centro Académico De Alajuela.")
    formato.config(font=('Arial 12'))
    formato.config(fg="white",bg="#212020")
    formato.place(x=20,y=180)

    formato = Label(estudiante, text="05- Centro Académico De Limón.")
    formato.config(font=('Arial 12'))
    formato.config(fg="white",bg="#212020")
    formato.place(x=20,y=200)
    
def cierraVentanaEst(estudiante,carne, nombre, categoria,frase, grupo):
    """
    Funcion: Cierra la ventana de ingresa un estudiante y llama a procesamiento.
    Entrada: Parámetro - estudiante,carne, nombre, categoria,frase, grupo.
    Salida: Llama a la función de procesamiento.
    """
    estudiante.destroy()
    insertarEstudiante(carne, nombre, categoria,frase, grupo)

#---------------------------Agregar frase motivadora------------------------------
def ventana4 ():
    """
    Funcion: Despliega la ventana agrega frase motivadora.
    Entrada: Carnet, categoría y frase.
    Salida: Llama a la función de validación.
    """
    ventana4 = Toplevel()
    ventana4.minsize(500,300)
    ventana4.resizable(width=NO,height=NO)
    ventana4.title("Agregar frase motivadora")
    ventana4.config( bg= "#212020",cursor="circle")
    
    #Etiquetas
    mensaje = Label(ventana4, text="Complete los datos solicitados para agregar una frase motivadora.")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=20)

    ecedula = Label(ventana4, text="Ingresar Carné :")
    ecedula.config(font=('Arial 12'))
    ecedula.config(fg="white",bg="#212020")
    ecedula.place(x=18,y=100)

    ecategoria = Label(ventana4, text="Seleccione Categoría :")
    ecategoria.config(font=('Arial 12'))
    ecategoria.config(fg="white",bg="#212020")
    ecategoria.place(x=18,y=140)

    efrase = Label(ventana4, text="Seleccione Frase :")
    efrase.config(font=('Arial 12'))
    efrase.config(fg="white",bg="#212020")
    efrase.place(x=18,y=180)

    #Cuadros de texto
    carne = ttk.Entry(ventana4,width=25)
    carne.place(x=320, y=100)

    #Cuadros de selección
    opciones = dict(clasificada)
    
    def on_combobox_select(event):
        """
        Funcion: Establece la conexión para que las frases dependan de la categoría.
        Entrada: Parámetro - event.
        Salida: Cambia los elementos de la segunda caja según la primera.
        """
        frase.set("")
        frase.config(values=opciones[categoria.get()])

    categoria = ttk.Combobox(ventana4, width="45", state="readonly", values=tuple(opciones.keys()))
    categoria. place (x=183,y=140)
    categoria.bind("<<ComboboxSelected>>", on_combobox_select)
    
    frase = ttk.Combobox(ventana4, width="45", state="readonly")
    frase. place (x=183,y=180)

    #Botón
    insertFrase = Button (ventana4,text="Insertar Frase",command = lambda:[validaEntradaFrases(ventana4, carne.get(), categoria.get(), frase.get())])
    insertFrase.place(x=200,y=250)
        
    ventana4.mainloop()

def seEncuentraCarnet(carne):
    """
    Funcion: Busca un determinado carnet en la memoria secundaria.
    Entrada: Parámetro - carne.
    Salida: Booleano.
    """
    for elemento in sinRepetidos:
        if carne == elemento[0]:
            return True
    return False

def validaEntradaFrases(ventana4, carne, categoria, frase):
    """
    Funcion: Valida las entradas de la ventana agregar 
    Entrada: Parámetro - ventana4, carne, categoria, frase.
    Salida: Mensaje o llama a la función de confirmación.
    """
    if categoria != "" or frase != "":
        if ingresarCarnet(carne) == True:
            if seEncuentraCarnet(carne) == True:
                confirmacion4 (ventana4, carne, categoria, frase)
            else:
                tit = "No se encuentra"
                cont = "El carne ingresado no se encuentra registrado en la BD."
                mensajeFrases (tit, cont)
        else:
            errorCarnet ()
    else:
        tit = "Formato incorrecto"
        cont = "Se deben completar todos los datos."
        mensajeFrases (tit, cont)
    
    
# Eliminación de ventana anteriór
def insertFraseAux (ventana4, carne, categoria, frase):
    """
    Funcion: Cierra la ventana de insertar frase y llama a confirmación.
    Entrada: Parámetro - ventana4, carne, categoria, frase
    Salida: Llama a la función de confirmación.
    """
    ventana4.destroy()
    confirmacion4 (carne, categoria, frase)
    
#Ventana de confirmación 
def confirmacion4 (ventana4, carne, categoria, frase):
    """
    Funcion: Despliega una ventana de confirmación.
    Entrada: Parámetro - ventana4, carne, categoria, frase.
    Salida: Llama a la función de procesamiento.
    """
    confirmacion4 = Toplevel()
    confirmacion4.minsize(235,70)
    confirmacion4.resizable(width=NO,height=NO)
    confirmacion4.title("Confirmación")
    confirmacion4.config( bg= "#212020",cursor="circle")

    #Etiquetas
    mensaje = Label(confirmacion4, text="¿Desea Insertar este usuario ?")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=5,y=20)

    #Botón
    si = Button (confirmacion4,text="   Sí    ",command = lambda: agregarFrase(confirmacion4, ventana4, carne, categoria, frase))
    si.place(x=50,y=100)

    no = Button (confirmacion4,text="   No   ",command = lambda: atras4(confirmacion4))
    no.place(x=150,y=100)

    confirmacion4.mainloop()

def atras4 (confirmacion4):
    """
    Funcion: Cierra la ventana de confirmación.
    Entrada: Parámetro - confirmacion4.
    Salida: Muestra un mensaje.
    """
    confirmacion4.destroy()
    tit = ""
    cont = "no se realizaron cambios."
    mensajeFrases (tit, cont)
    
#----------------------------------------Eliminar----------------------------------------
def eliminar ():
    """
    Funcion: Elimina el estudiante indicado según el carnet respectivo.
    Entrada: Carnet.
    Salida: Llama a la función de validar.
    """
    eliminar = Toplevel()
    eliminar.minsize(500,70)
    eliminar.resizable(width=NO,height=NO)
    eliminar.title("Eliminar Estudiante")
    eliminar.config( bg= "#212020",cursor="circle")

    #Etiquetas
    mensaje = Label(eliminar, text="Complete los datos solicitados para eliminar un estudiante.")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=20)

    ecedula = Label(eliminar, text="Ingresar Carné :")
    ecedula.config(font=('Arial 12'))
    ecedula.config(fg="white",bg="#212020")
    ecedula.place(x=18,y=70)
    
    #Cuadros de texto
    carne = ttk.Entry(eliminar,width=25)
    carne.place(x=320, y=70) 

    #Botón
    elimEstudiante = Button (eliminar,text="eliminar Estudiante",command= lambda: validaEliminar(eliminar, carne.get()))
    elimEstudiante.place(x=200,y=130)
    
    eliminar.mainloop()

def validaEliminar (eliminar,carne):
    """
    Funcion: Valida las entradas de la ventana eliminar estudiante.
    Entrada: Parámetro - eliminar,carne.
    Salida: Mensaje o llamada de la función de conexión.
    """
    if carne !="":
        if ingresarCarnet(carne) ==True:
            if existeCarnet (carne) != True:
                    elimEstudianteAux(eliminar,carne)
            else:
                tit="Datos desconocidos"
                cont="El Carnet no existe en la base de datos."
                mensajeFrases(tit,cont)
        else:
            errorCarnet ()
    else:
        tit="Datos desconocidos"
        cont="Ingrese los datos solicitados."
        mensajeFrases(tit,cont)
        
# Eliminación de ventana anteriór
def elimEstudianteAux (eliminar, carne):
    """
    Funcion: Cierra la ventana de eliminar y llama a confirmar.
    Entrada: Parámetro - eliminar, carne.
    Salida: Llama a la función de confirmar.
    """
    eliminar.destroy()
    confirmaElimar (carne)
    
#Ventana de confirmación 
def confirmaElimar (carne):
    """
    Funcion: Despliega la ventana de confirmación.
    Entrada: Parámetro - carne.
    Salida: Llama a la función de procesamiento.
    """
    
    confirmaElimar = Toplevel()
    confirmaElimar.minsize(235,70)
    confirmaElimar.resizable(width=NO,height=NO)
    confirmaElimar.title("Confirmación")
    confirmaElimar.config( bg= "#212020",cursor="circle")

    #Etiquetas
    mensaje = Label(confirmaElimar, text="¿Desea Insertar este usuario ?")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=5,y=20)

    #Botón
    si = Button (confirmaElimar,text="   Sí    ",command = lambda: eliminarEstudiante(confirmaElimar,carne))
    si.place(x=50,y=100)
    

    no = Button (confirmaElimar,text="   No   ",command = lambda: atrasElim(confirmaElimar))
    no.place(x=150,y=100)

    confirmaElimar.mainloop()

def atrasElim (confirmaElimar):
    """
    Funcion: Cierra la ventana de confirmar y llama a procesamiento.
    Entrada: Parámetro - confirmaElimar.
    Salida: Llama a la función de procesamiento.
    """
    confirmaElimar.destroy()
    eliminar ()
    
#------------------------------------Reporte-----------------------------------
def reporte ():
    """
    Funcion: Despliega la ventana de reporte.
    Entrada: N/D
    Salida: Llama a las ventanas respectivas.
    """
    reporte = Toplevel()
    reporte.minsize(500,300)
    reporte.resizable(width=NO,height=NO)
    reporte.title("Reporte")
    reporte.config( bg= "#212020",cursor="circle")

    #Etiquetas
    mensaje = Label(reporte, text="Elija una de las opciones mostradas.")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=20)

    #Botón
    categoria = Button (reporte,text="Por Categoría de frase",command=lambda: categoriaAux(reporte))
    categoria.place(x=50,y=130)

    grupo = Button (reporte,text="Por Grupo",command=lambda: porGrupoAux(reporte))
    grupo.place(x=220,y=130)
    
    catyFrase = Button (reporte,text="Por Categoría y frase",command=lambda: categoriaFraseAux(reporte))
    catyFrase.place(x=320,y=130)
    
    total = Button (reporte,text="Total de frases",command=lambda: totalFrasesAux(reporte))
    total.place(x=220,y=230)
    
    bitacora = Button (reporte,text="Imprimir  bitácora estudiantil",command=lambda: bitacoraEstAux(reporte))
    bitacora.place(x=30,y=230)

    batrasr = Button (reporte,text="Atras",command=lambda: atrasrAux(reporte))
    batrasr.place(x=370,y=230)
                
# Eliminación de ventana anteriór
def categoriaAux (reporte):
    """
    Funcion: Cierra la ventana de reporte y llama a la ventana respectiva.
    Entrada: Parámetro - reporte.
    Salida: Llama a la función de procesamiento.
    """
    reporte.destroy()
    rCategoria ()

def porGrupoAux (reporte):
    """
    Funcion: Cierra la ventana de reporte y llama a la ventana respectiva.
    Entrada: Parámetro - reporte.
    Salida: Llama a la función de procesamiento.
    """
    reporte.destroy()
    porGrupo()

def categoriaFraseAux (reporte):
    """
    Funcion: Cierra la ventana de reporte y llama a la ventana respectiva.
    Entrada: Parámetro - reporte.
    Salida: Llama a la función de procesamiento.
    """
    reporte.destroy()
    categoriaFrase()
    
def totalFrasesAux (reporte):
    """
    Funcion: Cierra la ventana de reporte y llama a la ventana respectiva.
    Entrada: Parámetro - reporte.
    Salida: Llama a la función de procesamiento.
    """
    reporte.destroy()
    totalFrasesPDF()

def bitacoraEstAux (reporte):
    """
    Funcion: Cierra la ventana de reporte y llama a la ventana respectiva.
    Entrada: Parámetro - reporte.
    Salida: Llama a la función de procesamiento.
    """
    reporte.destroy()
    bitacoraEstAux1(reporte)
    
def atrasrAux (reporte):
    """
    Funcion: Cierra la ventana de reporte y llama a la ventana respectiva.
    Entrada: Parámetro - reporte.
    Salida: Llama a la función de procesamiento.
    """
    reporte.destroy()

#--------------------------------Opciones de Reporte-----------------------------
def mensajeFrases (tit, cont):
    """
    Funcion: Muestra un mensaje respectivo.
    Entrada: Parámetro - tit, cont.
    Salida: Muestra el mensaje.
    """
    totalFrases = Toplevel()
    totalFrases.minsize(500,150)
    totalFrases.resizable(width=NO,height=NO)
    totalFrases.title(tit)
    totalFrases.config( bg= "#212020",cursor="circle")
    
    #Etiquetas
    mensaje = Label(totalFrases, text=cont)
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=75)

def determinaFrases():
    """
    Funcion: Valida si el botón extraer frases se vuelve a ejecutar.
    Entrada: N/D
    Salida: Muestra el mensaje.
    """
    if existeArchivo("frasesMotivadoras") == True:
        mensajeFrases ("Extraer frases", "Ya existe un archivo de frases creado.")
    else:
        tit = "Extraer frases"
        cont = "Las frases se han extraído satisfactoriamente."
        mensajeFrases (tit, cont)
        ejecutar()
        VentanaPrincipal(tk.DISABLED)
    
def rCategoria ():
    """
    Funcion: Despliega la ventana de reporte por categoría.
    Entrada: Categoría.
    Salida: Llama a la función de conexión.
    """
    rCategoria = Toplevel()
    rCategoria.minsize(500,150)
    rCategoria.resizable(width=NO,height=NO)
    rCategoria.title("Por Categoría de frase")
    rCategoria.config( bg= "#212020",cursor="circle")

    #Etiquetas
    mensaje = Label(rCategoria, text="Seleccione Categoría :")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=18,y=80)
    
    mensaje2 = Label(rCategoria, text="Selecciones la categoría de frase para generar un reporte.")
    mensaje2.config(font=('Arial 12')) 
    mensaje2.config(fg="white",bg="#212020")
    mensaje2.place(x=20,y=20)

    #Cuadros de selección
    opciones = dict(clasificada)
    categoria = ttk.Combobox(rCategoria, width="45", state="readonly", values=tuple(opciones.keys()))
    categoria. place (x=183,y=80)

    #Botón
    bcategoria = Button (rCategoria,text="Generar reporte",command=lambda: mensajeHTML1(rCategoria,categoria.get() ))
    bcategoria.place(x=200,y=140)
    
    rCategoria.mainloop()
    
def mensajeHTML1 (rCategoria,categoria):
    """
    Funcion: Muestra mensaje y llama a la función de procesamiento.
    Entrada: Parámetro - rCategoria,categoria.
    Salida: Llama a la función de procesamiento.
    """
    opcionHTML1(categoria)
    tit = "Aviso de Reporte"
    cont = "El reporte se ha creado satisfactoriamente ."
    mensajeFrases (tit, cont)
    rCategoria.destroy ()
    reporte ()
    
#--------------------------------------------------------------------------------------------------------
def porGrupo ():
    """
    Funcion: Despliega la ventana de reporte por grupo.
    Entrada: Grupo.
    Salida: Llamada a la función de validación.
    """
    porGrupo = Toplevel()
    porGrupo.minsize(500,150)
    porGrupo.resizable(width=NO,height=NO)
    porGrupo.title("Por grupo")
    porGrupo.config( bg= "#212020",cursor="circle")

    #Etiquetas
    mensaje = Label(porGrupo, text="Seleccione grupo :")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=18,y=80)
    
    mensaje2 = Label(porGrupo, text="Selecciones la categoría de frase para generar un reporte.")
    mensaje2.config(font=('Arial 12')) 
    mensaje2.config(fg="white",bg="#212020")
    mensaje2.place(x=20,y=20)

    #Cuadros de selección
    opGrupos=defineMayor ()
    opcioneGgrupos = calculaGruposTK(opGrupos)

    grupo=ttk.Combobox (porGrupo, width="15", state="readonly")
    grupo["values"]=opcioneGgrupos
    grupo. place (x=363,y=80)

    #Botón
    bgrupo = Button (porGrupo,text="Generar reporte",command=lambda: validarHTML2(porGrupo,grupo.get(),sinRepetidos) )
    bgrupo.place(x=200,y=140)
    
    porGrupo.mainloop()
    
def validarHTML2(porGrupo,grupo, sinRepetidos):
    """
    Funcion: Valida que la entrada grupo no sea vacía.
    Entrada: Parámetro - porGrupo,grupo, sinRepetidos.
    Salida: Mensaje o llama a la función de conexión.
    """
    if grupo == "":
        tit = "Datos erróneos"
        cont = "Debe selecionar una opción de grupo."
        mensajeFrases (tit, cont)
    else:
        mensajeHTML2(porGrupo,grupo, sinRepetidos)

def mensajeHTML2(porGrupo,grupo, sinRepetidos):
    """
    Funcion: Cierra la ventana de reporte por grupo y llama a procesamiento.
    Entrada: Parámetro - porGrupo,grupo, sinRepetidos.
    Salida: Llama a la función de procesamiento.
    """
    porGrupo.destroy ()
    tit = "Aviso de Reporte"
    cont = "El reporte se ha creado satisfactoriamente ."
    mensajeFrases (tit, cont)
    reporte ()
    opcionHTML2(grupo, sinRepetidos)
    
#------------------------------------------------------------------------------------------------------------------------------
def categoriaFrase ():
    """
    Funcion: Despliega la ventana de reporte por frase.
    Entrada: Categoría y frase.
    Salida: Llama a la función de validación.
    """
    categoriaFrase = Toplevel()
    categoriaFrase.minsize(500,150)
    categoriaFrase.resizable(width=NO,height=NO)
    categoriaFrase.title("Por Categoría de frase")
    categoriaFrase.config( bg= "#212020",cursor="circle")

    #Etiquetas
    mensaje = Label(categoriaFrase, text="Complete los datos solicitados para generar el reporte.")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=20)

    ecategoria = Label(categoriaFrase, text="Seleccione Categoría :")
    ecategoria.config(font=('Arial 12'))
    ecategoria.config(fg="white",bg="#212020")
    ecategoria.place(x=18,y=60)

    efrase = Label(categoriaFrase, text="Seleccione Frase :")
    efrase.config(font=('Arial 12'))
    efrase.config(fg="white",bg="#212020")
    efrase.place(x=18,y=100)
    
    #Cuadros de selección
    opciones = dict(clasificada)
    
    def on_combobox_select(event):
        """
        Funcion: Establece la conexión para que las frases dependan de la categoría.
        Entrada: Parámetro - event.
        Salida: Cambia los elementos de la segunda caja según la primera.
        """
        frase.set("")
        frase.config(values=opciones[categoria.get()])

    categoria = ttk.Combobox(categoriaFrase, width="45", state="readonly", values=tuple(opciones.keys()))
    categoria. place (x=183,y=60)
    categoria.bind("<<ComboboxSelected>>", on_combobox_select)
    
    frase = ttk.Combobox(categoriaFrase, width="45", state="readonly")
    frase. place (x=183,y=100)

    #Botón
    bgrupo = Button (categoriaFrase,text="Generar reporte",command=lambda: validarHTML3(categoriaFrase,categoria.get(), frase.get()) )
    bgrupo.place(x=200,y=140)
    
    categoriaFrase.mainloop()
    
def validarHTML3(categoriaFrase,categoria,frase):
    """
    Funcion: Valida las entradas de la ventana reporte por frase.
    Entrada: Parámetro - categoriaFrase,categoria,frase.
    Salida: Llama a la función de procesamiento.
    """
    if categoria == "" or frase == "":
        tit = "Datos erróneos"
        cont = "Debe selecionar una opción de grupo."
        mensajeFrases (tit, cont)
    else:
        mensajeHTML3(categoriaFrase,categoria,frase)

def mensajeHTML3(categoriaFrase,categoria,frase):
    """
    Funcion: Muestra mensaje y llama a la función de procesamiento.
    Entrada: Parámetro - categoriaFrase,categoria,frase.
    Salida: Llama a la función de procesamiento.
    """
    opcionHTML3(categoria,frase)
    tit = "Aviso de Reporte"
    cont = "El reporte se ha creado satisfactoriamente ."
    mensajeFrases (tit, cont)
    categoriaFrase.destroy ()
    reporte ()
    
#--------------------------------------------------------------------------------------------------------
def totalFrasesPDF ():
    """
    Funcion: Muestra un mensaje de confirmación del reporte PDF y llama a procesamiento.
    Entrada: N/D
    Salida: Muestra el mensaje.
    """
    totalFrasesPDF = Toplevel()
    totalFrasesPDF.minsize(500,150)
    totalFrasesPDF.resizable(width=NO,height=NO)
    totalFrasesPDF.title("Total de Frases")
    totalFrasesPDF.config( bg= "#212020",cursor="circle")
    
    #Etiquetas
    mensaje = Label(totalFrasesPDF, text="Su reporte se ha creado en un PDF en la carpeta principal.")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=75)
    generaPDF ()
    
#--------------------------------------------------------------------------------------------------------
def bitacoraEst ():
    """
    Funcion: Muestra un mensaje de confirmación del reporte CSV y llama a procesamiento.
    Entrada: N/D
    Salida: Muestra el mensaje.
    """
    bitacoraEst = Toplevel()
    bitacoraEst.minsize(500,150)
    bitacoraEst.resizable(width=NO,height=NO)
    bitacoraEst.title("Imprimir bitácora estudiantil")
    bitacoraEst.config( bg= "#212020",cursor="circle")
    
    #Etiquetas
    mensaje = Label(bitacoraEst, text="Su reporte se ha creado en un Exel en la carpeta principal.")
    mensaje.config(font=('Arial 12'))
    mensaje.config(fg="white",bg="#212020")
    mensaje.place(x=20,y=75)
    crearCSV2()
    
def bitacoraEstAux1(reporte):
    """
    Funcion: Verifica si existe un archivo CSV para eliminarlo.
    Entrada: Parámetro - reporte.
    Salida: Llama a la función de procesamiento.
    """
    if existeArchivoCsv("bitacora.csv") == True:
        remove("bitacora.csv")
    bitacoraEst ()
    
#--------------------------------Principal-------------------------------------------
if __name__ == '__main__':
    ventana = Tk()  
    ventana.title("  ") 
    ventana.minsize(550, 540)
    ventana.resizable(width=NO, height=NO)
    ventana.config(bg="blue")
    ventana.overrideredirect(True)

    if existeArchivo("frasesMotivadoras") == True and existeArchivo("BD") == True:
        y = tk.NORMAL
    else:
        y = tk.DISABLED
    
    VentanaPrincipal(y)
