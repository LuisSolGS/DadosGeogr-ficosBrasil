import json

try:
    with open("BrazilMun.geojson", 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)
    if 'type' in geojson_data:
        print(f"GeoJSON type: {geojson_data['type']}")
    else:
        print("No 'type' key found in GeoJSON data.")
   
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from '{file_path}'. Check if it's a valid GeoJSON/JSON file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    

states = {}
for x in range(len(geojson_data["features"])):
    uf = dict(geojson_data["features"][x])['properties']['UF']
    if (uf not in states.keys()):
        states[uf] =  [dict(geojson_data["features"][x])];
    else:
        states[uf].append(dict(geojson_data["features"][x]));
        
for uf in states.keys():
    f = open("estados/" + uf + ".geojson", 'w', encoding='utf-8')
    data = {"type": "FeatureCollection",
            "name": "municipios "+ uf,
            "features": states[uf]}
    json.dump(data, f, indent=4)
    print(uf + ".geojson writen")
    #for city in states[uf]:
    #    f.write(city + ',')
    #f.seek(-1, os.SEEK_CUR)
    #f.write("]}")
