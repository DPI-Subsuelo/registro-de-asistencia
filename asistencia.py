import tkinter as tk #se importa tkinter
from datetime import datetime #se importa la libreria datatime para usar tiempo y fechas
def registrar_asistencia(): #funcio registrar asistencia
    nombre_empleado = campo_texto.get() #nombre del empleado en el cuadro de texto
    hora_actual = datetime.now().strftime ("%Y-%m-%d %H:%M:%S") #se registra la hora actual, traida con el metodo datatime
    with open('registro_asistencia.txt', 'a') as f:
        f.write(f"{nombre_empleado},{hora_actual}\n")
    etiqueta_resultado.config(text=f"Asistencia registrada para: {nombre_empleado} a las {hora_actual}") #se guarda el metodo with open en el archivo asistencia.txt

ventana = tk.Tk() #se crea la ventana
ventana.geometry('300x100')
campo_texto = tk.Entry(ventana)
campo_texto.pack()

boton = tk.Button(ventana, text="Registrar Asistencia", command=registrar_asistencia) #se crea el boton con la funcion de registrar asistencia
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="") #etiqueta que muestra el resultado
etiqueta_resultado.pack()

ventana.mainloop() #mantener la ventana activa hasta que se hace clic en el botón cerrar.