#Elaborado por: Needler Bonilla Serrano
#               Jose Pablo Agüero Mora
#Fecha de Creación: 14/10/2021 3:00pm 
#Fecha de última Modificación: 03/11/2021 10:30am
#Versión: 3.9.6

# Importe de librerías
import pickle
import requests
from bs4 import BeautifulSoup

# Definición de funciones:

############################# Manejo de archivos ###########################
def existeArchivo(nomArchLeer):
    """
    Función: Verifica que exista un archivo con el nombre indicado.
    Entradas: Parámetro - Nombre del archivo (nomArchLeer).
    Salidas: 1 si existe el archivo en la carpeta, -1 si no existe el archivo.
    """
    try:
        f=open(nomArchLeer,"rb")
        pickle.load(f)
        f.close()
        return True
    except:
        return False

def lee(nomArchLeer):
    """
    Función: Lee los datos del archivo indicado.
    Entradas: Parámetro - Nombre del archivo (nomArchLeer).
    Salidas: Retorna los datos (codigos) del archivo indicado.
    """
    try:
        f=open(nomArchLeer,"rb")
        codigos = pickle.load(f)
        f.close()
        return codigos
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return

def graba(lista):
    """
    Función: Crea el archivo inicial con la lista de códigos.
    Entradas: Parámetro - Nombre de la lista (lista).
    Salidas: Crea el archivo o envía un mensaje de error en caso de que no sea posible.
    """
    nomArchGrabar = "BD"
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
    return

def grabaFinal(content, nombreArchivo):
    """
    Función: Abre el documento HTML y agrega todos los elemento dentro del documento.
    Entrada: Parámetro - (content) Contenido acumulado hasta el momento.
    Salida: N/D
    """
    with open(nombreArchivo, "w") as file:
        file.write(content)

########################### Memoria secundaria frases ##########################
def grabaFrases(lista):
    """
    Función: Crea el archivo inicial con la lista de códigos.
    Entradas: Parámetro - Nombre de la lista (lista).
    Salidas: Crea el archivo o envía un mensaje de error en caso de que no sea posible.
    """
    nomArchGrabar = "frasesMotivadoras"
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
    return

def existeArchivoCsv(nomArchLeer):
    """
    Función: Verifica que exista un archivo con el nombre indicado.
    Entradas: Parámetro - Nombre del archivo (nomArchLeer).
    Salidas: 1 si existe el archivo en la carpeta, -1 si no existe el archivo.
    """
    try:
        with open('bitacora.csv') as File:
            x = 0
        return True
    except:
        return False

############################ Web Scraping - Memoria ############################
def webScrap():
    URL = "https://webdelmaestrocmf.com/portal/siete-frases-motivadoras-deberiamos-decir-alumnos-dia/"
    page = requests.get(URL)

    contenido = page.text

    soup = BeautifulSoup(page.content, 'html.parser')
    lista = soup.find_all("li")

    nuevo = []
    for elemento in lista:
        nuevo.append(str(elemento))

    inicial = nuevo.index("<li>Mira lo que has conseguido. ¡Es fantástico!</li>")
    final = nuevo.index("<li>“Me siento muy bien cuando me ayudas”</li>")

    ultima = []
    indice = inicial
    while indice <= final:
        ultima.append(lista[indice])
        indice += 1

    definitiva = []
    for elemento in ultima:
        frase = str(elemento)
        frase2 = frase[4:-5]
        definitiva.append(frase2)

    return definitiva

############################# Caracteres especiales #############################
def refMayor(plista):
    """
    Función: Elimina los caracteres especiales presentes en las frases.
    Entrada: Parámetro - plista.
    Salida: Nueva lista de frases sin caracteres especiales.
    """
    otra = []
    for elemento in plista:
        pre = elemento.replace(u'\xa0', u' ')
        pre2 = pre.replace(u'“', u' ')
        otra.append(pre2.replace(u'”', u' '))
    return otra

def refinar(plista):
    """
    Función: Elimina los caracteres especiales presentes en las frases.
    Entrada: Parámetro - plista.
    Salida: Nueva lista de frases sin caracteres especiales.
    """
    otra = []
    for elemento in plista:
        otra.append(elemento.replace(u'\xa0', u' '))

    return otra
    
############################ Clasificación - Memoria #############################
def clasificacion():
    """
    Función: Clasifica las frases en sublistas según categoría.
    Entrada: N/D
    Salida: Lista de frases clasificada.
    """
    definitiva = webScrap()
    
    competencia = refinar(definitiva[0:6])
    iniciativa = refinar(definitiva[7:13])
    comunicacion = refinar(definitiva[14:19])
    identidad = refinar(definitiva[20:28])
    responsabilidad = refinar(definitiva[29:33]) 
    colaboracion = refinar(definitiva[34:40]) 
    confianza = refMayor(definitiva[41:50])
    esfuerzo = refMayor(definitiva[51:58])
    agradecer = refMayor(definitiva[59:64])
    valorar = refMayor(definitiva[65:71])
    ayuda = refMayor(definitiva[72:79])
    ver = refMayor(definitiva[80:84])
    sentir = refMayor(definitiva[85:91])

    matriz = []

    lisComp = []
    lisComp.append("La competencia")
    lisComp.append(tuple(competencia))
    matriz.append(lisComp)

    lisInic = []
    lisInic.append("La iniciativa")
    lisInic.append(tuple(iniciativa))
    matriz.append(lisInic)

    lisComu = []
    lisComu.append("La comunicación")
    lisComu.append(tuple(comunicacion))
    matriz.append(lisComu)

    lisIdenti = []
    lisIdenti.append("Su identidad")
    lisIdenti.append(tuple(identidad))
    matriz.append(lisIdenti)

    lisRespo = []
    lisRespo.append("La responsabilidad")
    lisRespo.append(tuple(responsabilidad))
    matriz.append(lisRespo)

    lisCola = []
    lisCola.append("La colaboración")
    lisCola.append(tuple(colaboracion))
    matriz.append(lisCola)

    lisConf = []
    lisConf.append("Frases para mostrarle tu confianza")
    lisConf.append(tuple(confianza))
    matriz.append(lisConf)

    lisEsf = []
    lisEsf.append("Frases para reconocer el esfuerzo y/o el sufrimiento")
    lisEsf.append(tuple(esfuerzo))
    matriz.append(lisEsf)

    lisAgra = []
    lisAgra.append("Frases para agradecer por el tiempo que han pasado juntos")
    lisAgra.append(tuple(agradecer))
    matriz.append(lisAgra)

    lisVal = []
    lisVal.append("Frases para ayudar a valorar el resultado")
    lisVal.append(tuple(valorar))
    matriz.append(lisVal)

    lisAyuda = []
    lisAyuda.append("Frases para agradecer por la ayuda o contribución")
    lisAyuda.append(tuple(ayuda))
    matriz.append(lisAyuda)

    lisVer = []
    lisVer.append("Frases para describir lo que ves")
    lisVer.append(tuple(ver))
    matriz.append(lisVer)

    lisSentir = []
    lisSentir.append("Frases para describir lo que sientes")
    lisSentir.append(tuple(sentir))
    matriz.append(lisSentir)

    return matriz

########################################################################
def ejecutar():
    """
    Función: Verifica si debe crear el archivo de frases o no.
    Entrada: N/D
    Salida: Lee el archivo o lo crea.
    """
    if existeArchivo("frasesMotivadoras") == True:
        clasificada = lee("frasesMotivadoras")
    else:
        clasificada = clasificacion()
        grabaFrases(clasificada)    
clasificada = clasificacion()
