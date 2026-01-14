import openrouteservice

# Create client
client = openrouteservice.Client(key='hidden') 

# Coordinates (longitude, latitude)
locations = {
    "Delhi": (77.1025, 28.7041),
    "Surat": (72.8311, 21.1702),
    "Lucknow": (80.9462, 26.8467),
    "Bangalore": (77.5946, 12.9716)
}

# Kanpur coordinates
kanpur_coords = (80.3468, 26.4499)

# Loop through each destination
for city, dest_coords in locations.items():
    coords = (kanpur_coords, dest_coords)
    route = client.directions(coords)
    summary = route['routes'][0]['summary']

    # Convert distance to kilometers
    distance_km = summary['distance'] / 1000

    # Convert duration to hours and minutes
    duration_sec = summary['duration']
    hours = int(duration_sec // 3600)
    minutes = int((duration_sec % 3600) // 60)

    print(f"{city}: {distance_km:.1f} km, {hours} hours {minutes} minutes")
    

'''Delhi: 466.8 km, 5 hours 41 minutes
Surat: 1163.2 km, 13 hours 53 minutes
Lucknow: 86.8 km, 1 hours 7 minutes
Bangalore: 1787.0 km, 22 hours 3 minutes'''
