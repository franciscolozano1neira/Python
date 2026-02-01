# Esta es la librería principal que necesito para que el programa "piense".
# En lugar de escribir yo miles de reglas (si goles > 10 y pases > 100...),
# importo el RandomForestClassifier de sklearn.
# Es básicamente el motor de la IA que me permite crear ese "consejo de personas"
# que va a analizar los patrones de los jugadores automáticamente.
from sklearn.ensemble import RandomForestClassifier
# Uso numpy solo para organizar los números en listas y generar los datos
# aleatorios del mercado de forma rápida
import numpy as np

# Datos para entrenamiento (45 Perfiles)
# 6 Métricas: [Goles, Asistencias, Recuperaciones, Pases, KM, Partidos de liga]
datos = [
    # Clase 2: Futura Leyenda
    [50, 15, 5, 2100, 10.2, 37],  # Futuro Messi
    [48, 12, 8, 1200, 11.0, 38],  # Futuro Cristiano
    [15, 28, 12, 1600, 10.5, 34],  # Futuro Ronaldinho
    [8, 10, 85, 1100, 10.8, 36],  # Futuro Puyol/Ramos
    [2, 35, 40, 2600, 12.0, 38],  # Futuro Xavi/Modric
    [4, 25, 35, 2400, 11.8, 35],  # Futuro Kroos/Xabi Alonso
    [1, 5, 95, 1400, 12.5, 34],  # Futuro Mascherano
    [12, 25, 20, 1800, 13.0, 36],  # Futuro Iniesta

    [3, 30, 25, 2300, 9.5, 35],  # PERFIL PIRLO
    [30, 8, 10, 500, 10.0, 34],  # PERFIL HAALAND/MBAPPÉ
    [2, 8, 70, 1150, 10.9, 35],  # Central moderno top
    [1, 15, 60, 1400, 13.5, 37],  # Lateral tipo Cafú/Roberto Carlos

    # CLASE 1: Interesantes
    [12, 5, 2, 350, 9.5, 25],
    [6, 10, 18, 650, 10.8, 22],
    [2, 4, 38, 700, 10.2, 24],
    [1, 8, 32, 800, 11.5, 20],
    [8, 8, 10, 500, 10.0, 28],
    [4, 12, 25, 950, 12.0, 26],
    [0, 2, 45, 600, 9.8, 22],
    [10, 3, 5, 300, 9.2, 18],
    [3, 7, 20, 850, 11.2, 21],
    [1, 5, 40, 750, 10.6, 23],
    [5, 5, 25, 600, 10.0, 15],
    [2, 6, 15, 500, 11.0, 12],
    [0, 3, 30, 450, 10.5, 14],
    [7, 2, 10, 300, 9.0, 10],
    [1, 1, 35, 550, 10.2, 13],

    # CLASE 0: Descartes
    [2, 1, 5, 180, 8.2, 8],
    [0, 2, 12, 250, 7.5, 10],
    [1, 0, 15, 300, 8.0, 12],
    [0, 0, 4, 80, 7.0, 4],
    [3, 1, 2, 150, 8.5, 7],
    [0, 1, 10, 200, 7.8, 5],
    [1, 0, 8, 120, 8.1, 6],
    [0, 0, 20, 100, 7.2, 9],
    [2, 0, 1, 50, 7.0, 3],
    [1, 1, 1, 100, 6.0, 2],
    [0, 0, 5, 50, 5.0, 1],
    [0, 0, 0, 20, 2.0, 1],
    [0, 0, 10, 80, 7.0, 4],
    [1, 0, 0, 40, 6.5, 2],
    [0, 0, 2, 10, 1.0, 1],
    [0, 1, 0, 30, 3.5, 2],
    [1, 0, 1, 20, 4.0, 1],
    [0, 0, 0, 0, 0, 0]
]

# Etiquetas: 12 Leyendas (Clase 2), 15 Interesantes (Clase 1), 18 Descartes (Clase 0)
# Aquí le decimos a la IA qué es cada cosa para que aprenda a diferenciar patrones.
resultados = [
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, # CLASE 2: La clase que buscamos jugadores que se parezcan a estos.
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, # CLASE 1: El término medio. No son prioridad pero se ven por si acaso.
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 # CLASE 0: El filtro. Lo que la IA debe aprender a rechazar.
]

# RandomForestClassifier: Imagina que para no equivocarte con un fichaje, en lugar de
# decidirlo tú solo, montas un "Consejo de 100 personas".
# Cada "persona" se fija en detalles diferentes: una mira los goles, otra los pases,
# otra las asistencias... Al final, el resultado será lo que la mayoría de ellas vote.
# Es un sistema muy fiable porque si una persona se equivoca, las otras 99 la corrigen.
modelo_ia = RandomForestClassifier(n_estimators=100)

# .fit (El entrenamiento): Aquí es donde las 100 personas "estudian" los datos y los resultados
# que les facilitamos de jugadores antiguos. Les enseñamos qué 'nota' sacó cada uno.
# Es como si les diéramos 45 exámenes ya corregidos para que aprendan qué estadísticas
# dan el suspenso (0), el aprobado (1) o el sobresaliente (2).
# Tras esto, el consejo ya está listo para analizar el mercado y encontrar los mejores fichajes.
modelo_ia.fit(datos, resultados)


