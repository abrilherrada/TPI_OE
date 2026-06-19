# ==============================================================================
# IMPORTAR MÓDULOS
# ==============================================================================
from utils.validacion import validar_opcion, validar_nombre, validar_especialidad
from utils.persistencia import cargar_especialidades, cargar_profesionales, cargar_turnos, guardar_reserva, actualizar_turno

# ==============================================================================
# FUNCIONES
# ==============================================================================
def saludar():
  """Saluda al usuario y solicita su nombre.
  
  Returns:
    str: El nombre del usuario.
  """
  # Imprimir mensaje de bienvenida
  print("\nBot: Bienvenido al sistema de turnos de CenMed. ¿Cómo se llama?")

  # Solicitar nombre hasta que sea válido
  while True:
    # Intentar obtener una entrada válida
    try:
      # Solicitar nombre al usuario
      nombre = input("\nUsuario: ").strip().title()
      # Validar nombre
      validar_nombre(nombre)
      # Si el nombre es válido, salir del bucle
      break

    # Manejar entrada inválida
    except ValueError as e:
      # Mostrar mensaje de error
      print(f"\nBot: {e} Por favor, ingrese un nombre válido.")
      # Continuar el bucle
      continue

  # Devolver nombre válido
  return nombre

def seleccionar_accion(accion):
  """
  Permite al usuario seleccionar una acción.
  
  Args:
    accion (str): La acción a realizar.
  
  Returns:
    str: La opción seleccionada.
  """
  # Imprimir opciones
  print(f"""\nBot: ¿Qué desea hacer? Ingrese el número correspondiente.
  1. {accion}
  2. Salir""")

  # Solicitar opción hasta que sea válida
  while True:
    # Intentar obtener una entrada válida
    try:
      # Solicitar opción al usuario
      opcion = input("\nUsuario: ")
      # Validar opción
      validar_opcion(opcion, (1, 2))
      # Si la opción es válida, devolverla
      return opcion

    # Manejar entrada inválida
    except ValueError as e:
      # Mostrar mensaje de error
      print(f"\nBot: {e} Por favor, ingrese una opción válida.")

def seleccionar_especialidad():
  """
  Permite al usuario seleccionar una especialidad.
  
  Returns:
    str: La especialidad seleccionada.
  """
  # Cargar especialidades
  especialidades = cargar_especialidades()

  # Imprimir mensaje para consultar especialidad
  print("\nBot: ¿Qué especialidad desea? Ingrese la especialidad o 0 para salir.")

  # Solicitar especialidad hasta que sea válida
  while True:
    # Intentar obtener una entrada válida
    try:
      # Solicitar especialidad al usuario
      opcion = input("\nUsuario: ")
      # Validar especialidad
      especialidad = validar_especialidad(opcion, especialidades)

      # Si el usuario quiere salir, devolver None
      if opcion == "0":
        return None

      # Si la especialidad es válida, devolverla
      return especialidad

    # Manejar entrada inválida
    except ValueError as e:
      # Mostrar mensaje de error
      print(f"\nBot: {e} Por favor, ingrese una especialidad válida o 0 para salir.")

def seleccionar_profesional(id_especialidad):
  """
  Permite al usuario seleccionar un profesional.
  
  Args:
    id_especialidad (int): El ID de la especialidad.
  
  Returns:
    dict: El profesional seleccionado.
  """
  # Cargar profesionales
  profesionales = cargar_profesionales()
  # Inicializar listas para almacenar profesionales por especialidad y seleccionados
  profesionales_por_especialidad = []
  profesionales_seleccionados = []

  # Filtrar profesionales por especialidad
  for profesional in profesionales:
    # Verificar si el profesional pertenece a la especialidad seleccionada
    if profesional["id_especialidad"] == id_especialidad:
      # Agregar profesional a la lista de profesionales por especialidad
      profesionales_por_especialidad.append(profesional)

  # Verificar si hay profesionales disponibles para la especialidad
  if not profesionales_por_especialidad:
    # Mostrar mensaje de error y devolver None
    print("\nBot: No hay profesionales disponibles para esta especialidad.")
    return None

  # Imprimir opciones sobre preferencia de profesional
  print("""\nBot: ¿Desea atenderse con un profesional en particular?
  1. Sí
  2. No""")

  # Solicitar opción hasta que sea válida
  while True:
    # Intentar obtener una entrada válida
    try:
      # Solicitar opción al usuario
      opcion = input("\nUsuario: ")
      # Validar opción
      validar_opcion(opcion, (1, 2))

      # Si el usuario quiere seleccionar un profesional
      if opcion == "1":
        # Imprimir pregunta sobre con cuál profesional desea atenderse
        print("\nBot: ¿Con cuál profesional desea atenderse? Ingrese el número correspondiente o 0 para salir.")
        # Imprimir lista de profesionales
        for i in range(len(profesionales_por_especialidad)):
          print(f"{i + 1}. {profesionales_por_especialidad[i]['nombre']}")

        # Solicitar opción hasta que sea válida
        while True:
          # Intentar obtener una entrada válida
          try:
            # Solicitar opción al usuario
            opcion = input("\nUsuario: ")
            # Validar opción
            validar_opcion(opcion, (0, len(profesionales_por_especialidad)))

            # Si el usuario quiere salir, devolver None
            if opcion == "0":
              return None

            # Agregar profesional seleccionado a la lista de profesionales seleccionados
            profesionales_seleccionados.append(profesionales_por_especialidad[int(opcion) - 1])
            # Devolver lista de profesionales seleccionados
            return profesionales_seleccionados

          # Si la entrada no es válida, mostrar mensaje de error
          except ValueError as e:
            print(f"\nBot: {e} Por favor, elija un profesional de la lista.")

      # Si el usuario no quiere seleccionar un profesional
      elif opcion == "2":
        # Asignar todos los profesionales de la especialidad a la lista de profesionales seleccionados
        profesionales_seleccionados = profesionales_por_especialidad
        # Devolver lista de profesionales seleccionados
        return profesionales_seleccionados

    # Si la entrada no es válida, mostrar mensaje de error
    except ValueError as e:
      print(f"\nBot: {e} Por favor, ingrese una opción válida.")
