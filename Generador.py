import customtkinter, secrets, random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from ventana_carga import barra_carga

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

numeros=list(range(0,10))

mayuscula=['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

minuscula=['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

simbolos=[ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
           '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
           '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
           '}', '~']

class AppGenerator:

    def ingresar_caracteres(self, event=None):

        valor = self.entrada.get()

        if not valor:
            messagebox.showwarning("Advertencia", "Debe ingresar el número de caracteres [0 ---> 30]")
            return

        try:
            self.nro_caracteres = int(valor)
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida")
            self.entrada.delete(0, tk.END)
            return

        if self.nro_caracteres < 1 or self.nro_caracteres > 30:
            messagebox.showerror("Error", "Ingrese una cantidad en el rango establecido.")
            self.entrada.delete(0, tk.END)
            return


    def generar_contraseña(self):

        self.ingresar_caracteres()

        if not hasattr(self, "nro_caracteres"):
            return
        
        barra_carga()
        self.root.update()

        contraseña=[]

        opc_1 = self.checkbox_1.get()
        opc_2 = self.checkbox_2.get()

        if opc_1 and opc_2:

            for i in range(self.nro_caracteres):
                may=secrets.choice(mayuscula)
                contraseña.append(may)

            for i in range(self.nro_caracteres):
                num=secrets.choice(numeros)
                contraseña.append(num)

            for i in range(self.nro_caracteres):
                simb=secrets.choice(simbolos)
                contraseña.append(simb)

            for i in range(self.nro_caracteres):
                minu=secrets.choice(minuscula)
                contraseña.append(minu)

        elif opc_1:

            for i in range(self.nro_caracteres):
                may=secrets.choice(mayuscula)
                contraseña.append(may)

            for i in range(self.nro_caracteres):
                num=secrets.choice(numeros)
                contraseña.append(num)

            for i in range(self.nro_caracteres):
                minu=secrets.choice(minuscula)
                contraseña.append(minu)

        elif opc_2:

            for i in range(self.nro_caracteres):
                may=secrets.choice(mayuscula)
                contraseña.append(may)

            for i in range(self.nro_caracteres):
                simb=secrets.choice(simbolos)
                contraseña.append(simb)

            for i in range(self.nro_caracteres):
                minu=secrets.choice(minuscula)
                contraseña.append(minu)

        else:
            messagebox.showwarning("Advertencia", "Seleccione al menos una opción.")
            return

        random.shuffle(contraseña)

        final=random.sample(contraseña, self.nro_caracteres)

        password="".join(map(str, final))

        with open("Contraseñas.txt", "a") as archivo:
            archivo.write(password+"\n")

        print(password)

        fecha=datetime.now()

        messagebox.showinfo(
            "Info",
            f"Contraseña generada a las {fecha.hour}:{fecha.minute}:{fecha.second} ✔"
        )


    def __init__(self, root):

        self.root=root
        self.root.geometry("500x350+400+350")
        self.root.title("Generador de contraseñas")
        self.root.resizable(False, False)

        self.root.bind("<Return>", self.ingresar_caracteres)

        self.titulo=customtkinter.CTkLabel(root, text="Configuración", font=("Arial", 18, "bold"))
        self.titulo.pack(pady=10)

        self.entrada=customtkinter.CTkEntry(root, width=120)
        self.entrada.pack(pady=10)

        self.var_1=tk.BooleanVar()
        self.checkbox_1=customtkinter.CTkCheckBox(root, text="Números", variable=self.var_1)
        self.checkbox_1.pack(pady=10)

        self.var_2=tk.BooleanVar()
        self.checkbox_2=customtkinter.CTkCheckBox(root, text="Símbolos", variable=self.var_2)
        self.checkbox_2.pack(pady=5)

        self.boton_generar = customtkinter.CTkButton(root, text="GENERAR", 
        command=self.generar_contraseña, 
        hover_color="light green",
        border_spacing=2 )

        
        self.boton_generar.pack(pady=10)


root=customtkinter.CTk()
app=AppGenerator(root)
root.mainloop()