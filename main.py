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

def buscar_turnos(profesionales):
  """
  Busca los turnos disponibles para los profesionales seleccionados.
  
  Args:
    profesionales (list): Lista de profesionales seleccionados.
  
  Returns:
    list: Lista de turnos disponibles.
  """
  # Cargar todos los turnos
  turnos_totales = cargar_turnos()
  # Inicializar listas vacías para almacenar los turnos disponibles y los IDs de los profesionales
  turnos_disponibles = []
  ids_profesionales = []

  # Recorrer la lista de profesionales seleccionados
  for profesional in profesionales:
    # Agregar el ID del profesional a la lista de IDs de profesionales
    ids_profesionales.append(profesional["id"])

  # Recorrer la lista de turnos totales
  for turno in turnos_totales:
    # Si el turno está disponible y el ID del profesional está en la lista de IDs de profesionales
    if turno["id_profesional"] in ids_profesionales and turno["disponible"] == "True":
      # Agregar el turno a la lista de turnos disponibles
      turnos_disponibles.append(turno)

  # Determinar el mensaje según la cantidad de profesionales seleccionados
  cantidad_profesionales = "el profesional seleccionado" if len(ids_profesionales) == 1 else "los profesionales seleccionados"
  
  # Si no hay turnos disponibles
  if len(turnos_disponibles) == 0:
    # Mostrar mensaje de error con mensaje dinámico y devolver None
    print(f"\nBot: No hay turnos disponibles para la especialidad y {cantidad_profesionales}.")
    return None

  # Si hay turnos disponibles
  else:
    # Devolver lista de turnos disponibles
    return turnos_disponibles

def seleccionar_turno(turnos_disponibles, profesionales):
  """
  Permite al usuario seleccionar un turno de la lista de turnos disponibles.
  
  Args:
    turnos_disponibles (list): Lista de turnos disponibles.
    profesionales (list): Lista de profesionales.
  
  Returns:
    dict: Turno seleccionado.
  """
  # Imprimir mensaje sobre turnos disponibles
  print("\nBot: Podemos ofrecerle los siguientes turnos:")

  # Recorrer la lista de turnos disponibles
  for i in range(len(turnos_disponibles)):
    # Inicializar variable para almacenar el nombre del profesional
    nombre_profesional = None

    # Recorrer la lista de profesionales
    for profesional in profesionales:
      # Si el ID del profesional coincide con el ID del turno
      if profesional["id"] == turnos_disponibles[i]["id_profesional"]:
        # Asignar el nombre del profesional
        nombre_profesional = profesional["nombre"]
        # Salir del bucle
        break

    # Imprimir el turno con el nombre del profesional
    print(f"{i + 1}. {nombre_profesional} - {turnos_disponibles[i]['fecha']} {turnos_disponibles[i]['hora']}")

  # Imprimir mensaje para que el usuario elija un turno
  print("\nBot: Ingrese el número correspondiente al turno que desea reservar o 0 para salir.")

  # Solicitar opción hasta que sea válida
  while True:
    # Intentar obtener entrada válida
    try:
      # Solicitar opción al usuario
      opcion = input("\nUsuario: ")
      # Validar opción
      validar_opcion(opcion, (0, len(turnos_disponibles)))

      # Si el usuario quiere salir, devolver None
      if opcion == "0":
        return None

      # Si la opción es válida, devolver el turno seleccionado
      else:
        return turnos_disponibles[int(opcion) - 1]

    # Si la entrada no es válida, mostrar mensaje de error
    except ValueError as e:
      print(f"\nBot: {e} Por favor, elija un turno de la lista o 0 para salir.")

def confirmar_turno(especialidad, profesional, turno):
  """
  Confirma el turno seleccionado.
  
  Args:
    especialidad (str): Especialidad seleccionada.
    profesional (str): Profesional seleccionado.
    turno (dict): Turno seleccionado.
  
  Returns:
    bool: True si el turno se confirma, False en caso contrario.
  """
  # Imprimir el turno seleccionado y las opciones
  print(f"""\nBot: Seleccionó el siguiente turno:
  Consulta de {especialidad} con {profesional} el {turno['fecha']} a las {turno['hora']}.
  ¿Desea confirmar este turno?
  1. Sí
  2. No""")

  # Solicitar opción hasta que sea válida
  while True:
    # Intentar obtener entrada válida
    try:
      # Solicitar opción al usuario
      opcion = input("\nUsuario: ")
      # Validar opción
      validar_opcion(opcion, (1, 2))

      # Si el usuario confirma el turno, devolver True
      if opcion == "1":
        return True

      # Si el usuario no confirma el turno, devolver False
      else:
        return False

    # Si la entrada no es válida, mostrar mensaje de error
    except ValueError as e:
      print(f"\nBot: {e} Por favor, ingrese 1 para confirmar o 2 para rechazar.")

def registrar_turno(paciente, id_turno):
  """
  Registra el turno seleccionado.
  
  Args:
    paciente (str): Paciente que solicita el turno.
    id_turno (int): ID del turno seleccionado.
  """
  # Crear reserva
  reserva = {
    "paciente": paciente,
    "id_turno": id_turno,
    "estado": "confirmado"
  }
  # Guardar reserva
  guardar_reserva(reserva)

  # Actualizar disponibilidad del turno
  actualizar_turno(id_turno)

  # Imprimir mensaje de confirmación
  print("\nBot: Su turno ha sido registrado correctamente.")

def despedirse():
  """
  Despide al paciente.
  
  Returns:
    bool: False para indicar que el sistema debe cerrarse.
  """
  # Imprimir mensaje de despedida
  print("\nBot: Gracias por usar el sistema de turnos.\n")

  # Devolver False para indicar que el sistema debe cerrarse
  return False
