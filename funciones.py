#Elaborado por: Needler Bonilla Serrano
#               Jose Pablo Agüero Mora
#Fecha de Creación: 14/10/2021 3:00pm 
#Fecha de última Modificación: 03/11/2021 10:30am
#Versión: 3.9.6

# Importe de librerías
import csv
from fpdf import FPDF
import random
from datetime import datetime
from archivos import *

# Definición de funciones:

################################# Templates ###############################
template1 = """
<center>
    <h1>----------</h1>
    <table border width="50%">
        <tr>
            <th colspan=6 style= "font-size:150%">Reporte Bitácora - Por categoría de frase</th>
        </tr>
        <tr>
            <td style="font-size:150%">Número de grupo</td> <td style="font-size:150%">Carnet</td> <td style="font-size:150%">Nombre completo</td> <td style="font-size:150%">Frases</td>
        </tr>
"""

template2 = """
<center>
    <h1>----------</h1>
    <table border width="50%">
        <tr>
            <th colspan=6 style= "font-size:150%">Reporte bitácora - Por grupo</th>
        </tr>
        <tr>
            <td style="font-size:150%">Carnet</td> <td style="font-size:150%">Nombre completo</td> <td style="font-size:150%">Frases</td>
        </tr>
"""
template3 = """
<center>
    <h1>----------</h1>
    <table border width="50%">
        <tr>
            <th colspan=6 style= "font-size:150%">Reporte bitácora - Por categorías y frase</th>
        </tr>
        <tr>
            <td style="font-size:150%">Número de grupo</td> <td style="font-size:150%">Carnet</td> <td style="font-size:150%">Nombre completo</td>
        </tr>
"""
############################### Fin Templates ##############################

################################ Agrega filas ##############################
def agregaFilas1(lista):
    """
    Función: Agrega las filas de la tabla con sus respectivos valores.
    Entrada: Parámetro - (lista) Matriiz con todos los datos y
    (indice) que es el indicador de la columna.
    Salida: Edición del contenido HMTL.
    """
    content = """
        <tr>"""
    content += """
            <td>"""+str(lista[3])+"</td>"+" <td>"+str(lista[0])+"</td>"+" <td>"+str(lista[1])+"</td>"+" <td>"+str(lista[2])+"</td>"
    content += """
        </tr>"""
    return content

def agregaFilas2(lista):
    """
    Función: Agrega las filas de la tabla con sus respectivos valores.
    Entrada: Parámetro - (lista) Matriiz con todos los datos y
    (indice) que es el indicador de la columna.
    Salida: Edición del contenido HMTL.
    """
    content = """
        <tr>"""
    content += """
            <td>"""+str(lista[0])+"</td>"+" <td>"+str(lista[1])+"</td>"+" <td>"+str(lista[2])+"</td>"
    content += """
        </tr>"""
    return content

def agregaFilas3(lista):
    """
    Función: Agrega las filas de la tabla con sus respectivos valores.
    Entrada: Parámetro - (lista) Matriiz con todos los datos y
    (indice) que es el indicador de la columna.
    Salida: Edición del contenido HMTL.
    """
    content = """
        <tr>"""
    content += """
            <td>"""+str(lista[3])+"</td>"+" <td>"+str(lista[0])+"</td>"+" <td>"+str(lista[1])+"</td>"
    content += """
        </tr>"""
    return content

def agregaEtiquetas():
    """
    Función: Agrega las líneas finales del HTML.
    Entrada: N/D
    Salida: Variable con las etiquetas.
    """
    content = """
    </table>
    <h1>----------</h1>
</center>"""
    return content

def grabaFinal(content, nombreArchivo):
    """
    Función: Abre el documento HTML y agrega todos los elemento dentro del documento.
    Entrada: Parámetro - (content) Contenido acumulado hasta el momento.
    Salida: N/D
    """
    with open(nombreArchivo, "w") as file:
        file.write(content)
############################# Fin Agrega filas ###########################

############################## Ciclo filas ###############################
def crearHTML(nombreArchivo, template):
    """
    Función: Crea un HTML y determina las pocisiones de las sublistas dentro del mismo.
    Entrada: N/D
    Salida: Documento HTML Con todos los elementos de SubLista.
    """
    f = open(nombreArchivo, 'w')
    html_template = template
    f.write(html_template) 
    f.close()

def leer2(nombreArchivo):   
    """
    Función: Lee el contenido del HTML
    Entrada:N/D
    Salida: Retorno de variable content
    """
    with open(nombreArchivo, "r") as file:
        content = file.read()
        return content