# Funcion que Sirve para meter en el sistema a cualquier jugador que hayamos visto nosotros mismos,
# sin esperar a que el programa lo genere al azar
def AñadirJugador(nombres, datos, nombre, estadisticas):
    """
    nombre: Texto (Ej: "Lamine Yamal")
    estadisticas: Lista [Goles, Asistencias, Recuperaciones, Pases, KM, Partidos de Liga ]
    """
    # Le ponemos una etiqueta para saber que no es una promesa aleatoria,
    # sino un fichaje que nosotros hemos propuesto manualmente.
    nombres.append("Ojeado Manual: " + nombre)
    datos.append(estadisticas)


# Generacion automatica del mercado de fichajes de 40 candidatos (Sin porteros)
Id_candidatos = []
ListaPuntos = []

for i in range(1, 41):
    Id_candidatos.append("Id_Promesa: " + str(i))
    # Generamos los datos uno a uno (forma mas humana que usar matrices de numpy directas)
    goles = np.random.randint(0, 55)
    asist = np.random.randint(0, 40)
    recup = np.random.randint(0, 100)
    pases = np.random.randint(100, 2900)
    km = round(np.random.uniform(7.5, 14.5), 1)
    pj = np.random.randint(1, 38)
    ListaPuntos.append([goles, asist, recup, pases, km, pj])

# Metemos a los objetivos especificos
AñadirJugador(Id_candidatos, ListaPuntos, "Lamine Yamal", [15, 22, 18, 1400, 11.2, 35])
AñadirJugador(Id_candidatos, ListaPuntos, "Rodri", [8, 12, 75, 2600, 12.5, 37])

# La IA analiza a los candidatos y le asigna una probabilidad de que su fichaje sea bueno
probabilidades = modelo_ia.predict_proba(ListaPuntos)
Informe = []

# Analisis de los datos para poder asignarles un rol dependiendod e sus metricas
for i in range(len(Id_candidatos)):
    # Extraemos las métricas para que sea fácil de leer
    goles = ListaPuntos[i][0]
    asist = ListaPuntos[i][1]
    recup = ListaPuntos[i][2]
    pases = ListaPuntos[i][3]
    km    = ListaPuntos[i][4]

    #  Roles especificos
    #  Defensas
    if recup > 50:
        if pases > 1300:
            rol_detectado = "CEN" # Central con salida de balón
        elif km > 11.5:
            rol_detectado = "LAT" # Lateral
        else:
            rol_detectado = "CEN" # Central

    #  Centrocampistas
    elif pases > 1200:
        if recup > 40:
            rol_detectado = "MCD" # Medio centro defensivo (
        elif asist > 18:
            rol_detectado = "MCO" # Mediapunta ofensivo
        elif km > 12:
            rol_detectado = "MC"  # Medio centro
        else:
            rol_detectado = "MC"

    #  Extremos
    elif km > 11 and asist > 12:
        if pases > 800:
            rol_detectado = "MI" if i % 2 == 0 else "MD" # Mediocentros Izq/Der
        else:
            rol_detectado = "EI" if i % 2 == 0 else "ED" # Extremos

    #  Delanteros
    else:
        rol_detectado = "DEL"

    # Significado de probabilidades[i][2]:
    # El [2] le dice al código que solo nos dé el porcentaje de la CLASE 2 (Leyendas) basandose en sus metricas
    # solo tenemos encueta al que la IA  a metido en el salco de la clase 2 el resto no los necesitamos.
    # multiplicamos por 100 para tener una "Nota" sobre 100.
    nota = int(probabilidades[i][2]* 100)


    # Etiquetas
    etiqueta = ""
    if nota >= 90:
        if rol_detectado == "DEL" and goles > 40: etiqueta = " (¡Perfil MESSI/CR7!)"
        elif rol_detectado == "MCO" or rol_detectado == "ED": etiqueta = " (¡Perfil Ronaldinho!)"
        elif rol_detectado == "MCD" or rol_detectado == "CEN": etiqueta = " (¡Perfil Defensivo!)"
        elif rol_detectado == "MC" or rol_detectado == "MCO": etiqueta = " (¡Perfil Creador!)"

    Informe.append({
        'nombre': Id_candidatos[i] + etiqueta,
        'nota': nota,
        'rol': rol_detectado,
        'puntos': ListaPuntos[i]
    })

def orden(j): return j['nota']

#Ordena de mayor porcentaje a menor porcentaje por la nota que la IA proporciona usando el metodo orden
Informe.sort(key=orden, reverse=True)

# Salida por terminal
print("\n Resultado de los 10 mejores segun la IA \n")
print("Nº | ROL | NOTA | G-A-R-P-KM-PG | NOMBRE")
#G= goles - A = asistencias - R=Recuperaciones de balon - P = pases - KM =Kilometros recorridos - PG =Partidos jugados
print("----------------------------------------------")

for i in range(10):
    f = Informe[i]  # Sacamos el diccionario del jugador actual (la i de la lista)
    p = f['puntos']  # Extraemos sus métricas para no escribir f['puntos'] todo el rato
    #Redondeo de los kilometros recorridos a un decimal
    km_fijo = round(p[4], 1)

    print(i + 1, "  |", f['rol'], "|", f['nota'],
          "% |", int(p[0]), "-", int(p[1]), "-", int(p[2]), "-", int(p[3]), "-", km_fijo ,"-", int(p[5]),
          "|", f['nombre'])