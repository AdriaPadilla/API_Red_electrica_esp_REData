# librerias
import requests
import json
import os
from datetime import datetime

# Parametros de guardado de datos
output_folder = "data/" # carpeta de exportación
time = datetime.now() # fecha de la petición
filename = f"{time}--datos" # Nombre del archivo de salida

# Aquí tienes la lista de parametros admitidos = https://www.ree.es/es/apidatos
# Nota importante: Ten en cuenta que la API tiene limitaciones y rangos de datos. 
# Por ejemplo, no es posible recuperar los precios de la energia hora a hora de un periodo superior a un mes.
# No hay listado de incompatibilidades de petición. 

# Parametros de configuración de la petición:
base_url = "https://apidatos.ree.es"
lang = "es"
category = "mercados"
widget = "precios-mercados-tiempo-real"
start_date = "2022-12-21T00:00"
end_date = "2022-12-21T14:00"
time_trunc = "hour" # hour / day / month / year
geo_trunc = "electric_system" #unico valor permitido
geo_limit = "peninsular"
region_id = "8741"

# Función principal
def get_data():
    response = requests.get(f"{base_url}/{lang}/datos/{category}/{widget}?start_date={start_date}&end_date={end_date}&time_trunc={time_trunc}&geo_trunc={geo_trunc}&geo_limit={geo_limit}&geo_ids={region_id}")
    data = response.json()
    
    # Exportación de los datos (creará carpeta definida en variable "output_folder")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open((output_folder + f"{filename}.json").replace(" ", "T"), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print("done")

get_data()