def cicloFilas1(nombreArchivo, plista):
    """
    Función: Se encarga de llenar cada celda de la planilla con elementos deseados de la lista.
    Entrada: Parámetro lista.
    Salida: N/D
    """
    content = leer2(nombreArchivo)
    contador = 0
    while contador < len(plista):
        actual = nuevaBitacora(plista[contador])
        content += agregaFilas1(actual)
        contador += 1

    content += agregaEtiquetas()
    grabaFinal(content, nombreArchivo)

def cicloFilas2(nombreArchivo, plista):
    """
    Función: Se encarga de llenar cada celda de la planilla con elementos deseados de la lista.
    Entrada: Parámetro lista.
    Salida: N/D
    """
    content = leer2(nombreArchivo)
    contador = 0
    while contador < len(plista):
        actual = nuevaBitacora(plista[contador])
        content += agregaFilas2(actual)
        contador += 1

    content += agregaEtiquetas()
    grabaFinal(content, nombreArchivo)

def cicloFilas3(nombreArchivo, plista):
    """
    Función: Se encarga de llenar cada celda de la planilla con elementos deseados de la lista.
    Entrada: Parámetro lista.
    Salida: N/D
    """
    content = leer2(nombreArchivo)
    contador = 0
    while contador < len(plista):
        actual = nuevaBitacora(plista[contador])
        content += agregaFilas3(actual)
        contador += 1

    content += agregaEtiquetas()
    grabaFinal(content, nombreArchivo)
############################# Fin Ciclo filas ##############################

