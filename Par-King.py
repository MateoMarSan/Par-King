#Mateo Martínez Sanz Grupo: X3
listadeniveles=[]
jugar=True
diccionario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]#diciionario
def probarint(elemento): # método que comprueba que comprueba que el elemento introducido puede convertirse a un entero
        try:
            int(elemento)
            return True
        except:
            return False
with open("D:/01 Estadistica/1/Cuatrimestre2/PAR/Practica/Proyecto1/niveles.txt","r")as archivo: #abrimos el fichero de los niveles bajo el nombre de archivo
    numerodeniveles=int(archivo.readline()) #número de niveles dentro del fichero de niveles
    a = 0
    for elemento in archivo: #dónde empieza cada nivel
        elemento=elemento.rstrip('\n')
        if probarint(elemento):
            listadeniveles.append(int(a+1))
        a+=1
with open('D:/01 Estadistica/1/Cuatrimestre2/PAR/Practica/Proyecto1/records.txt')as archivo:# abrimos el fichero de récords bajo el nombre de archivo
    records=archivo.read().split()
nivelmaximo=len(records)+1 #línea de código que lee cuál es el nivel máximo que se puede escoger en función del archivo de récords 
print("Elija el nivel (1", end = "") #se imprime en la consola el nivel al que se quiere acceder
if nivelmaximo!=1:
    if nivelmaximo-1!=numerodeniveles:
        a=1
    else:
        a=2
    for b in range(nivelmaximo-a):
       print("-"+str(b+2),end="")
nivel=int(input("): "))#da la opción al usuario de elegir el nivel

def crearnivel(nivel,listadeniveles):#método que crea el nivel seleccionado por el jugador con respecto a la lista de niveles del fichero niveles
    listadecoches=[]
    with open("D:/01 Estadistica/1/Cuatrimestre2/PAR/Practica/Proyecto1/niveles.txt","r")as archivo:
        numerodelinea=listadeniveles[nivel-1]
        archivo=archivo.readlines()
        numerrodecoches=int(archivo[numerodelinea])#numero de coches que hay por nivel
        for a in range(numerrodecoches):
            elemento=str(archivo[numerodelinea+a+1].rstrip('\n'))
            listadecoches.append(elemento)#añadimos el elemento a la lista de coches
    return listadecoches

def ponercoche(tablero,nombre,orientacion,x,y,longitud,entrada):
    if orientacion=="H": #orientación horizontal H/orientación vertical V
        if entrada==1:
            tablero[y][x-1]=" "
        elif entrada==-1:
            tablero[y][x+longitud]=" "
        tablero[y][x]=orientacion+nombre.upper()
        tablero[y][x+longitud-1]=orientacion+nombre
        for a in range(longitud-2):
            tablero[y][x+a+1]=orientacion+"-"
    else:
        if entrada==1:
            tablero[y-1][x]=" "
        elif entrada==-1:
            tablero[y+longitud][x]=" "
        tablero[y][x]=orientacion+nombre.upper()
        tablero[y+longitud-1][x]=orientacion+nombre
        for a in range(longitud-2):
            tablero[y+a+1][x]=orientacion+"-"
    return tablero

def movimientoposible(tablero,orientacion,x,y,longitud,entrada): #los movimientos que podrán ser implemnetados a la hora de jugar
    if orientacion=="H": #si el coche está orientado horizontalmente
        if entrada==1 and tablero[y][x+longitud]==" ":
            return True
        elif entrada==-1 and tablero[y][x-1]==" ":
            return True
    else:#si el coche está orientado viertcalmente
        if entrada==1 and tablero[y+longitud][x]==" ":
            return True
        elif entrada==-1 and tablero[y-1][x]==" ":
            return True
    return False

def dibujar(tablero): #metodo que dibuja el tablero, con los respectivos coches
    cabezacocheH=["┌────"," ","└────"]#atributos para el coche en horizontal
    mediococheH=["─────","     ","─────"]
    fincocheH=["────┐"," ","────┘"]
    iniciococheV=["┌───┐"," ","│   │"]#atributos para el coche en vertical
    mediococheV=["│   │","│   │","│   │"]
    fincocheV=["│   │"," ","└───┘"]
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")#imprimo directamente estos caracteres sin tener que poner el comando correspondiente
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    for a in range(6):
        for c in range(3):
            for b in range (8):
                if tablero[a+1][b]=="▒":
                    print("▒▒▒▒▒",end="")
                if tablero[a+1][b]==" ":
                    print("     ",end="")
                elif tablero[a+1][b][0]=="H":
                    if tablero[a+1][b][1]=="-":
                        print(mediococheH[c],end="")
                    elif tablero[a+1][b][1]==tablero[a+1][b][1].upper():
                        cabezacocheH[1]="│"+tablero[a+1][b][1]+"   "
                        print(cabezacocheH[c],end="")
                    else:
                        fincocheH[1]="   "+tablero[a+1][b][1]+"│"
                        print(fincocheH[c],end="")
                elif tablero[a+1][b][0]=="V":
                    if tablero[a+1][b][1]=="-":
                        print(mediococheV[c],end="")
                    elif tablero[a+1][b][1]==tablero[a+1][b][1].upper():
                        iniciococheV[1]="│ "+tablero[a+1][b][1]+" │"
                        print(iniciococheV[c],end="")
                    else:
                        fincocheV[1]="│ "+tablero[a+1][b][1]+" │"
                        print(fincocheV[c],end="")
            print()
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

