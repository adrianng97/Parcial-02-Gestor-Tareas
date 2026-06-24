import json
import os
import logging

# Configuración del sistema de Logs
logging.basicConfig(
    filename='registro.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

ARCHIVO_JSON = 'tareas.json'

def cargar_tareas():
    """Lee el archivo JSON y retorna la lista de tareas. Lo crea si no existe."""
    if not os.path.exists(ARCHIVO_JSON):
        return []
    
    try:
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        logging.error("El archivo JSON estaba corrupto o vacío al intentar leer.")
        return []
    except PermissionError:
        logging.error("Error de permisos al intentar leer el archivo de tareas.")
        return []

def guardar_tareas(tareas):
    """Guarda la lista de tareas actual en el archivo JSON."""
    try:
        with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
            json.dump(tareas, archivo, indent=4, ensure_ascii=False)
    except IOError as e:
        logging.error(f"Error de E/S al intentar guardar las tareas: {e}")

def agregar_tarea(titulo, descripcion, prioridad):
    """Crea una nueva tarea, le asigna un ID único y la guarda."""
    tareas = cargar_tareas()
    
    # Generar un ID auto-incremental basado en las tareas existentes
    nuevo_id = 1 if not tareas else max(t['id'] for t in tareas) + 1
    
    nueva_tarea = {
        "id": nuevo_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad.lower(),
        "estado": "pendiente"
    }
    
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    logging.info(f"Tarea agregada: ID {nuevo_id} | Título: '{titulo}' | Prioridad: {prioridad}")
    return nueva_tarea

def completar_tarea(id_tarea):
    """Busca una tarea por ID y cambia su estado a completada."""
    tareas = cargar_tareas()
    
    for tarea in tareas:
        if tarea['id'] == id_tarea:
            if tarea['estado'] == 'completada':
                return False, "La tarea ya se encontraba completada previamente."
            
            tarea['estado'] = 'completada'
            guardar_tareas(tareas)
            logging.info(f"Tarea completada: ID {id_tarea}")
            return True, "Tarea marcada como completada con éxito."
            
    logging.warning(f"Intento fallido de completar tarea. ID {id_tarea} no encontrado.")
    return False, "Error: El ID ingresado no corresponde a ninguna tarea."

def eliminar_tarea(id_tarea):
    """Busca una tarea por ID y la elimina de la lista."""
    tareas = cargar_tareas()
    
    for i, tarea in enumerate(tareas):
        if tarea['id'] == id_tarea:
            del tareas[i]
            guardar_tareas(tareas)
            logging.info(f"Tarea eliminada: ID {id_tarea}")
            return True, "Tarea eliminada correctamente."
            
    logging.warning(f"Intento fallido de eliminar tarea. ID {id_tarea} no encontrado.")
    return False, "Error: El ID ingresado no corresponde a ninguna tarea."