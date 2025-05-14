import hashlib
import os

def leer_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error al leer archivo: {e}"

def encriptar(texto, metodo):
    if metodo == "SHA256":
        return hashlib.sha256(texto.encode()).hexdigest()
    elif metodo == "AES":
        return "🔐 Simulación de AES (aún sin implementar)"
    elif metodo == "RSA":
        return "🔐 Simulación de RSA (aún sin implementar)"
    else:
        return "Método de encriptación no reconocido"

def desencriptar(texto, metodo):
    if metodo == "SHA256":
        return "❌ No se puede desencriptar SHA256 (es un hash unidireccional)"
    elif metodo == "AES":
        return "🔓 Simulación de desencriptado AES (no implementado aún)"
    elif metodo == "RSA":
        return "🔓 Simulación de desencriptado RSA (no implementado aún)"
    else:
        return "Método no reconocido"

def guardar_resultado(texto, modo, metodo):
    carpeta = "resultados"
    os.makedirs(carpeta, exist_ok=True)
    nombre_archivo = f"{modo.lower()}_{metodo.lower()}.txt"
    ruta = os.path.join(carpeta, nombre_archivo)
    with open(ruta, 'w', encoding='utf-8') as file:
        file.write(texto)
    return ruta

def listar_resultados():
    carpeta = "resultados"
    if not os.path.exists(carpeta):
        return []
    return [f for f in os.listdir(carpeta) if f.endswith(".txt")]

def leer_resultado(nombre_archivo):
    ruta = os.path.join("resultados", nombre_archivo)
    return leer_archivo(ruta)
