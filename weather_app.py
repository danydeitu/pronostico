import requests

def obtener_pronostico(ciudad):
 
    api_key = '0f9fbd50a830e723fe7ef447a81d9524'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'

    # solicitud a la API
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código 200)
    if respuesta.status_code == 200:
        datos = respuesta.json()

        # Mostrar datos del pronóstico
        print(f'Datos crudos de la API: {datos}')

        # Acceder a información específica
        temperatura = datos['main']['temp']
        descripcion = datos['weather'][0]['description']

        # Mostrar datos específicos del pronóstico
        print(f'Pronóstico para {ciudad}: Temperatura {temperatura}°C, {descripcion}')
    else:
        print(f'Error al obtener el pronóstico. Código de error: {respuesta.status_code}')

# Ejemplo de uso
ciudad = 'San Miguel'
obtener_pronostico(ciudad)
