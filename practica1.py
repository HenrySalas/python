#! /usr/bin/env python
#Convierte directamente en ejecutable
"""Practica01
Taller de Sistemas Operativos 2015A
Alumno: Arturo Enrique Reynoso Salas
Fecha de creacion: 30 enero 2015
Ultima modificacion: 01 febrero 2015
"""

#Imprime instrucciones y datos del archivo
def body (open_archive,num_i,num_d,dir_i,dir_d):
    num_i = int(num_i)
    num_d = int(num_d)
    direction = int(dir_i)
    i = 0
    
    print 'Instrucciones '
    line_i = []
    for i in range(num_i):
        line_i.append(open_archive.readline())
        cod = line_i[i]
        cod = cod[0]
        dir = line_i[i]
        dir = dir[1:]
        print direction + i,#
        print 'Cod: %s' % cod + '\t Dir: %s' % dir,#
        #print line_i[i],#
        i = i + 1
    i = 0
    
    direction = int(dir_d)
    print '\nDatos '
    line_d = []
    for i in range(num_d):
        line_d.append(open_archive.readline())
        print direction + i,#
        print 'Valor: %s' % line_d[i],#
        i = i + 1

#Imprime informacion del archivo
def head (open_archive):
    no_instrucciones = open_archive.readline()
    no_datos = open_archive.readline()
    dir_instrucciones = open_archive.readline()
    dir_datos = open_archive.readline()
    print "\x1b[2J"
    print '\nNo. de instrucciones: %s' % (no_instrucciones) + 'No. de datos: %s' % (no_datos) +'Direccion inicial de instrucciones: %s' % (dir_instrucciones) +'Direccion inicial de datos: %s' % (dir_datos)
    body(open_archive,no_instrucciones,no_datos,dir_instrucciones,dir_datos)

#Funcion para abrir archivo
def openarc (archive, type):
    open_archive = ''
    open_archive = open(archive + "." + type, "r")
    if (open_archive != ''):
        print '\n\nArchivo: %s.%s' % (archive,type)
        head(open_archive)
    else:
        print 'Error al abrir el archivo %s tipo %s' % (archive, type)
    return open_archive

#Funcion para cerrar archivo
def closearc (open_arc):
    open_arc.close()


#Inicio
def inicio ():
    archive = raw_input('Porfavor introduzca el nombre del archivo a trabajar (sin extension): \n')
    type = raw_input('Porfavor introduzca la extencion del archivo: \n')
    open_arc = openarc(archive,type)
    
    
    #Al final para cerrar el archivo
    closearc(open_arc)

inicio()
