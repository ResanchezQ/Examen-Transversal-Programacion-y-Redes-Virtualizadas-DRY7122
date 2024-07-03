import requests
print("bienvenidos a nuestro sistema de mapa")
print("para salir usar S")
def obtener_coordenadas(ciudad, pais, api_key):
    url = "https://graphhopper.com/api/1/geocode"
    params = {
        "q": f"{ciudad}, {pais}",
        "locale": "es",
        "limit": 1,
        "key": "9fdda051-f6b3-4061-9332-8547d9851355"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['hits']:
        location = data['hits'][0]['point']
        return (location['lat'], location['lng'])
    else:
        print("No se encontraron coordenadas para la ubicación dada.")
        return None

def obtener_ruta(coordenadas_origen, coordenadas_destino, medio_transporte, api_key):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [f"{coordenadas_origen[0]},{coordenadas_origen[1]}", f"{coordenadas_destino[0]},{coordenadas_destino[1]}"],
        "vehicle": medio_transporte,
        "locale": "es",
        "key": api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    api_key = "9fdda051-f6b3-4061-9332-8547d9851355"  # Reemplaza con tu propia API Key
    while True:
        ciudad_origen = input("Ciudad de Origen: ")
        if ciudad_origen.lower() == 's':
            break
        ciudad_destino = input("Ciudad de Destino: ")
        if ciudad_destino.lower() == 's':
            break
        medio_transporte = input("Medio de transporte (car, bike, foot): ")
        if medio_transporte.lower() == 's':
            break

        coordenadas_origen = obtener_coordenadas(ciudad_origen, "Chile", api_key)
        coordenadas_destino = obtener_coordenadas(ciudad_destino, "Argentina", api_key)

        if coordenadas_origen and coordenadas_destino:
            ruta = obtener_ruta(coordenadas_origen, coordenadas_destino, medio_transporte, api_key)

            distancia_km = ruta["paths"][0]["distance"] / 1000
            distancia_millas = distancia_km * 0.621371
            duracion_segundos = ruta["paths"][0]["time"] / 1000
            duracion_minutos = duracion_segundos / 60
            narrativa = ruta["paths"][0]["instructions"]

            print(f"Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
            print(f"Duración del viaje: {duracion_minutos:.2f} minutos")
            print("Narrativa del viaje:")
            for paso in narrativa:
                print(f"- {paso['text']} ({paso['distance'] / 1000:.2f} km)")

if __name__ == "__main__":
    main()


