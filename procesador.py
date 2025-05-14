import hashlib
import os
from g1 import Atbash, Cesar, Cod_URL, Rail_Fence, ROT13, Vigenere
from g2 import base16, base32, base64, base85
from g3 import XOR


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
        return Cesar.cifrado_cesar(texto, 3)
    elif metodo == "Cod_URL":
        return Cod_URL.codificar_url(texto)
    elif metodo == "ROT13":
        return ROT13.rot13(texto)
    elif metodo == "Rail_Fence":
        return Rail_Fence.codificar_rail_fence(texto, 3)
    elif metodo == "Vigenere":
        return Vigenere.vigenere_codificar(texto, "clave")
    elif metodo == "base16":
        return base16.codificar_base16(texto)
    elif metodo == "base32":
        return base32.codificar_base32(texto)
    elif metodo == "base64":
        return base64.codificar_base64(texto)
    elif metodo == "base85":
        return base85.codificar_base85(texto)
    elif metodo == "XOR":
        return XOR.xor_codificar(texto, "clave")
    else:
        return "Método de encriptación no reconocido"


def desencriptar(texto, metodo):
    if metodo == "Atbash":
        return Atbash.atbash(texto)
    elif metodo == "Cesar":
        return Cesar.descifrado_cesar(texto, 3)
    elif metodo == "Cod_URL":
        return Cod_URL.decodificar_url(texto)
    elif metodo == "ROT13":
        return ROT13.rot13(texto)
    elif metodo == "Rail_Fence":
        return Rail_Fence.decodificar_rail_fence(texto, 3)
    elif metodo == "Vigenere":
        return Vigenere.vigenere_decodificar(texto, "clave")
    elif metodo == "base16":
        return base16.decodificar_base16(texto)
    elif metodo == "base32":
        return base32.decodificar_base32(texto)
    elif metodo == "base64":
        return base64.decodificar_base64(texto)
    elif metodo == "base85":
        return base85.decodificar_base85(texto)
    elif metodo == "XOR":
        return XOR.xor_decodificar(texto, "clave")
    else:
        return "Método de desencriptación no reconocido"


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
