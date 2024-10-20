import tkinter as tk
from tkinter import messagebox
import os

# Archivo donde se almacenan las tareas, en caso de que no las hayas completado
TASKS_FILE = "tareas.txt"

# Ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Configuracion de columnas y filas para que se expandan 
root.columnconfigure(0, weight=0)  
root.columnconfigure(1, weight=1)  
root.rowconfigure(2, weight=1)

# Añadiendo titulo
title_label = tk.Label(root, text="Lista de Tareas", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Label para escribir nueva taarea
task_label = tk.Label(root, text="Escribir nueva tarea:", font=("Arial", 12))
task_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")  

# Un Entry para ingresar nuevas tareas
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=1, column=1, padx=10, pady=(15, 0), sticky="ew")  # Ajuste de pady para bajarlo más

# Crear una Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, height=10, width=45, selectmode=tk.SINGLE)
task_listbox.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")

# Añadir nuevas tareas
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()  # Para guardar las tareas
    else:
        messagebox.showwarning("Input Error", "Debes ingresar una tarea.")

# Funcion para eliminar tareas seleccionadas
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()  # Guardar
    except:
        messagebox.showwarning("Delete Error", "Debes seleccionar una tarea para eliminar.")

# Funcion para marcar las tareas como completadas
def mark_as_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, "✔️ " + task)
        task_listbox.itemconfig(selected_task_index, {'fg': 'green'})  # Cambiar a color verde las tareas completadas
        save_tasks()
    except:
        messagebox.showwarning("Tarea realizada", "Continuar")

# Funcion para guardar las tareas en un archivo
def save_tasks():
    tasks = task_listbox.get(0, task_listbox.size())
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

#Funcion para cargar las tareas desde el archivo
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for task in f.readlines():
                task_listbox.insert(tk.END, task.strip())

#Botones
add_button = tk.Button(root, text="Añadir tarea", command=add_task)
add_button.grid(row=3, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Eliminar tarea", command=delete_task)
delete_button.grid(row=3, column=1, padx=10, pady=10)

complete_button = tk.Button(root, text="Marcar como completada", command=mark_as_completed)
complete_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

# Cargar las tareas al iniciar la aplicacion
load_tasks()

# Ejecutar la aplicacion
root.mainloop()
