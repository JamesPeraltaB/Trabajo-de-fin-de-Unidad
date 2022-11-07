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

    if opc == '2':
    #OPCIÓN 2 LISTAR LIBROS
        def listar_libros():
            print(data)

        listar_libros()

    if opc == '3':
    #OPCIÓN 3 AGREGAR LIBRO
        datos = [input('Id: '), input('Título: '), input('Género: '), input('ISBN: '), input('Editorial: '), input('Autores: ')]
        def append_list_as_row(file_name, raw_content):
            
            with open(file_name,'a+',newline='') as write_obj:
                cvs_writer = writer(write_obj)
                cvs_writer.writerow(raw_content)
                print('¡Listo! Revisa en la ruta que indica la terminal.')

        append_list_as_row(open_file, datos)

    if opc == '4':
    #OPCIÓN 4 ELIMINAR LIBRO
        def eliminar_libro(file_name):
            eliminado = input('Ingresa el libro a eliminar: ')
            with open(file_name, 'r+') as r, open('output.csv', 'w') as f:
                reader = csv.reader(r)
                writer = csv.writer(f)
                for row in reader:
                    if eliminado in row:
                        print(f'{row} será eliminada')
                    else:
                        writer.writerow(row)

        eliminar_libro(open_file)

    if opc == '5':
    #OPCIÓN 5 BUSCAR LIBRO
        def buscar_libro():
            df = pd.DataFrame(data)
            eleccion = input('Título o ISBN: ')
            if eleccion.lower() == 'título':
                libro = input('Ingresa el libro: ')
                df = df[df.apply(lambda r: r.str.contains(libro, na=False).any(), axis=1)]
                print(df)
            elif eleccion.lower() == 'isbn':
                isbn = input('Ingresa el ISBN: ')
                df = df[df.apply(lambda r: r.str.contains(isbn, na=False).any(), axis=1)]
                print(df)
            else:
                print('Opción incorrecta.')

        buscar_libro()

    if opc == '6':
    # OPCIÓN 6 ORDERNAR LIBROS POR TÍTULO
        def ordenar_libros():
            csvData = pd.read_csv(open_file)
            csvData.sort_values(csvData.columns[1], axis=0, inplace=True)
            print(csvData)

        ordenar_libros() #El primero es Angels and Demons, el último es Twilight

    if opc == '7':
    #OPCIÓN 7 Buscar libros por autor, editorial o género
        def buscar_libro_other():
            df = pd.DataFrame(data)
            eleccion = input('¿Buscar por Autor, Editorial o Género?: ')
            if eleccion.lower() == 'autor':
                autor = input('Ingresa el autor: ')
                df = df[df.apply(lambda r: r.str.contains(autor, na=False).any(), axis=1)]
                print(df)
            elif eleccion.lower() == 'editorial':
                editorial = input('Ingresa la editorial: ')
                df = df[df.apply(lambda r: r.str.contains(editorial, na=False).any(), axis=1)]
                print(df)
            elif eleccion.lower() == 'género':
                genero = input('Ingresa el género: ')
                df = df[df.apply(lambda r: r.str.contains(genero, na=False).any(), axis=1)]
                print(df)
            else:
                print('Opción incorrecta.')

        buscar_libro_other()