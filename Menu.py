import os
from Gestion import Gestion
from Carga import Carga
from Filtrado import filtrado
from Grafica import Grafica

carga = None  

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pantalla_inicial():
    print("============================================")
    print("Lenguajes Formales y de Programación, B+")
    print("Daved Abshalon Ejcalon Chonay")
    print("202105668")
    print("============================================")
    input("Presiona ENTER para continuar...")
    limpiar_pantalla()

def cargar_archivo_entrada():
    global carga  # Acceder a carga globalmente
    carga = Carga()
    carga.agregar_peliculas()

def menu_principal():
    while True:
        print("===========  MENÚ PRINCIPAL ===========")
        print("1. Cargar archivo de entrada")
        print("2. Gestionar Películas")
        print("3. Filtrado")
        print("4. Graficar")
        print("5. Salir")
        print("=======================================")
        
        opcion = input("Selecciona una opción: ")
        limpiar_pantalla()
        if opcion == "1":
            cargar_archivo_entrada()
            
        elif opcion == "2":
            if carga is not None:  # Verificar que carga esté definida
                gestion = Gestion(carga.lista_peliculas)
                gestion.mostrar_menu_gestion_peliculas()
            else:
                print("Primero debes cargar un archivo de películas.")
                input("Presiona ENTER para continuar...")
                
        elif opcion == "3":
            if carga is not None:  # Verificar que carga esté definida
                filtro = filtrado(carga.lista_peliculas)
                filtro.mostrar_menu_filtrado()
            else:
                print("Primero debes cargar un archivo de películas.")
                input("Presiona ENTER para continuar...")
                
        elif opcion == "4":
            if carga is not None:  # Verificar que carga esté definida
                grafica = Grafica(carga.lista_peliculas)
                respuesta = input("¿Deseas generar el grafico? (s/n): ")
                if respuesta.lower() == "s":
                    grafica.generar_grafica()
            else:
                print("Primero debes cargar un archivo de películas.")
                input("Presiona ENTER para continuar...")
                
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            input("Opción inválida. Presiona ENTER para continuar...")

def main():
    pantalla_inicial()
    menu_principal()

if __name__ == "__main__":
    main()