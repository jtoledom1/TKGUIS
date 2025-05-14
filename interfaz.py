# interfaz.py

import customtkinter as ctk
import tkinter.filedialog
import procesador
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("1000x680")
root.title("ToledinsKEY")

# --- Frames
left_frame = ctk.CTkFrame(root, width=500, fg_color="#4D7CFE", corner_radius=0)
left_frame.pack(side="left", fill="both")

right_frame = ctk.CTkFrame(root, width=500, fg_color="white", corner_radius=0)
right_frame.pack(side="right", fill="both", expand=True)

# --- Contenido izquierdo
ctk.CTkLabel(left_frame, text="Welcome to ToledinsKEY", font=("Arial Bold", 24), text_color="white").pack(pady=(80, 10), padx=20, anchor="w")
ctk.CTkLabel(left_frame, text="___________________________", font=("Arial", 20), text_color="white").pack(padx=20, anchor="w")
ctk.CTkLabel(left_frame,
    text=("Tkinter Designer uses Figma API to\n"
          "analyse the design file and creates the\n"
          "respective code and files needed for the GUI.\n\n"
          "Even Tkinter Designer's GUI is created using\n"
          "Tkinter Designer."),
    justify="left",
    font=("Arial", 16),
    text_color="white"
).pack(pady=(10, 30), padx=20, anchor="w")

# --- Selector de modo
modo_label = ctk.CTkLabel(left_frame, text="Modo de operación", font=("Arial", 18), text_color="white")
modo_label.pack(pady=(10, 5), padx=20, anchor="w")

def limpiar_campos():
    global texto_actual
    texto_actual = ""
    file_entry.delete(0, "end")
    preview_text.configure(state="normal")
    preview_text.delete("1.0", "end")
    preview_text.insert("1.0", "Aquí aparecerá el contenido del archivo...")
    preview_text.configure(state="disabled")
    resultado_text.configure(state="normal")
    resultado_text.delete("1.0", "end")
    resultado_text.insert("1.0", "Aquí se mostrará el resultado de la operación")
    resultado_text.configure(state="disabled")

def cambio_modo_callback(opcion):
    limpiar_campos()

modo_menu = ctk.CTkOptionMenu(
    left_frame,
    values=["Encriptar", "Desencriptar"],
    command=cambio_modo_callback,
    width=200
)
modo_menu.set("Encriptar")
modo_menu.pack(padx=20, anchor="w")

# --- Contenido derecho
ctk.CTkLabel(right_frame, text="Empecemos a encriptar!", font=("Arial Bold", 22), text_color="#3E3F7D").pack(pady=(40, 20))

file_entry = ctk.CTkEntry(right_frame, placeholder_text="Selecciona un archivo .txt", width=300)
file_entry.pack(pady=10)

preview_text = ctk.CTkTextbox(right_frame, width=400, height=160)
preview_text.pack(pady=10)
preview_text.insert("1.0", "Aquí aparecerá el contenido del archivo...")
preview_text.configure(state="disabled")

resultado_text = ctk.CTkTextbox(right_frame, width=400, height=120)
resultado_text.pack(pady=(5, 10))
resultado_text.insert("1.0", "Aquí se mostrará el resultado de la operación")
resultado_text.configure(state="disabled")

texto_actual = ""

def open_file():
    global texto_actual
    path = tkinter.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        contenido = procesador.leer_archivo(path)
        texto_actual = contenido
        file_entry.delete(0, "end")
        file_entry.insert(0, path)

        preview_text.configure(state="normal")
        preview_text.delete("1.0", "end")
        preview_text.insert("1.0", contenido)
        preview_text.configure(state="disabled")

def generar_operacion():
    metodo = encrypt_menu.get()
    modo = modo_menu.get()

    if not texto_actual:
        resultado = "⚠️ Primero carga un archivo."
    else:
        if modo == "Encriptar":
            resultado = procesador.encriptar(texto_actual, metodo)
        elif modo == "Desencriptar":
            resultado = procesador.desencriptar(texto_actual, metodo)
        else:
            resultado = "❓ Modo inválido"

        # Guardar resultado
        ruta_guardado = procesador.guardar_resultado(resultado, modo, metodo)
        resultado += f"\n\n✅ Resultado guardado en:\n{ruta_guardado}"

    resultado_text.configure(state="normal")
    resultado_text.delete("1.0", "end")
    resultado_text.insert("1.0", resultado)
    resultado_text.configure(state="disabled")

# Botones
ctk.CTkButton(right_frame, text="📂 Cargar archivo", width=300, command=open_file).pack(pady=10)

encrypt_menu = ctk.CTkOptionMenu(
    right_frame,
    values=[
        "Atbash", "Cesar", "Cod_URL", "ROT13", "Rail_Fence", "Vigenere",
        "base16", "base32", "base64", "base85",
        "XOR"
    ],
    width=300
)


encrypt_menu.set("Tipo de encripción")
encrypt_menu.pack(pady=10)

ctk.CTkButton(right_frame, text="✅ Generar", width=300, command=generar_operacion).pack(pady=10)
# interfaz.py

# ... [código anterior intacto arriba] ...


# (Después de crear modo_menu...)

# --- Archivos generados
ctk.CTkLabel(left_frame, text="Archivos generados", font=("Arial", 18), text_color="white").pack(pady=(20, 5), padx=20, anchor="w")

# Botón para actualizar lista
def actualizar_lista_archivos():
    archivos = procesador.listar_resultados()
    if archivos:
        archivo_selector.configure(values=archivos)
        archivo_selector.set(archivos[0])
        mostrar_contenido_archivo(archivos[0])
    else:
        archivo_selector.configure(values=["(sin archivos)"])
        archivo_selector.set("(sin archivos)")
        resultado_text.configure(state="normal")
        resultado_text.delete("1.0", "end")
        resultado_text.insert("1.0", "No hay archivos generados aún.")
        resultado_text.configure(state="disabled")

# Mostrar contenido seleccionado
def mostrar_contenido_archivo(nombre_archivo):
    if nombre_archivo and nombre_archivo != "(sin archivos)":
        contenido = procesador.leer_resultado(nombre_archivo)
        resultado_text.configure(state="normal")
        resultado_text.delete("1.0", "end")
        resultado_text.insert("1.0", contenido)
        resultado_text.configure(state="disabled")

# Botón actualizar archivos
ctk.CTkButton(left_frame, text="📁 Ver archivos generados", width=200, command=actualizar_lista_archivos).pack(padx=20, pady=(5, 5), anchor="w")

# Menú desplegable de archivos
archivo_selector = ctk.CTkOptionMenu(left_frame, values=["(sin archivos)"], command=mostrar_contenido_archivo, width=200)
archivo_selector.set("(sin archivos)")
archivo_selector.pack(padx=20, pady=(0, 10), anchor="w")

# Ejecutar
root.mainloop()
