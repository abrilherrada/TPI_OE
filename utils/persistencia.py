# Importar librerías
import csv

#CONSTANTES
# Rutas de archivos
ARCHIVO_ESPECIALIDADES = "db/especialidades.csv"
ARCHIVO_PROFESIONALES = "db/profesionales.csv"
ARCHIVO_TURNOS = "db/turnos_disponibles.csv"
ARCHIVO_RESERVAS = "db/reservas.csv"

# Campos de los archivos
CAMPOS_ESPECIALIDADES = ["id", "nombre"]
CAMPOS_PROFESIONALES = ["id", "nombre", "id_especialidad"]
CAMPOS_TURNOS = ["id", "id_profesional", "fecha", "hora", "disponible"]
CAMPOS_RESERVAS = ["id", "paciente", "id_turno", "estado"]

# FUNCIONES
def cargar_especialidades():
  """
  Carga las especialidades desde el archivo CSV.
  
  Returns:
    list: Lista de diccionarios con las especialidades.
  """
  # Inicializar lista vacía para almacenar las especialidades
  especialidades = []

  # Intentar abrir el archivo y leer las especialidades
  try:
    # Abrir el archivo en modo lectura
    with open(ARCHIVO_ESPECIALIDADES, "r", encoding="utf-8") as archivo:
      # Crear un lector CSV
      lector = csv.DictReader(archivo)
      # Recorrer cada fila del archivo
      for fila in lector:
        # Agregar la fila a la lista
        especialidades.append(fila)

  # Si el archivo no se encuentra
  except FileNotFoundError:
    print(f"Error: Hubo un problema al cargar las especialidades de la base de datos.")
  # Si hay algún otro error
  except Exception as e:
    print(f"Error inesperado al cargar las especialidades: {e}")

  # Devolver la lista de especialidades
  return especialidades

def cargar_profesionales():
  """
  Carga los profesionales desde el archivo CSV.
  
  Returns:
    list: Lista de diccionarios con los profesionales.
  """
  # Inicializar lista vacía para almacenar los profesionales
  profesionales = []

  # Intentar abrir el archivo y leer los profesionales
  try:
    # Abrir el archivo en modo lectura
    with open(ARCHIVO_PROFESIONALES, "r", encoding="utf-8") as archivo:
      # Crear un lector CSV
      lector = csv.DictReader(archivo)
      # Recorrer cada fila del archivo
      for fila in lector:
        # Agregar la fila a la lista
        profesionales.append(fila)

  # Si el archivo no se encuentra
  except FileNotFoundError:
    print(f"Error: Hubo un problema al cargar los profesionales de la base de datos.")
  # Si hay algún otro error
  except Exception as e:
    print(f"Error inesperado al cargar los profesionales: {e}")

  # Devolver la lista de profesionales
  return profesionales

def cargar_turnos():
  """
  Carga los turnos desde el archivo CSV.
  
  Returns:
    list: Lista de diccionarios con los turnos.
  """
  # Inicializar lista vacía para almacenar los turnos
  turnos = []

  # Intentar abrir el archivo y leer los turnos
  try:
    # Abrir el archivo en modo lectura
    with open(ARCHIVO_TURNOS, "r", encoding="utf-8") as archivo:
      # Crear un lector CSV
      lector = csv.DictReader(archivo)
      # Recorrer cada fila del archivo
      for fila in lector:
        # Agregar la fila a la lista
        turnos.append(fila)

  # Si el archivo no se encuentra
  except FileNotFoundError:
    print(f"Error: Hubo un problema al cargar los turnos de la base de datos.")
  # Si hay algún otro error
  except Exception as e:
    print(f"Error inesperado al cargar los turnos: {e}")

  # Devolver la lista de turnos
  return turnos

def guardar_reserva(reserva):
  """
  Guarda una reserva en el archivo CSV.
  
  Args:
    reserva (dict): Diccionario con los datos de la reserva.
  """
  # Intentar abrir el archivo y leer las reservas existentes
  try:
    # Abrir el archivo en modo lectura
    with open(ARCHIVO_RESERVAS, "r", encoding="utf-8") as archivo:
      # Crear un lector CSV
      lector = csv.DictReader(archivo)
      # Convertir el lector en una lista
      reservas = list(lector)

    # Asignar un ID a la reserva nueva en base al número de reservas existentes
    reserva["id"] = len(reservas) + 1

    # Abrir el archivo en modo añadir
    with open(ARCHIVO_RESERVAS, "a", encoding="utf-8", newline="") as archivo:
      # Crear un escritor CSV
      escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_RESERVAS)
      # Escribir la reserva en el archivo
      escritor.writerow(reserva)

  # Si el archivo no se encuentra
  except FileNotFoundError:
    # Abrir el archivo en modo escritura
    with open(ARCHIVO_RESERVAS, "w", newline="", encoding="utf-8") as archivo:
      # Crear un escritor CSV
      escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_RESERVAS)
      # Escribir el encabezado
      escritor.writeheader()
      # Asignar un ID a la reserva
      reserva["id"] = 1
      # Escribir la reserva en el archivo
      escritor.writerow(reserva)

  # Si hay un error de permisos
  except PermissionError:
    print(f"Error: Hubo un problema al guardar la reserva en la base de datos.")

  # Si hay algún otro error
  except Exception as e:
    print(f"Error inesperado al guardar la reserva: {e}")

def actualizar_turno(id_turno):
  """
  Actualiza un turno en el archivo CSV.
  
  Args:
    id_turno (str): ID del turno a actualizar.
  """
  # Intentar abrir el archivo y leer los turnos existentes
  try:
    # Abrir el archivo en modo lectura
    with open(ARCHIVO_TURNOS, "r", encoding="utf-8") as archivo:
      # Crear un lector CSV
      lector = csv.DictReader(archivo)
      # Convertir el lector en una lista
      turnos = list(lector)

    # Recorrer la lista de turnos
    for turno in turnos:
      # Si el ID del turno coincide con el ID especificado
      if turno["id"] == id_turno:
        # Actualizar el campo "disponible" a "False"
        turno["disponible"] = "False"
        # Salir del bucle
        break

    # Abrir el archivo en modo escritura
    with open(ARCHIVO_TURNOS, "w", encoding="utf-8", newline="") as archivo:
      # Crear un escritor CSV
      escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_TURNOS)
      # Escribir el encabezado
      escritor.writeheader()
      # Escribir los turnos actualizados
      escritor.writerows(turnos)

  # Si el archivo no se encuentra
  except FileNotFoundError:
    print(f"Error: Hubo un problema al actualizar el turno en la base de datos.")
  # Si hay algún otro error
  except Exception as e:
    print(f"Error inesperado al actualizar el turno: {e}")