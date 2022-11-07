import pandas as pd
from csv import writer
import csv
import os

nombre=str(input("Ingresa tu nombre para empezar: "))

print("                             Bienvenido "+nombre+"!!")


while True:
    print("""
        Estas son las opciones disponibles para interactuar con este menú:
        1) Leer archivo de disco duro.
        2) Listar libros.
        3) Agregar libros.
        4) Eliminar libros.
        5) Buscar libro por ISBN o por título.
        6) Ordenar libros por título.
        7) Buscar libros por autor, editorial o género.
        8) Buscar libros por número de autores.
        9) Editar o actualizar datos de un libro.
        10) Guardar libros en archivo de disco duro.
    """)

    opc = input('Ingresa una opción para continuar: ')


    if opc == '1':

    #OPCIÓN 1 RUTA

        open_file = input('Escriba el nombre o la dirección del archivo a leer: ')
        if open_file == '':
            print('No se seleccionó un archivo, el predeterminado será "books2.csv"')
    open_file = 'books2.csv'

    data = pd.read_csv(open_file, sep=",") #index_col=0,
