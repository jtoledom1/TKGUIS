import customtkinter as ctk
import tkinter.filedialog

# Configuración general
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Ventana principal
root = ctk.CTk()
root.geometry("1000x650")
root.title("ToledinsKEY")

# Frames principales
left_frame = ctk.CTkFrame(root, width=500, fg_color="#4D7CFE", corner_radius=0)
left_frame.pack(side="left", fill="both")

right_frame = ctk.CTkFrame(root, width=500, fg_color="white", corner_radius=0)
right_frame.pack(side="right", fill="both", expand=True)

# --- CONTENIDO IZQUIERDO ---
title = ctk.CTkLabel(
    left_frame,
    text="Welcome to ToledinsKEY",
    font=("Arial Bold", 24),
    text_color="white",
)
title.pack(pady=(100, 10), padx=20, anchor="w")

line = ctk.CTkLabel(
    left_frame,
    text="___________________________",
    font=("Arial", 20),
    text_color="white",
)
line.pack(padx=20, anchor="w")

desc = ctk.CTkLabel(
    left_frame,
    text=(
        "Tkinter Designer uses Figma API to\n"
        "analyse the design file and creates the\n"
        "respective code and files needed for the GUI.\n\n"
        "Even Tkinter Designer's GUI is created using\n"
        "Tkinter Designer."
    ),
    justify="left",
    font=("Arial", 16),
    text_color="white",
)
desc.pack(pady=(10, 0), padx=20, anchor="w")

# --- CONTENIDO DERECHO ---
right_title = ctk.CTkLabel(
    right_frame,
    text="Empecemos a encriptar!",
    font=("Arial Bold", 22),
    text_color="#3E3F7D",
)
right_title.pack(pady=(40, 20))

# Entrada de archivo
file_entry = ctk.CTkEntry(right_frame, placeholder_text="Selecciona un archivo .txt", width=300)
file_entry.pack(pady=10)

# Caja de texto para mostrar contenido
preview_text = ctk.CTkTextbox(right_frame, width=400, height=180)
preview_text.pack(pady=(10, 5))
preview_text.insert("1.0", "Aquí aparecerá el contenido del archivo...")
preview_text.configure(state="disabled")

# Función para seleccionar archivo y leer contenido
def open_file():
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            file_entry.delete(0, "end")
            file_entry.insert(0, file_path)

            # Mostrar contenido en el textbox
            preview_text.configure(state="normal")
            preview_text.delete("1.0", "end")
            preview_text.insert("1.0", content)
            preview_text.configure(state="disabled")

# Botón de cargar archivo
file_button = ctk.CTkButton(
    right_frame,
    text="📂 Cargar archivo",
    width=300,
    command=open_file
)
file_button.pack(pady=10)

# Menú tipo de encripción
encrypt_menu = ctk.CTkOptionMenu(
    right_frame,
    values=["AES", "RSA", "SHA256"],
    width=300
)
encrypt_menu.set("Tipo de encripción")
encrypt_menu.pack(pady=10)

# Botón generar
generate_button = ctk.CTkButton(
    right_frame,
    text="🔐 Generar",
    width=300,
    command=lambda: print("¡Encriptando con método:", encrypt_menu.get(), "!")
)
generate_button.pack(pady=10)

# Ejecutar app
root.mainloop()