def movecoche(coche,orientacion,accion):
    a=list(coche)#convertimos el coche en una lista
    if orientacion=="H":#reducir o aumentar en 1 su posición no fija
        a[1]=str(int(a[1])+accion)
    else:
        a[2]=str(int(a[2])+accion)
    coche="".join(a)
    return coche

while jugar==True: #Empieza el juego
    nivelcompletado=False #iniciamlizamos la variable de completar un nivel en false
    listadecoches=crearnivel(nivel,listadeniveles)
    if nivel==nivelmaximo:#Número de nivel introducido por teclado sin récord por lo tanto, nivel no disponible
        print("NIVEL "+str(nivel)+" - SIN RECORD")
    else: #Nivel disponible
        with open("D:/01 Estadistica/1/Cuatrimestre2/PAR/Practica/Proyecto1/records.txt","r")as archivo: #si el nivel tiene algún récord registrado nos indica cuál es
                record=archivo.readline().split()[nivel-1] #Cuál es el récord
        print("NIVEL "+str(nivel)+" - "+record+" MOVIMIENTOS")
    print()
    #creamos el tablero e introducimos los coches en su posición
    tablero=[["▒","▒","▒","▒","▒","▒","▒","▒"],["▒"," "," "," "," "," "," ","▒"],["▒"," "," "," "," "," "," ","▒"],["▒"," "," "," ", " "," "," "," "],["▒"," "," "," "," "," "," ","▒"],["▒"," "," "," "," "," "," ","▒"],["▒"," "," "," "," "," "," ","▒"],["▒","▒","▒","▒","▒","▒","▒","▒"]]
    for a in range(len(listadecoches)):
        tablero=ponercoche(tablero,diccionario[a],listadecoches[a][0],int(listadecoches[a][1]),int(listadecoches[a][2]),int(listadecoches[a][3]),0)
    movimientos=0 #contador de movimientos
    while nivelcompletado==False:
        dibujar(tablero) #llamada al método que imprime por pantalla el tablero correspondiente al nivel seleccionado
        entrada=input("Movimientos = ")
        for a in range(len(entrada)):
            letra=diccionario.index(entrada[a].lower()) #
            if entrada[a]==entrada[a].upper(): #cambio a mayúsculas
                #si la letra corresponde a un movimiento posible
                if movimientoposible(tablero,listadecoches[letra][0],int(listadecoches[letra][1]),int(listadecoches[letra][2]),int(listadecoches[letra][3]),-1)==True:
                    listadecoches[letra]=movecoche(listadecoches[letra],listadecoches[letra][0],-1)
                    tablero=ponercoche(tablero,diccionario[letra],listadecoches[letra][0],int(listadecoches[letra][1]),int(listadecoches[letra][2]),int(listadecoches[letra][3]),-1)
                    movimientos+=1
                #si el movimiento no es posible
                else:
                    print("Movimiento "+entrada[a]+" imposible por bloqueo",end="")
                    break
            else:
                #si la letra corresponde a un movimiento posible
                if movimientoposible(tablero,listadecoches[letra][0],int(listadecoches[letra][1]),int(listadecoches[letra][2]),int(listadecoches[letra][3]),1) == True :
                    listadecoches[letra]=movecoche(listadecoches[letra],listadecoches[letra][0],1)
                    tablero=ponercoche(tablero,diccionario[letra],listadecoches[letra][0],int(listadecoches[letra][1]),int(listadecoches[letra][2]), int(listadecoches[letra][3]), 1)
                    movimientos+=1
                    print(listadecoches[letra][2])
                    #movimiento correspondiente a haber completado el nivel
                    if(int(listadecoches[letra][1])+int(listadecoches[letra][3])-1)==7 and int(listadecoches[letra][2])==3 and listadecoches[letra][0]=="H":
                        nivelcompletado=True
                #si el movimiento no es posible
                else:
                    print("Movimiento "+entrada[a]+" imposible por bloqueo")
                    break
        print()
    dibujar(tablero)
    print("ENHORABUENA, HA COMPLETADO EL NIVEL!") #aparece cuando se completa el nivel, cuando la variable nivelcompletado cambia a true
    print("Movimientos: "+str(movimientos)) #Cuántos movimientos hemos realizado en el nivel
    datosderecords=""
    with open("D:/01 Estadistica/1/Cuatrimestre2/PAR/Practica/Proyecto1/records.txt", "r")as archivo:
        records=archivo.readline().split()
    if nivelmaximo==nivel: #si el nivel jugado es el último que no tiene se récord, este se actualiza
        records.append(str(movimientos))
        nivelmaximo+=1 #el nivel máximo posible pasa a ser el siguiente
    else:
        if int(records[nivel-1])>movimientos:
            records[nivel-1]=str(movimientos)
    for a in range(len(records)): #almacena los récords en la variable datosrecords
        datosderecords+=records[a]+" "
    with open("D:/01 Estadistica/1/Cuatrimestre2/PAR/Practica/Proyecto1/records.txt","w")as archivo: #abre el fichero de récords y escribe los datos
        archivo.write(datosderecords)
        archivo.truncate()
    sigo=input("Desea jugar el siguiente nivel? [S/N] ") #Al finalizar un nivel, nos pregunta si queremos continuar jugando el siguiente nivel
    if sigo=="S": #Si la entrada por teclado es una S, el programa continua con el siguiente nivel
        nivel+=1
    elif sigo=="N": #Si la entrada por teclado es una N, programa se sale del bucle while y se para el juego
        jugar=False