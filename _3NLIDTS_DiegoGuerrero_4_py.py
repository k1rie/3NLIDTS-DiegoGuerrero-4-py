#Formulario de registro (version mejorada con IA)
import tkinter as tk
from tkinter import messagebox
import os
import re

CARPETA_DESTINO = os.path.join(os.path.expanduser("~"), "Documents", "Programacion Avanzada")
ARCHIVO_DESTINO = os.path.join(CARPETA_DESTINO, "14Sep26Py.txt")

def validar_datos(nombres, apellidos, telefono, edad, estatura, genero_id):
    if not nombres.strip() or not apellidos.strip():
        return "El nombre y los apellidos son obligatorios."
    if not re.fullmatch(r"\d{10}", telefono.strip()):
        return "El teléfono debe tener 10 dígitos numéricos."
    if not edad.strip().isdigit() or not (0 < int(edad) <= 120):
        return "La edad debe ser un número entero entre 1 y 120."
    try:
        valor_estatura = float(estatura.strip())
        if not (0 < valor_estatura <= 250):
            return "La estatura debe ser un número entre 1 y 250 cm."
    except ValueError:
        return "La estatura debe ser un valor numérico (ej. 167 o 167.5)."
    if genero_id == 0:
        return "Selecciona un género."
    return None

def guardar_valores():
    nombres = tbNombre.get().strip().title()
    apellidos = tbApellidos.get().strip().title()
    telefono = tbTelefono.get().strip()
    edad = tbEdad.get().strip()
    estatura = tbEstatura.get().strip()

    error = validar_datos(nombres, apellidos, telefono, edad, estatura, varGenero.get())
    if error:
        messagebox.showwarning("Datos incompletos", error)
        return

    genero = {1: "Hombre", 2: "Mujer", 3: "Otro"}[varGenero.get()]

    ### Generar la cadena de caracteres
    datos = (
        "Nombres: " + nombres + "\n" +
        "Apellidos: " + apellidos + "\n" +
        "Edad: " + edad + "\n" +
        "Estatura: " + estatura + "\n" +
        "Telefono: " + telefono + "\n" +
        "Genero: " + genero + "\n"
    )

    ## Guardar los datos en el archivo TXT (carpeta Documentos del usuario)
    try:
        os.makedirs(CARPETA_DESTINO, exist_ok=True)
        with open(ARCHIVO_DESTINO, "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n\n")
    except OSError as e:
        messagebox.showerror("Error al guardar", f"No se pudo escribir el archivo:\n{e}")
        return

    ###Mostrar mensaje de confirmación
    messagebox.showinfo("Información", "Datos guardados con éxito: \n\n" + datos)
    limpiar_campos()

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    varGenero.set(0)
    tbNombre.focus_set()

ventana = tk.Tk()
ventana.geometry("350x500")
ventana.resizable(False, False)
ventana.config(bg="#B39DDB")
ventana.title("Actividad 04 - Formulario de Registro V.02 - Diego Enrique González Guerrero")
varGenero = tk.IntVar()

lbNombre = tk.Label(ventana, text="Nombre: ", bg="#B39DDB")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos: ", bg="#B39DDB")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Teléfono: ", bg="#B39DDB")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad: ", bg="#B39DDB")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura (cm): ", bg="#B39DDB")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

groupBox = tk.LabelFrame(ventana, text="Genero: ", bg="#B39DDB", padx=12, pady=12)
groupBox.pack(pady=10)
rbMasculino = tk.Radiobutton(groupBox, text="Masculino", variable=varGenero, value=1, bg="#B39DDB")
rbMasculino.grid(row=0, column=0)
rbFemenino = tk.Radiobutton(groupBox, text="Femenino", variable=varGenero, value=2, bg="#B39DDB")
rbFemenino.grid(row=0, column=1)
rbOtro = tk.Radiobutton(groupBox, text="Otro", variable=varGenero, value=3, bg="#B39DDB")
rbOtro.grid(row=0, column=2)

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack(pady=4)
btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
btnLimpiar.pack()

ventana.mainloop()