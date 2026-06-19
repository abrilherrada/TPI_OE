# Importar librerías
import unicodedata

def validar_nombre(nombre):
  """
  Valida que el nombre no esté vacío y que contenga solo letras.
  
  Args:
    nombre (str): El nombre a validar.
  
  Raises:
    ValueError: Si el nombre está vacío o contiene caracteres no alfabéticos.
  """
  if not nombre.strip():
    raise ValueError("El nombre no puede estar vacío.")
  elif not nombre.replace(" ", "").isalpha():
    raise ValueError("El nombre debe contener solo letras.")

def validar_opcion(opcion, rango):
  """Valida que la opción ingresada no esté vacía, sea un número entero y esté dentro del rango especificado.
  
  Args:
    opcion (str): Opción ingresada como string.
    rango (tuple): Rango de opciones válidas.
  
  Raises:
    ValueError: Si la opción no cumple con las condiciones.
  """
  if not opcion.strip():
    raise ValueError("El valor ingresado no puede estar vacío.")
  elif not opcion.lstrip('-').isdigit():
    raise ValueError("El valor ingresado debe ser un número entero.")
  elif int(opcion) < rango[0] or int(opcion) > rango[1]:
    raise ValueError(f"El valor ingresado debe ser un número entre {rango[0]} y {rango[1]}.")

def eliminar_tildes(texto):
  """
  Elimina las tildes de una cadena de texto y la convierte a minúsculas.
  
  Args:
    texto (str): Texto a normalizar.
  
  Returns:
    str: Texto sin tildes y en minúsculas.
  """
  nfkd = unicodedata.normalize('NFKD', texto)
  return "".join([c for c in nfkd if not unicodedata.combining(c)]).lower()


def validar_especialidad(especialidad, especialidades):
  """Valida que la especialidad ingresada exista en la lista de especialidades.
  
  Args:
    especialidad (str): Especialidad ingresada como string.
    especialidades (list): Lista de especialidades válidas.
  
  Raises:
    ValueError: Si la especialidad no está en la lista de especialidades válidas.
  
  Returns:
    str: La especialidad válida.
  """
  especialidad_normalizada = eliminar_tildes(especialidad)
  especialidades_normalizadas = []

  for registro in especialidades:
    especialidades_normalizadas.append(eliminar_tildes(registro["nombre"]))

  if especialidad_normalizada not in especialidades_normalizadas:
    raise ValueError("La especialidad ingresada no se encuentra en nuestra lista.")

  indice = especialidades_normalizadas.index(especialidad_normalizada)

  return especialidades[indice]