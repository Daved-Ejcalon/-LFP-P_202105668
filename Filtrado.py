class filtrado:
    def __init__(self, lista_peliculas):
        self.lista_peliculas = lista_peliculas

    def filtrar_por_actor(self):
        actor_buscar = input("Ingrese el nombre del actor: ")
        peliculas_actor = []
        for pelicula in self.lista_peliculas:
            if actor_buscar in pelicula['actores']:
                peliculas_actor.append(pelicula['nombre'])
        
        if peliculas_actor:
            print(f"Películas en las que participa {actor_buscar}:")
            for pelicula in peliculas_actor:
                print(pelicula)
        else:
            print(f"No se encontraron películas en las que participa {actor_buscar}.")

    def filtrar_por_año(self):
        año_buscar = input("Ingrese el año a filtrar: ")
        peliculas_año = [pelicula for pelicula in self.lista_peliculas if str(pelicula['año']) == año_buscar]
        
        if peliculas_año:
            print(f"Películas del año {año_buscar}:")
            for pelicula in peliculas_año:
                print(f"{pelicula['nombre']} - Género: {pelicula['género']}")
        else:
            print(f"No se encontraron películas para el año {año_buscar}.")

    def filtrar_por_genero(self):
        genero_buscar = input("Ingrese el género a filtrar: ")
        peliculas_genero = [pelicula for pelicula in self.lista_peliculas if pelicula['género'].lower() == genero_buscar.lower()]
        
        if peliculas_genero:
            print(f"Películas del género {genero_buscar}:")
            for pelicula in peliculas_genero:
                print(f"{pelicula['nombre']} - Año: {pelicula['año']}")
        else:
            print(f"No se encontraron películas para el género {genero_buscar}.")
    
    def mostrar_menu_filtrado(self):
        while True:
            print("")
            print("============== MENÚ FILTRADO ================")
            print("1. Filtrar por actor")
            print("2. Filtrar por año")
            print("3. Filtrar por género")
            print("4. Volver al menú principal")
            print("==============================================")
            
            opcion = input("Selecciona una opción: ")

            if opcion.lower() == "1":
                self.filtrar_por_actor()
            elif opcion.lower() == "2":
                self.filtrar_por_año()
            elif opcion.lower() == "3":
                self.filtrar_por_genero()
            elif opcion.lower() == "4":
                break
            else:
                input("Opción inválida. Presiona ENTER para continuar...")
