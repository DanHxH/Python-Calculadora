import tkinter as tk

# Función para evaluar la expresión matemática
def evaluate(event=None):
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Función para agregar caracteres a la expresión matemática
def add_to_expression(character):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(character))

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")

# Crear campo de entrada para la expresión matemática
display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Crear botones de la calculadora
buttons = []
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

for i, text in enumerate(button_texts):
    button = tk.Button(root, text=text, font=("Arial", 18), borderwidth=2, relief="ridge", 
                       command=lambda t=text: add_to_expression(t) if t != '=' else evaluate())
    button.grid(row=i//4+1, column=i%4, padx=5, pady=5, sticky="nsew")
    buttons.append(button)

# Botón para borrar (Clear)
clear_button = tk.Button(root, text='C', font=("Arial", 18), borderwidth=2, relief="ridge", 
                         command=lambda: display.delete(0, tk.END))
clear_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

# Configurar redimensionamiento de los botones y el display
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Hacer que la tecla 'Enter' evalúe la expresión
root.bind('<Return>', evaluate)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
