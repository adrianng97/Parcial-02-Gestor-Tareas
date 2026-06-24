import tareas as gestor
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt

# Instanciar la consola de Rich para colores y formatos
console = Console()

def mostrar_menu():
    console.print("\n")
    console.print(Panel.fit("[bold cyan]Gestor de Tareas con Prioridad[/bold cyan]", border_style="cyan"))
    console.print("[bold white]1.[/bold white] Agregar nueva tarea")
    console.print("[bold white]2.[/bold white] Ver todas las tareas")
    console.print("[bold white]3.[/bold white] Marcar tarea como completada")
    console.print("[bold white]4.[/bold white] Eliminar tarea")
    console.print("[bold white]5.[/bold white] Salir")

def ver_tareas():
    lista_tareas = gestor.cargar_tareas()
    
    if not lista_tareas:
        console.print("[yellow]Actualmente no hay tareas registradas.[/yellow]")
        return

    # Crear una tabla estilizada
    tabla = Table(title="Lista de Tareas", show_header=True, header_style="bold magenta")
    tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("Título", style="white")
    tabla.add_column("Descripción", style="dim")
    tabla.add_column("Prioridad", justify="center")
    tabla.add_column("Estado", justify="center")

    for t in lista_tareas:
        # Colores dinámicos según prioridad y estado
        color_prio = "red" if t['prioridad'] == "alta" else "yellow" if t['prioridad'] == "media" else "green"
        color_estado = "bold green" if t['estado'] == "completada" else "bold red"
        
        tabla.add_row(
            str(t['id']),
            t['titulo'],
            t['descripcion'],
            f"[{color_prio}]{t['prioridad'].capitalize()}[/{color_prio}]",
            f"[{color_estado}]{t['estado'].capitalize()}[/{color_estado}]"
        )
    
    console.print(tabla)

def main():
    while True:
        mostrar_menu()
        opcion = Prompt.ask("\n[bold cyan]Selecciona una opción[/bold cyan]", choices=["1", "2", "3", "4", "5"])

        if opcion == "1":
            console.print("\n[bold]-- Agregar Nueva Tarea --[/bold]")
            titulo = Prompt.ask("Título de la tarea")
            descripcion = Prompt.ask("Breve descripción")
            prioridad = Prompt.ask("Prioridad", choices=["alta", "media", "baja"])
            
            gestor.agregar_tarea(titulo, descripcion, prioridad)
            console.print("[bold green]¡Tarea agregada con éxito![/bold green]")

        elif opcion == "2":
            console.print("\n")
            ver_tareas()

        elif opcion == "3":
            console.print("\n[bold]-- Completar Tarea --[/bold]")
            ver_tareas()
            try:
                # IntPrompt valida automáticamente que el usuario ingrese un número entero
                id_tarea = IntPrompt.ask("Ingresa el ID de la tarea a completar")
                exito, mensaje = gestor.completar_tarea(id_tarea)
                
                if exito:
                    console.print(f"[bold green]{mensaje}[/bold green]")
                else:
                    console.print(f"[bold red]{mensaje}[/bold red]")
            except Exception:
                console.print("[bold red]Entrada inválida. Asegúrate de ingresar un número entero.[/bold red]")

        elif opcion == "4":
            console.print("\n[bold]-- Eliminar Tarea --[/bold]")
            ver_tareas()
            try:
                id_tarea = IntPrompt.ask("Ingresa el ID de la tarea a eliminar")
                exito, mensaje = gestor.eliminar_tarea(id_tarea)
                
                if exito:
                    console.print(f"[bold green]{mensaje}[/bold green]")
                else:
                    console.print(f"[bold red]{mensaje}[/bold red]")
            except Exception:
                console.print("[bold red]Entrada inválida. Asegúrate de ingresar un número entero.[/bold red]")

        elif opcion == "5":
            console.print("\n[bold blue]¡Saliendo del Gestor de Tareas. Hasta luego![/bold blue]\n")
            break

if __name__ == "__main__":
    main()