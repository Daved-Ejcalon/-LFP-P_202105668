class Carga:
    def __init__(self):
        self.lista_peliculas = []

    def pelicula_tiene_actor(self, nombre_película, actor):
        for película in self.lista_peliculas:
            if película['nombre'] == nombre_película:
                return actor in película['actores']
        return False

    def get_nombre_peliculas(self):
        nombres = []
        for película in self.lista_peliculas:
            nombres.append(película['nombre'])
        return nombres
    
    def get_nombre_actores(self):
        nombres = []
        for película in self.lista_peliculas:
            nombres.extend(película['actores'])
        return list(set(nombres))
        
    def creacion_diccionario_pelicula(self, nombre, actores, año, género):
        película = {
            "nombre": nombre,
            "actores": actores.split(","),
            "año": int(año),
            "género": género
        }
        return película

    def leer_archivo_peliculas(self, ruta):
        
        try:
            with open(ruta, 'r', encoding='utf8') as lectura_lfp:
                lines = lectura_lfp.readlines()
            return lines
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return []

    def agregar_peliculas(self):

        ruta_archivo = input("Ingresa la ruta del archivo de películas: ")
        lines = self.leer_archivo_peliculas(ruta_archivo)
        
        for linea in lines:
            datos = linea.strip().split(';')

            if len(datos) != 4:
                print(f"La línea '{linea}' no tiene el formato correcto.")
                continue
            
            nombre_pelicula = datos[0]
            actores = datos[1]
            año = datos[2]
            género = datos[3]

            # Verificar si existe una película con el mismo nombre
            if nombre_pelicula in self.get_nombre_peliculas():
                print(f"La película '{nombre_pelicula}' ya fue cargada.")

                # Remover la película con el mismo nombre
                self.lista_peliculas = [p for p in self.lista_peliculas if p['nombre'] != nombre_pelicula]

            película = self.creacion_diccionario_pelicula(nombre_pelicula, actores, año, género)
            self.lista_peliculas.append(película)

        print(f"Se han cargado {len(self.lista_peliculas)} películas.")
