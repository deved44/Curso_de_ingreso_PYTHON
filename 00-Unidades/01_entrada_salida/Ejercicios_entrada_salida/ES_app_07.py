import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: David Alejandro
apellido: Morales Silva
---
Ejercicio: entrada_salida_07
---
Enunciado:
Al presionar el botón  que corresponde a cada operación (suma, resta, multiplicación, y división), 
se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado 
de la misma utilizando el Dialog Alert. Ej: "El resultado de la …… es: 755"  
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_dividir = customtkinter.CTkButton(master=self, text="Dividir", command=self.btn_dividir_on_click)
        self.btn_dividir.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_sumar_on_click(self):
        
        primer_numero_suma = self.txt_operador_a.get()
        primer_numero_suma = int(primer_numero_suma)
        
        segundo_numero_suma = self.txt_operador_b.get()
        segundo_numero_suma = int(segundo_numero_suma)
        
        resultado_suma = primer_numero_suma + segundo_numero_suma
        
        mensaje_suma = f"El resultado de la suma es {resultado_suma}"
        
        alert("",mensaje_suma)
        
    def btn_restar_on_click(self):
        
        primer_numero_resta = self.txt_operador_a.get()
        primer_numero_resta = int(primer_numero_resta)
        
        segundo_numero_resta = self.txt_operador_b.get()
        segundo_numero_resta = int(segundo_numero_resta)
        
        resultado_resta = primer_numero_resta - segundo_numero_resta
        
        mensaje_resta = f"El resultado de la resta es {resultado_resta}"
        
        alert("",mensaje_resta)

    def btn_multiplicar_on_click(self):
        
        primer_numero_producto = self.txt_operador_a.get()
        primer_numero_producto = int(primer_numero_producto)
        
        segundo_numero_producto = self.txt_operador_b.get()
        segundo_numero_producto = int(segundo_numero_producto)
        
        resultado_producto = primer_numero_producto * segundo_numero_producto
        
        mensaje_producto = f"El resultado de la suma es {resultado_producto}"
        
        alert("",mensaje_producto)
        
    def btn_dividir_on_click(self):
        
        primer_numero_division = self.txt_operador_a.get()
        primer_numero_division = int(primer_numero_division)
        
        segundo_numero_division = self.txt_operador_b.get()
        segundo_numero_division = int(segundo_numero_division)
        
        resultado_division = primer_numero_division / segundo_numero_division
        
        mensaje_division = f"El resultado de la suma es {resultado_division}"
        
        alert("",mensaje_division)
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()