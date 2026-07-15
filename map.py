import folium
import random

# center map on langley/vancouver area
map1 = folium.Map(location=[49.15, -122.6], zoom_start=10)

# fake crash data list to simulate bc open data
# format: [lat, lon, location name, number of crashes]
crash_data = []

for i in range(50):
    lat = random.uniform(49.02, 49.30)
    lon = random.uniform(-123.15, -122.25)
    crashes = random.randint(1, 20) # random number of crashes
    crash_data.append([lat, lon, f"Intersection {i}", crashes])

# variables to count bad spots
dangerous_spots = 0
total_spots = len(crash_data)

# loop through the list to add markers to map
for spot in crash_data:
    latitude = spot[0]
    longitude = spot[1]
    name = spot[2]
    num_crashes = spot[3]
    
    # check if the intersection is dangerous
    if num_crashes >= 12:
        color_choice = "red"
        status = "Dangerous - High Crash Zone"
        dangerous_spots = dangerous_spots + 1
    elif num_crashes >= 6:
        color_choice = "orange"
        status = "Medium Risk"
    else:
        color_choice = "green"
        status = "Safe"
        
    # put marker on map
    folium.Marker(
        location=[latitude, longitude],
        popup=f"{name}: {num_crashes} crashes. Status: {status}",
        icon=folium.Icon(color=color_choice)
    ).add_to(map1)

# save the map file
map1.save("index.html")

# casual print statements that look like a student wrote them
print("Map code finished running!")
print("Total intersections checked:", total_spots)
print("Dangerous red zones found:", dangerous_spots)
