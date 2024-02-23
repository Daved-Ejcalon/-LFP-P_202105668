class Gestion:
    def __init__(self, lista_peliculas):
        self.lista_peliculas = lista_peliculas

    def num_peliculas(self):
        return len(self.lista_peliculas)

    def mostrar_menu_gestion_peliculas(self):
        while True:
            # Mostrar el menú de gestión de películas
            print("")
            print("===========  MENÚ GESTIÓN DE PELÍCULAS ===========")
            print("1. Mostrar películas")
            print("2. Mostrar actores")
            print("3. Volver al menú principal")
            print("==================================================")
            
            opcion = input("Selecciona una opción: ")

            if opcion.lower() == "1":
                if self.num_peliculas() == 0:
                    print("No hay películas cargadas.")
                self.mostrar_peliculas()
            elif opcion.lower() == "2":
                if self.num_peliculas() == 0:
                    print("No hay películas cargadas.")
                self.mostrar_actores()
            elif opcion.lower() == "3":
                break
            else:
                input("Opción inválida. Presiona Enter para continuar...")

    def mostrar_peliculas(self):
        print("")
        print("========================  LISTA DE PELÍCULAS =====================")
        for i, pelicula in enumerate(self.lista_peliculas, 1):
            print(f"{i}. {pelicula['nombre']} ({pelicula['año']}) - Género: {pelicula['género']}")
        print("==================================================================")

    def mostrar_actores(self):
        while True:
            self.mostrar_peliculas()
            seleccion = input("Selecciona el número de la película para ver los actores (0 para volver): ")
            if seleccion.isdigit():
                seleccion = int(seleccion)
                if seleccion == 0: # Volver
                    break
                if seleccion <= len(self.lista_peliculas):
                    pelicula = self.lista_peliculas[seleccion - 1]
                    print("")
                    print(f"Actores de '{pelicula['nombre']}':\n{', '.join(pelicula['actores'])}")
                else: # Número fuera de rango
                    print("Número de película inválido. Inténtalo de nuevo.")
            else: # No es un número
                print("Por favor, ingresa un número válido.")
