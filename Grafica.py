from graphviz import Digraph
class Grafica:
    def __init__(self, lista_peliculas):
        self.lista_peliculas = lista_peliculas

    def generar_grafica(self):
        dot = Digraph()

        dot.attr(rankdir='RL')

        # Creacion lista de nombres de actores
        lista_nombre_actores = []
        for pelicula in self.lista_peliculas:
            actores = pelicula['actores']
            for actor in actores:
                if actor not in lista_nombre_actores:
                    lista_nombre_actores.append(actor)

        # Generar los nodos de actores
        for actor in lista_nombre_actores:
            dot.node(f"A_{actor}", actor, shape='square', pos='right', fontsize='10')

        # Generar los nodos de peliculas y tablas
        for i, pelicula in enumerate(self.lista_peliculas):
            nombre = pelicula['nombre']
            año = str(pelicula['año'])
            género = pelicula['género']

            # Crear tabla para la información de la película
            table = f'<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD COLSPAN="2" BGCOLOR="lightblue">{nombre}</TD></TR>' \
                    f'<TR><TD>{año}</TD><TD>{género}</TD></TR></TABLE>>'

            dot.node(f"P_{i}", table, shape='none', pos='left')

        # Generar las aristas
        for i, película in enumerate(self.lista_peliculas):
            nombre_pelicula = película['nombre']
            actores = película['actores']
            for actor in actores:
                # Si el actor participa en la película, agregar la arista
                dot.edge(f"A_{actor}", f"P_{i}")

        # Generar el archivo de la gráfica
        dot.render('Grafico', format='png', cleanup=True)

        # Generar archivo .dot
        #with open('Grafico.dot', 'w') as file:
        #    file.write(dot.source)
        
        # Mensaje de éxito
        print("¡Diagrama generado con éxito como 'Grafico.png'!")