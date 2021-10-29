import csv


def read_csv():
    csvfile = open("colores.csv")
    data = list(csv.DictReader(csvfile))
    csvfile.close()

    fila = 0
    columna = "propiedades"
    print(data[fila][columna])



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    read_csv()
 
