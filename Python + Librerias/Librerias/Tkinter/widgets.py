import tkinter as tk

#crear ventana principal
root = tk.Tk()

#configura ventana 
root.title("Widgets")
root.geometry("900x600")#Alto x Ancho

""" 15 widgets más usados ​​en Tkinter """
# 1. Label(Etiqueta)
label = tk.Label(root, text="oprime el boton", font=("Arial", 10))
label.pack(side="right")

#  2. Button(Botón)
button = tk.Button(root, text="Click 😝", font=("Arial",10) )
button.pack(side="right")

# 3. Entry(Campo de texto)
entry=tk.Entry(root, font=("Arial", 10))
entry.pack(pady=10)

# 4. Text(Área de texto)
text = tk.Text(root, height=5, width= 15)
text.pack(pady=7)

# 5. Checkbutton(Casilla de verificación)
var = tk.IntVar()
check = tk.Checkbutton(root, text="Aceptar terminos y condiciones", variable=var) 
check.pack(pady=10)

#6. Radiobutton(Botón de radio)
var2 = tk.IntVar()
radio1 = tk.Radiobutton(root, text="Opcion 1", variable=var2, value= 1)
radio2 = tk.Radiobutton(root, text="Opcion 2", variable=var2, value= 2)
radio1.pack(pady=5)
radio2.pack(pady=5)

# 7. Listbox(Lista desplegable)
listbox = tk.Listbox(root)
listbox.pack(side="left")
listbox.insert(1,"Python")
listbox.insert(2, "Java")
listbox.insert(3, "Ruby")

#8. Spinbox(Selector numérico)
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack(pady= 10)

#9. Scale(Deslizador)
scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack(pady=10)

#10. Scrollbar(Barra de desplazamiento)
text.pack(side="left")

scroll = tk.Scrollbar(root, command=text.yview)
scroll.pack(side="right",fill="y")


#11. Frame(Contenedor)
frame = tk.Frame(root, relief="ridge", borderwidth=2)
frame.pack(pady=10)

label1 = tk.Label(frame, text="11. Dentro del frame")
label1.pack(pady=5)

# 12. Canvas(Dibujos)
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

canvas.create_line(10,10,100,90, fill = "blue")
canvas.create_rectangle(50, 20, 90, 80, outline="red")

#13. Toplevel(Ventana secundaria)
def abrir_ventana():
    ventana = tk.Toplevel()
    ventana.title("Nueva ventana")
    ventana.geometry("200x300")
    tk.Label(ventana, text="Hola").pack()

btn = tk.Button(root, text="Abrir ventana", command=abrir_ventana)
btn.pack()
#14. Menu(Menú desplegable)
menu= tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Abrir")
file_menu.add_command(label="Guardar")
file_menu.add_separator()
file_menu.add_command(label="salir", command=root.quit)

menu.add_cascade(label="Archivo", menu=file_menu)

#15. Messagebox(Cuadros de diálogo)
from tkinter import messagebox
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "Hola desde tkinter")
btn = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
btn.pack(pady=10)



# Ejecuta el bucle de la aplicacion 
root.mainloop()