################################# CSV ######################################
def crearCSV2():
    """
    Funcion: Crea un archivo exel donde se almacenan los datos de estudiante.
    Entradas: N/D
    Salidas: Documento exel.
    """
    with open ("bitacora.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        subtitulos = [["Carnet","Nombre Completo","Frase","Grupo"]]
        writer.writerows(subtitulos)
        nuevaLista = cicloNuevaBitacora()
        writer.writerows(nuevaLista)

########################### Interpretar datos #############################
def formulaGrupo(grupo):
    """
    Funcion: Genera un dato tipo string o de texto de frupo ingresado.
    Entradas: Parámetro grupo.
    Salidas: Retorno de string.
    """
    string = "Grupo " + str(grupo)
    return string

def formulaFrase(tupla):
    """
    Funcion: Calcula el indice de la frase.
    Entradas: Parámetro tupla.
    Salidas: Retorno ultima
    """
    ultima = []
    for elemento in tupla:
        cat = elemento[0] - 1
        frase = elemento[1] - 1
        final = clasificada[cat][1][frase]
        ultima.append(final)
    return ultima
    
def formulaNombre(tupla):
    """
    Funcion: Determina la posición de l nombre 
    Entradas: Parámetrp tupla.
    Salidas:  Retorno de ubicación de nombre.
    """
    nombreF = ""
    for palabra in tupla:
        nombreF += palabra + " "
    nombreF = nombreF[:-1]
    return nombreF.title()

def nuevaBitacora(sublista):
    """
    Funcion: Genera una lista con todos los elementos de estudiantes.
    Entradas: Parámetro sublista.
    Salidas: Retrona lista Nueva.
    """
    nueva = []
    carnet = sublista[0]
    nombre = formulaNombre(sublista[1])
    frase = formulaFrase(sublista[2])
    grupo = formulaGrupo(sublista[3])

    nueva.append(carnet)
    nueva.append(nombre)
    nueva.append(frase)
    nueva.append(grupo)
    return nueva

def cicloNuevaBitacora():
    """
    Funcion: Agrega cada elemento de la base de datos a la lista Nueva.
    Entradas: N/D
    Salidas: Retorno de list Nueva
    """
    modulo = lee("BD")
    nueva = []
    for elemento in modulo:
        editada = nuevaBitacora(elemento)
        nueva.append(editada)
    return nueva

def estaLaTupla(pcate, pelemento):
    """
    Funcion: Determina si la tupla es la correcta.
    Entradas: Parámetros pcate y pelemento.
    Salidas: Reotrno de Banderas True y False.
    """
    interno = 0
    for i in pelemento:
        if pcate == i:
            return interno
        interno += 1
    return False
        
def calculaFraseFinal(cate, frase):
    """
    Funcion: Calcula la posición de la frase y la categoría.
    Entradas: Parámetro cate y frase
    Salidas: Retorno de posición de frase y categoría.
    """
    try:
        for elemento in clasificada:
            if estaLaTupla(frase, elemento[1]) != False:
                interno = estaLaTupla(frase, elemento[1])
                externo = clasificada.index(elemento)
        return (externo, interno)
    except:
        ext = calculaCate(cate)
        frase = 0
        return (ext, frase)

def calculaCate(cate):
    """
    Funcion: Busca una categoría en la lista de clasificadas.
    Entradas:  Parámetro cate.
    Salidas:  Llamado a función.
    """
    for elemento in clasificada:
        if cate == elemento[0]:
            return clasificada.index(elemento)

############################# Opciones HTML ############################
def opcionHTML1(cate):
    """
    Función: Incluye todos los procesos necesarios a realizar cuando se
    elige la opción Generar documento HTML.
    Entrada: Parámetro - (lista) Lista tokenizada y procesada.
    Salida: Realiza los procesos para crear y escribir automáticamente
    en el archivo HTML.
    """
    crearHTML("reporte_por_categoria.html", template1)
    plista = clasCategoriaAux(cate)
    cicloFilas1("reporte_por_categoria.html", plista)
    return ""

def opcionHTML2(grupo, sinRepetidos):
    """
    Función: Incluye todos los procesos necesarios a realizar cuando se
    elige la opción Generar documento HTML.
    Entrada: Parámetro - (lista) Lista tokenizada y procesada.
    Salida: Realiza los procesos para crear y escribir automáticamente
    en el archivo HTML.
    """
    crearHTML("reporte_por_grupo.html", template2)
    plista = clasGrupoAux(grupo, sinRepetidos)
    cicloFilas2("reporte_por_grupo.html", plista)
    return ""

def opcionHTML3(categoria,frase):
    """
    Función: Incluye todos los procesos necesarios a realizar cuando se
    elige la opción Generar documento HTML.
    Entrada: Parámetro - (lista) Lista tokenizada y procesada.
    Salida: Realiza los procesos para crear y escribir automáticamente
    en el archivo HTML.
    """
    crearHTML("reporte_por_frase.html", template3)
    plista = clasFraseAux(categoria,frase)
    cicloFilas3("reporte_por_frase.html", plista)
    return ""

####################### Algoritmos de clasificación listas ###################
def seIngresa(elemento, categoria):
    """
    Funcion:  Busca la frese en la categoría seleccionada.
    Entradas: Parámetro elemento y categoria.
    Salidas: Retorno de banderas True o False.
    """
    for frase in elemento[2]:
        if frase[0] == categoria+1:
            return True
    return False

def clasCategoria(categoria):
    """
    Funcion: Lee la base de datos y determina si la categoría se encuentra en su interior.
    Entradas: Parámetro categoria.
    Salidas: Lista Nueva.
    """
    modulo = lee("BD")
    nueva = []
    for elemento in modulo:
        if seIngresa(elemento, categoria) == True:
            nueva.append(elemento)
    return nueva

def clasCategoriaAux(cate):
    """
    Funcion: Determina que la categoría se encuentra en la BD.
    Entradas: Parámetro cate.
    Salidas: Retorno afunción.
    """
    categoria = calculaCate(cate)
    return clasCategoria(categoria)
    
def clasGrupo(grupo, sinRepetidos):
    """
    Funcion: Busca el grupo en la base de datos.
    Entradas: Parámetros grupo y sinRepetidos.
    Salidas: Retorno de lista con los grupos encontrados.
    """ 
    if sinRepetidos == []:
        modulo = lee("BD")
    else:
        modulo = sinRepetidos
        
    nueva = []
    for elemento in modulo:
        if elemento[3] == grupo:
            nueva.append(elemento)
    return nueva

def clasGrupoAux(grupo, sinRepetidos):
    """
    Funcion: Determina sin el grupo se encuentra en la lista y si se repite.
    Entradas: Parámetros grupo y sinRepetidos.
    Salidas: Retorno a llamado de función.
    """
    num=grupo[-1]
    return clasGrupo(int(num), sinRepetidos)

def seAgrega(elemento, tupla):
    """
    Funcion: Determina si la frse es la misma a la tupla.
    Entradas: Parámetros elemento y tupla.
    Salidas: Retorno de banderas.
    """
    for frase in elemento[2]:
        if frase == tupla:
            return True
    return False

def clasFrase(tupla):
    """
    Funcion: Busca dentro de la base de datos y meter en una lista las categorías y frases.
    Entradas: Parámetro tupla.
    Salidas: Retornode lista.
    """
    modulo = lee("BD")
    nueva = []
    for elemento in modulo:
        confir = seAgrega(elemento, tupla)
        if seAgrega(elemento, tupla) == True:
            nueva.append(elemento)
    return nueva

def clasFraseAux(categoria,frase):
    """
    Funcion: Esxtrae cada elemento  (categoría y frase) de la lista y los guada en una tupla.
    Entradas:Parámetro categoria y frase
    Salidas: Retorno de tupla.
    """
    listaT = []
    total=calculaFraseFinal(categoria,frase)
    cat = total[0]+1
    listaT.append(cat)
    frase = total[1]+1
    listaT.append(frase)
    tup = tuple(listaT)
    return clasFrase(tup)

################## PDF ###############
def generaNombre():
    """
    Función: Genera el nombre del archivo PDF.
    Entrada: N/D
    Salida: Nombre con la fecha y la hora específica.
    """
    completo = ""
    now = datetime.now()
    dia = str(now.day)
    mes = str(now.month)
    anno = str(now.year)
    hora = str(now.hour)
    minuto = str(now.minute)
    seg = str(now.second)

    completo += "Frases-"+dia+"-"+mes+"-"+anno+"-"+hora+"-"+minuto+"-"+seg+".pdf"
    return completo

def eliminaRepTuplas(frasesT):
    """
    Funcion: Valida que los elemetos no estén duplicados y los guada en una lista.
    Entradas: Parámetro frasesT.
    Salidas: Lista con las tuplas de categoría y frase.
    """
    nuevo = []
    for elemento in frasesT:
        if elemento not in nuevo:
            nuevo.append(elemento)
    return nuevo

def clasificarPdf():
    """
    Funcion: Clasifica los datos de los estudiantes en una lista
    Entradas: N/D
    Salidas: Lista Nueva con los datos de cada estudiante.
    """
    nuevaLista = []
    frasesT = []
    for elemento in sinRepetidos:
        for tupla in elemento[2]:
            frasesT.append(tupla)
    dupFrasesT = eliminaRepTuplas(frasesT)

    for i in dupFrasesT:
        actual = []
        indice = i[0] - 1
        clas = clasificada[indice][0]
        iFras = i[1] - 1
        frase = clasificada[indice][1][iFras]
        actual.append(clas)
        actual.append(frase)
        nuevaLista.append(actual)
    return nuevaLista

def generaListasPDF():
    """
    Funcion: Clasifica las categorías y frases en una lista de listas eliminando caracteres ascii.
    Entradas: N/D
    Salidas: Lisa con todas las categorías y sus frases.
    """
    listaEntera=[]
    for elemento in clasificada:
        actual=[]
        actual.append(elemento[0])
        listaFrases=[]
        for i in elemento[1]:
            if i==' Muchas gracias por haber….(cuando es algo positivo) .' :
                i=i.replace(u"…",u" ")
            listaFrases.append(i)
        actual.append(listaFrases)
        listaEntera.append(actual)
    return listaEntera
        
def colorRandom ():
    """
    Funcion: Genera valores random para crear colores de codigo RGB.
    Entradas: N/D
    Salidas: Parámetro con el código de color en una tupla.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def tcol_set(hoja):
    """
    Funcion: Organiza los codigos de colores entrados por parámetro de función.
    Entradas: Parámetro hoja.
    Salidas:Secuencia de colores por pagina raíz.
    """
    cr, cg, cb = colorRandom ()
    hoja.set_text_color (r = cr, g = cg, b = cb)

def generaPDF():
    """
    Funcion: Genera un pdf con todas las frases con sus categorías.
    Entradas: N/D
    Salidas: PDF con las fraces y listas.
    """
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    pdf.set_font("Arial","",18) 
    pdf.cell(w=0,h=7,txt="Reporte - Total de Frases",border="TB",ln=1,align="C",fill=0) #Titulo.

    for elemento in generaListasPDF():

        pdf.set_font("Arial","",18)
        tcol_set(pdf)
        pdf.multi_cell(w=0,h=7,txt="",border=0,align="C",fill=0)
        pdf.multi_cell(w=0,h=7,txt=elemento[0],border=0,align="C",fill=0) #Categoría
        pdf.multi_cell(w=0,h=7,txt="",border=0,align="C",fill=0)
        
        for indice in elemento[1]:
            pdf.set_text_color(r=0 ,g=0 ,b=0)
            pdf.set_font("Arial","",12)
            pdf.multi_cell(w=0,h=7,txt=indice,border=0,align="L",fill=0) #Frase
            pdf.multi_cell(w=0,h=7,txt="",border=0,align="C",fill=0)
            
    pdf.output(generaNombre())

if existeArchivo ("BD")==True:
    bitacora = lee("BD")
    sinRepetidos = lee("BD")
else:
    bitacora = []
    sinRepetidos = []

nuevaLista = clasificarPdf()
