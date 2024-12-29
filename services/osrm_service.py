import requests

def get_optimal_route(origin, destination):
    base_url = "http://router.project-osrm.org/route/v1/driving"
    url = f"{base_url}/{origin[1]},{origin[0]};{destination[1]},{destination[0]}"
    params = {
        "overview": "full",
        "geometries": "geojson"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        route_data = response.json()
        route = route_data['routes'][0]
        return {
            "distance": route['distance'], 
            "duration": route['duration'], 
            "geometry": route['geometry']
        }
    else:
        return None
