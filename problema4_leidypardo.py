# Nombre del estudiante: Leidy Lorena Pardo Acevedo
# Grupo: 213022_1017
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación
# Código Fuente: Autoría propia
# Problema 4: Videoteca digital (Filtrado y conteo de catálogo)

catalogo = [
    ["Aladdin", 1992, 8.0, "Animacion"],
    ["Spider Man", 2002, 7.5, "Accion"],
    ["El Padrino", 1972, 9.2, "Crimen"],
    ["Mean Girls", 2004, 7.1, "Comedia"],
    ["El lobo de Wall Street", 2013, 8.2, "Comedia"],
    ["Emoji: La pelicula", 2017, 3.5, "Animacion"],
    ["Escuadron suicida", 2016, 5.9, "Accion"]
]

while True:
    try:
        calificacion_minima = float(input("--Ingrese la calificacion minima que debe tener la pelicula: \n"))
        if calificacion_minima >=1 and calificacion_minima <=10:
            break
        else:
            print("||Recuerde escoger un numero entre 1 a 10||\n")
    except ValueError:
        print("||El valor a ingresar debe ser un numero entre 1 y 10||\n")
while True:    
    try:
        anio_limite = int(input("--Ingrese el año limite de lanzamiento: \n"))
        if anio_limite >=1900 and anio_limite <= 2026:
            break
        else:
            print("||Escoja un año entre 1900 y 2026||\n")
    except ValueError:
        print("||Debe ingresar un año Valido, Ej: 2000||\n")

def contar_peliculas_filtradas(catalogo, calificacion_minima, anio_limite):
    contador = 0
    peliculas_cumplen_criterios = []

    for fila in catalogo:
        titulo = fila[0]
        anio = fila[1]
        calificacion = fila[2]
        genero = fila[3]

        if calificacion >= calificacion_minima and anio >= anio_limite:
            contador += 1
            peliculas_cumplen_criterios.append(f"{titulo} ({anio}) - Calificación: {calificacion} - Género: {genero}")

    return contador, peliculas_cumplen_criterios

resultado, peliculas_filtradas = contar_peliculas_filtradas(catalogo, calificacion_minima, anio_limite)

print(f"Número de películas que cumplen con los criterios: {resultado}\n")
if resultado > 0:
    print("--Películas que cumplen con los criterios:\n")
    for pelicula in peliculas_filtradas:
        print(pelicula)
else:
    print("No hay películas que cumplan con los criterios.\n")