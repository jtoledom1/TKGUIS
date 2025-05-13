import customtkinter as ctk
import tkinter.filedialog
from logica import procesador  # 👈 importamos nuestra lógica

# Configuración general
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Crear ventana
root = ctk.CTk()
root.geometry("1000x650")
root.title("ToledinsKEY")

# Frames
left_frame = ctk.CTkFrame(root, width=500, fg_color="#4D7CFE", corner_radius=0)
left_frame.pack(side="left", fill="both")

right_frame = ctk.CTkFrame(root, width=500, fg_color="white", corner_radius=0)
right_frame.pack(side="right", fill="both", expand=True)

# Lado izquierdo
ctk.CTkLabel(left_frame, text="Welcome to ToledinsKEY", font=("Arial Bold", 24), text_color="white").pack(pady=(100, 10), padx=20, anchor="w")
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
).pack(pady=(10, 0), padx=20, anchor="w")

# Lado derecho
ctk.CTkLabel(right_frame, text="Empecemos a encriptar!", font=("Arial Bold", 22), text_color="#3E3F7D").pack(pady=(40, 20))

file_entry = ctk.CTkEntry(right_frame, placeholder_text="Selecciona un archivo .txt", width=300)
file_entry.pack(pady=10)

# TextBox para contenido del archivo
preview_text = ctk.CTkTextbox(right_frame, width=400, height=160)
preview_text.pack(pady=10)
preview_text.insert("1.0", "Aquí aparecerá el contenido del archivo...")
preview_text.configure(state="disabled")

# TextBox para resultado cifrado
resultado_text = ctk.CTkTextbox(right_frame, width=400, height=120)
resultado_text.pack(pady=(5, 10))
resultado_text.insert("1.0", "Aquí se mostrará el resultado de la encriptación")
resultado_text.configure(state="disabled")

# Variable global para el texto leído
texto_actual = ""

# Función para abrir archivo
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

# Función para encriptar usando lógica externa
def generar_encriptado():
    metodo = encrypt_menu.get()
    if not texto_actual:
        resultado = "⚠️ Primero carga un archivo."
    else:
        resultado = procesador.encriptar(texto_actual, metodo)

    resultado_text.configure(state="normal")
    resultado_text.delete("1.0", "end")
    resultado_text.insert("1.0", resultado)
    resultado_text.configure(state="disabled")

# Botones y menú
ctk.CTkButton(right_frame, text="📂 Cargar archivo", width=300, command=open_file).pack(pady=10)

encrypt_menu = ctk.CTkOptionMenu(right_frame, values=["AES", "RSA", "SHA256"], width=300)
encrypt_menu.set("Tipo de encripción")
encrypt_menu.pack(pady=10)

ctk.CTkButton(right_frame, text="🔐 Generar", width=300, command=generar_encriptado).pack(pady=10)

# Ejecutar app
root.mainloop()
