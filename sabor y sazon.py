import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Clase principal
class GestionClientes:
    def __init__(self, identificacion, nombreCompleto, genero, tipoMenu, numeroSesiones, costoSesion):
        self.identificacion = identificacion
        self.nombreCompleto = nombreCompleto
        self.genero = genero
        self.tipoMenu = tipoMenu
        self.numeroSesiones = numeroSesiones
        self.costoSesion = costoSesion
        self.fechaRegistro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def calcularCostoTotal(self):
        return self.numeroSesiones * self.costoSesion


# Diccionario con los costos por menú
costos_menu = {
    "Ejecutivo": 35000,
    "Vegetariano": 28000,
    "Degustación": 75000,
    "Infantil": 20000,
    "Gourmet": 95000
}

# Pantalla de acceso
def pantalla_acceso():
    acceso = tk.Tk()
    acceso.title("Acceso - Sabor & Sazón")
    acceso.geometry("300x150")

    tk.Label(acceso, text="Ingrese la contraseña:").pack(pady=10)
    entry_pass = tk.Entry(acceso, show="*")
    entry_pass.pack()

    def validar():
        if entry_pass.get() == "2233":
            acceso.destroy()
            crear_interfaz()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    tk.Button(acceso, text="Ingresar", command=validar).pack(pady=10)
    acceso.mainloop()


# Interfaz principal
def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Sabor & Sazón - Gestión de Clientes")
    ventana.geometry("400x400")
    ventana.configure(bg="#f0f0f0")

    # Campos de entrada
    tk.Label(ventana, text="Identificación:").pack()
    entry_id = tk.Entry(ventana)
    entry_id.pack()

    tk.Label(ventana, text="Nombre completo:").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Género:").pack()
    genero_var = tk.StringVar(value="Masculino")
    tk.OptionMenu(ventana, genero_var, "Masculino", "Femenino").pack()

    tk.Label(ventana, text="Tipo de menú:").pack()
    menu_var = tk.StringVar(value="Ejecutivo")
    tk.OptionMenu(ventana, menu_var, *costos_menu.keys()).pack()

    tk.Label(ventana, text="Número de sesiones:").pack()
    entry_sesiones = tk.Entry(ventana)
    entry_sesiones.pack()

    # Función para guardar y mostrar reporte
    def guardar_y_calcular():
        try:
            cliente = GestionClientes(
                identificacion=entry_id.get(),
                nombreCompleto=entry_nombre.get(),
                genero=genero_var.get(),
                tipoMenu=menu_var.get(),
                numeroSesiones=int(entry_sesiones.get()),
                costoSesion=costos_menu[menu_var.get()]
            )
            total = cliente.calcularCostoTotal()

            # Ventana de reporte
            reporte = tk.Toplevel()
            reporte.title("Reporte de Ventas")
            reporte.geometry("350x300")
            reporte.configure(bg="red")  # Fondo rojo

            tk.Label(reporte, text="📊 Reporte de Cliente", bg="red", fg="white", font=("Arial", 14, "bold")).pack(pady=10)
            tk.Label(reporte, text=f"Identificación: {cliente.identificacion}", bg="red", fg="white").pack()
            tk.Label(reporte, text=f"Nombre: {cliente.nombreCompleto}", bg="red", fg="white").pack()
            tk.Label(reporte, text=f"Género: {cliente.genero}", bg="red", fg="white").pack()
            tk.Label(reporte, text=f"Menú: {cliente.tipoMenu}", bg="red", fg="white").pack()
            tk.Label(reporte, text=f"Sesiones: {cliente.numeroSesiones}", bg="red", fg="white").pack()
            tk.Label(reporte, text=f"Costo por sesión: {cliente.costoSesion}", bg="red", fg="white").pack()
            tk.Label(reporte, text=f"Total a pagar: {total}", bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
            tk.Label(reporte, text=f"Fecha de registro: {cliente.fechaRegistro}", bg="red", fg="white").pack()

        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido de sesiones.")

    # Botones
    tk.Button(ventana, text="Guardar y Calcular", command=guardar_y_calcular).pack(pady=10)

    def salir():
        if messagebox.askyesno("Salir", "¿Desea cerrar la aplicación?"):
            ventana.quit()

    tk.Button(ventana, text="Salir", command=salir).pack(pady=10)

    ventana.mainloop()


# Ejecutar primero la pantalla de acceso
pantalla_acceso()
