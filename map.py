import folium

# 1. Initialize the regional map layout
my_map = folium.Map(location=[49.1500, -122.6000], zoom_start=10)

# 2. Store your geographic data arrays in a clean matrix list
# Structure: [Latitude, Longitude, Location Name, Marker Color, Icon Design]
locations_data = [
    [49.1044, -122.6578, "Langley: Infrastructure Node", "blue", "home"],
    [49.2827, -123.1207, "Vancouver: Supply Chain Hub", "red", "cloud"],
    [49.0504, -122.3045, "Abbotsford: Agricultural Center", "green", "leaf"],
    [49.2001, -122.9109, "New Westminster: Logistics Junction", "orange", "flag"],
    [49.2488, -122.7567, "Coquitlam: Spatial Grid Check", "purple", "info-sign"]
]

# 3. Use a programmatic loop to instantly deploy all tracking markers
for station in locations_data:
    folium.Marker(
        location=[station[0], station[1]],
        popup=station[2],
        tooltip="Click to inspect data log",
        icon=folium.Icon(color=station[3], icon=station[4])
    ).add_to(my_map)

# 4. Save the compiled program output
my_map.save("index.html")
print("Data loop executed! 5 regional markers compiled successfully.")
