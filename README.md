# Trabajo Práctico Integrador de Organización Empresarial: Chatbot de reserva de turnos médicos

## Información institucional

**Universidad:** Universidad Tecnológica Nacional

**Carrera:** Tecnicatura Universitaria en Programación

**Materia:** Organización Empesarial

**Comisión:** 13 y 23

**Tutores:** Cristian Balmaceda y Alejandro Lencinas

**Docentes:** Mario Lopez y Andrea Ramos

**Año:** 2026

---

## Integrantes

- Abril Herrada (comisión 13)
- Erik Riberi (comisión 23)

---

## Descripción del proyecto

Este proyecto fue desarrollado como Trabajo Práctico Integrador de la materia Organización Empresarial.

Consiste en una aplicación de consola desarrollada en Python que permite simular la reserva de turnos médicos mediante un chatbot. El chatbot guía al paciente para gestionar un turno médico. El usuario puede elegir una especialidad, elegir profesionales, ver los turnos disponibles para las opciones de especialidad y profesional seleccionadas y confirmar la reserva.

La aplicación utiliza estructuras de datos dinámicas, funciones, modularización y archivos CSV para implementar persistencia de la información entre distintas ejecuciones del programa.

---

## Estructura del proyecto

```text
TPI_OE/
│
├── db/
│   ├── especialidades.csv
│   ├── profesionales.csv
│   ├── reservas.csv
│   └── turnos_disponibles.csv
├── utils/
│   ├── persistencia.py
│   └── validacion.py
├── main.py
├── .gitignore
└── README.md
```

### Módulos

- `main.py`: punto de entrada del chatbot. Contiene el bucle principal y todas las funciones que gestionan el diálogo con el paciente (saludo, selección de acciones, selección de especialidad, selección de profesional, selección de turno, confirmación y registro del turno).
- `utils/validacion.py`: centraliza las funciones de validación de entradas (nombre, opciones numéricas y especialidades) y una utilidad para normalizar texto.
- `utils/persistencia.py`: centraliza las funciones de acceso a los archivos CSV. Provee funciones para cargar especialidades, profesionales y turnos, así como para registrar reservas y actualizar la disponibilidad de los turnos.

### Base de datos

Los datos se almacenan en la carpeta `db/` mediante archivos CSV simples:

- `especialidades.csv`: columnas `id`, `nombre`. Define el catálogo de especialidades médicas.
- `profesionales.csv`: columnas `id`, `nombre`, `id_especialidad`. Define el catálogo de profesionales y relaciona cada profesional con su especialidad.
- `turnos_disponibles.csv`: columnas `id`, `id_profesional`, `fecha`, `hora`, `disponible`. Representa la agenda de cada profesional; el campo `disponible` puede ser `True` o `False` y se actualiza tras una reserva confirmada.
- `reservas.csv`: columnas `id`, `paciente`, `id_turno`, `estado`. Guarda las reservas efectivamente confirmadas. Si el archivo no existe, se crea el encabezado automáticamente.

---

## Requisitos y dependencias

- Python 3.10 o superior.
- No se requieren librerías externas: el proyecto utiliza exclusivamente los módulos estándar `csv` y `unicodedata`.
- Terminal con acceso a los comandos `python` o `python3` y permisos de lectura/escritura sobre la carpeta `db/` para que se puedan actualizar los CSV.

---

## Instrucciones de ejecución

- Clonar o descargar el repositorio y ubicarse en el directorio raíz `TPI_OE/` que contiene `main.py` y los directorios `db/` y `utils/`.
- Ejecutar el programa con `python main.py` (o `python3 main.py` según el sistema). El script debe correrse desde la raíz del proyecto.
- Seguir las instrucciones que aparece en consola. Al confirmar un turno se actualizarán automáticamente `db/reservas.csv` y `db/turnos_disponibles.csv`.

---

## Funcionamiento

El chatbot guía al paciente durante el proceso de reserva de turnos médicos.

### Flujo general

1. El usuario ingresa su nombre.
2. El usuario selecciona una especialidad médica.
3. El usuario indica si desea atenderse con un profesional específico o con cualquiera de los disponibles.
4. El sistema consulta los turnos disponibles.
5. El usuario selecciona un turno.
6. El sistema muestra un resumen de la reserva.
7. El usuario confirma o cancela la operación.
8. Si la reserva es confirmada:
   - El sistema registra una nueva reserva en `db/reservas.csv`.
   - El sistema marca el turno seleccionado como no disponible en `db/turnos_disponibles.csv`.

### Opciones disponibles

| Pantalla                   | Entrada esperada                            |
| -------------------------- | ------------------------------------------- |
| Inicio                     | Nombre del paciente                         |
| Menú principal             | `1` Ver turnos disponibles / `2` Salir      |
| Selección de especialidad  | Nombre de una especialidad o `0` para salir |
| Preferencia de profesional | `1` Sí / `2` No                             |
| Selección de profesional   | Número de opción o `0` para cancelar        |
| Selección de turno         | Número de opción o `0` para cancelar        |
| Confirmación               | `1` Confirmar / `2` Cancelar                |

### Validaciones

El sistema valida todas las entradas del usuario para evitar errores y garantizar la consistencia de los datos:

- Validación del nombre del paciente.
- Validación de opciones numéricas.
- Validación de especialidades existentes.
- Verificación de profesionales asociados a la especialidad seleccionada.
- Verificación de disponibilidad de turnos.
- Manejo de cancelaciones controladas.
- Manejo de errores de lectura y escritura en archivos CSV.

---

## Funcionalidades

- Consulta de especialidades médicas.
- Consulta de profesionales por especialidad.
- Búsqueda de turnos disponibles.
- Selección y confirmación de reservas.
- Persistencia de datos mediante archivos CSV.
- Actualización automática de disponibilidad de turnos.
- Validación de entradas y manejo de errores.
