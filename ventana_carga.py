import tkinter as tk
from tkinter import ttk

def barra_carga():
    top = tk.Toplevel()
    top.title("Generando contraseña...")
    top.geometry("300x120+400+200")
    top.resizable(False, False)

    barra = ttk.Progressbar(top, orient="horizontal",length=250, mode="determinate", maximum=100 )
    barra.pack(pady=30)

    def run():
        if barra["value"] < 100:
            barra["value"] +=1
            top.after(40, run)
        else:
            top.destroy()
    run()
    top.wait_window() #Espera hasta que se cierre