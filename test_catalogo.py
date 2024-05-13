from leccion10.domain.Pelicula import Pelicula
from Service.Servicio import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print("opciones:")
        print("1 Agregar Pelicula")
        print("2. listar Peliculas")
        print("3. Eliminar catalogo peliculas")
        print("4. salir")
        opcion = int(input("Escribe tu opcion (1-4): "))

        if opcion == 1:
            nombre_pelicula = input("proporciona el nombre: ")
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)

        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar_peliculas()


    except Exception as e:
        print(f"Ocurrio un error {e}")
        opcion = None



else:
    print("salimos del programa...")
