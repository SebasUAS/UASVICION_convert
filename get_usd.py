import bcchapi
import pandas as pd
from datetime import datetime, timedelta

def obtener_usd_clp(): # O obtener_uf_clp()
    # GitHub inyectará el token de forma segura al ejecutar
    TOKEN = os.getenv("BCCH_TOKEN") 
    
    siete = bcchapi.Siete(token=TOKEN)
    
    # 1. Inicializamos la conexión oficial
    siete = bcchapi.Siete(token=TOKEN)
    
    # 2. Definimos una ventana de tiempo (los últimos 7 días)
    # Esto garantiza que si hoy es domingo, el script retroceda hasta encontrar el valor del viernes.
    fecha_fin = datetime.now().strftime("%Y-%m-%d")
    fecha_inicio = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    
    try:
        # 3. Consultamos la base de datos estructurada
        df = siete.cuadro(
            series=["F073.TCO.PRE.Z.D"], 
            nombres=["USD"], 
            desde=fecha_inicio, 
            hasta=fecha_fin
        )
        
        # 4. Magia de Pandas: Eliminamos los días sin valor (dropna) y sacamos el último registro (iloc[-1])
        ultimo_valor = float(df['USD'].dropna().iloc[-1])
        
        print(f"Valor USD Obtenido: {ultimo_valor} CLP")
        return ultimo_valor
        
    except Exception as e:
        print(f"Error al conectar con BCCh: {e}")
        return None

if __name__ == "__main__":
    obtener_usd_clp()