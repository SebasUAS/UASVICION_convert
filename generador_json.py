import json
from datetime import datetime
from get_usd import obtener_usd_clp
from get_uf import obtener_uf_clp
from get_cop import obtener_cop_clp

def compilar_tasas():
    print("Iniciando la extracción de tasas de cambio...")
    
    # Ejecutamos las funciones importadas
    uf = obtener_uf_clp()
    usd = obtener_usd_clp()
    cop = obtener_cop_clp()
    
    # Armamos el diccionario con los datos unificados
    tasas = {
        "UF_CLP": uf,
        "USD_CLP": usd,
        "COP_CLP": cop,
        "ultima_actualizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Generamos el archivo plano JSON
    nombre_archivo = "valores_uasvision.json"
    try:
        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            json.dump(tasas, archivo, indent=4)
        print(f"\n¡Éxito! Archivo '{nombre_archivo}' generado correctamente.")
    except Exception as e:
        print(f"\nError al guardar el archivo JSON: {e}")

if __name__ == "__main__":
    compilar_tasas()