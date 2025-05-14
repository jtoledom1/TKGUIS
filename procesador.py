import hashlib
import os
from g1 import Atbash, Cesar, Cod_URL, Rail_Fence, ROT13, Vigenere


def leer_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error al leer archivo: {e}"

def encriptar(texto, metodo):
    if metodo == "Atbash":
        return Atbash.atbash(texto)
    elif metodo == "Cesar":
        return Cesar.cifrado_cesar(texto,3)
    elif metodo == "Cod_URL":
        return Cod_URL.codificar_url(texto)
    elif metodo == "Rail_Fence":
        return Rail_Fence.codificar_rail_fence(texto,20)
    elif metodo == "ROT13":
        return "🔐 Simulación de ROT13 (aún sin implementar)"
    elif metodo == "Vigenere":
        return "🔐 Simulación de Vigenere (aún sin implementar)"
    else:
        return "Método de encriptación no reconocido"

def desencriptar(texto, metodo):
    if metodo == "Atbash":
        return Atbash.atbash(texto)
    elif metodo == "Cesar":
        return Cesar.descifrado_cesar(texto,3)
    elif metodo == "Cod_URL":
        return Cod_URL.decodificar_url(texto)
    elif metodo == "Rail_Fence":
        return Rail_Fence.decodificar_rail_fence(texto,20)
    elif metodo == "ROT13":
        return "🔐 Simulación de ROT13 (aún sin implementar)"
    elif metodo == "Vigenere":
        return "🔐 Simulación de Vigenere (aún sin implementar)"
    else:
        return "Método de encriptación no reconocido"

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
