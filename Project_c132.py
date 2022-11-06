import csv

rows = []

with open("Nasa_Exoplanet_Archive.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

    headers = rows[0]
    planet_data_rows = rows[1:]


headers[0] = "XXXXX"

solar_system_planet_count = {}
for planet_data in planet_data_rows:
  if solar_system_planet_count.get(planet_data[11]):
    solar_system_planet_count[planet_data[11]] += 1
  else:
    solar_system_planet_count[planet_data[11]] = 1

max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)
print("The solar system {} has the maximum number of {} planets out of all the solar systems discovered.".format(max_solar_system, solar_system_planet_count[max_solar_system]))


temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  planet_mass = planet_data[3]
  if planet_mass.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_mass_value = planet_mass.split(" ")[0]
    planet_mass_ref = planet_mass.split(" ")[1]
    if planet_mass_ref == "Jupiters":
      planet_mass_value = float(planet_mass_value) * 317.8
    planet_data[3] = planet_mass_value

  planet_radius = planet_data[7]
  if planet_radius.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_radius_value = planet_radius.split(" ")[0]
    planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
      planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value


hd_10180_planets = []
for planet_data in planet_data_rows:
  if max_solar_system == planet_data[11]:
    hd_10180_planets.append(planet_data)

import plotly.express as px

hd_10180_planet_masses = []
hd_10180_planet_names = []
for planet_data in hd_10180_planets:
  hd_10180_planet_masses.append(planet_data[3])
  hd_10180_planet_names.append(planet_data[1])

hd_10180_planet_masses.append(1)
hd_10180_planet_names.append("Earth")

fig = px.bar(x=hd_10180_planet_names, y=hd_10180_planet_masses)
fig.show()

temp_planet_data_rows = list(planet_data_rows)

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()

low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 10:
    low_gravity_planets.append(planet_data_rows[index])


planet_type_values = []
for planet_data in planet_data_rows:
    planet_type_values.append(planet_data[6])

print(list(set(planet_type_values)))

planet_masses = []
planet_radiuses=[]
for planet_data in low_gravity_planets:
    planet_masses.append(planet_data[3])
    planet_radiuses.append(planet_data[7])

fig = px.scatter(x=planet_radiuses, y=planet_masses, title="Project_C132 - Comparing Radii with Masses")
fig.update_layout(xaxis_title="Planet Radius", yaxis_title="Planet Masses")
fig.show()

planet_masses = []
planet_radiuses = []
planet_types = []
for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_types.append(planet_data[6])

fig = px.scatter(x=planet_radiuses, y=planet_masses, color=planet_types, title="Project C132 - Comparing Radii with Planet Type")
fig.update_layout(xaxis_title="Planet Radius", yaxis_title="Planet Types")
fig.show()

suitable_planets = []
for planet_data in low_gravity_planets:
  if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth":
    suitable_planets.append(planet_data)

print(len(suitable_planets))