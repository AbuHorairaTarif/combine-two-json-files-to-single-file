import json

# Read the contents of the files
with open('hotels.json', 'r') as hotels_file:
    hotels_data = json.load(hotels_file)

with open('locations.json', 'r') as locations_file:
    locations_data = json.load(locations_file)

# Create a dictionary for coordinates to state mapping
coord_to_state = {(loc['latitude'], loc['longitude']): loc['abbr'] for loc in locations_data}

# Add state information to hotels data
for hotel in hotels_data:
    latitude = str(hotel['latitude'])
    longitude = str(hotel['longitude'])
    coordinates = (latitude, longitude)
    
    if coordinates in coord_to_state:
        hotel['state'] = coord_to_state[coordinates]
    else:
        hotel['state'] = 'Unknown'

# Write the updated hotel data to a new JSON file
with open('hotels_with_state.json', 'w') as output_file:
    json.dump(hotels_data, output_file, indent=2)

print("Data has been combined and written to 'hotels_with_state.json'.")

