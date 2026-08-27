import requests

def obtener_cop_clp():
    # Endpoint público de ExchangeRate-API (No requiere API Key)
    # Documentación oficial: https://www.exchangerate-api.com/docs/free
    url = "https://open.er-api.com/v6/latest/COP"
    
    try:
        # Hacemos la consulta a la API con un límite de tiempo de 10 segundos
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Validamos que la consulta fue exitosa
        if data.get("result") == "success":
            # Extraemos la tasa de conversión directa de COP a CLP
            valor_cop_a_clp = data.get("rates", {}).get("CLP")
            
            # Capturamos la fecha de la última actualización desde el servidor de la API
            fecha = data.get("time_last_update_utc", "")
            
            print(f"1 COP equivale a: {valor_cop_a_clp} CLP")
            print(f"(Última actualización de la API: {fecha})")
            
            return valor_cop_a_clp
        else:
            print("La API devolvió un estado de error.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión al obtener el COP: {e}")
        return None
    except KeyError as e:
        print(f"Error procesando los datos de la API (Formato inesperado): {e}")
        return None

if __name__ == "__main__":
    obtener_cop_clp()