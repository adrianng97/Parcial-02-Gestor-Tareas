# Gestor de Tareas en Python

Un sistema interactivo por consola para gestionar tareas con niveles de prioridad. Desarrollado en Python, utiliza un sistema de almacenamiento persistente en `.json` y registra las acciones del sistema en un archivo `.log`.

## Características
* **Modularidad:** Código dividido entre interfaz de usuario y lógica de negocio.
* **Persistencia:** Los datos no se borran al cerrar el programa; se guardan en `tareas.json`.
* **Trazabilidad:** Cada acción de agregar, completar o eliminar queda guardada con fecha y hora en `registro.log`.
* **Manejo de Errores:** Tolerancia a fallos en lectura/escritura y validación estricta de los inputs del usuario (IDs inexistentes o textos en lugar de números).
* **Interfaz Gráfica de Consola (CLI):** Utiliza la librería `rich` para imprimir tablas y menús coloridos.

## Instalación y Uso

1. Asegúrate de tener Python 3.x instalado.
2. Abre tu terminal en la carpeta del proyecto.
3. Instala la librería requerida:
   ```bash
   pip install -r requirements.txt