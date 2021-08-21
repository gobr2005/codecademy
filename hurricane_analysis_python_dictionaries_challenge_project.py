# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 2
# Update Recorded Damages
def converted_damages_data(damages):
  conversion = {"M": 1000000,
                "B": 1000000000}
  updated_damages = list()
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage.find("M") != -1: 
      updated_damages.append(float(damage[0:damage.find("M")]) * conversion["M"])
    if damage.find("B") != -1: 
      updated_damages.append(float(damage[0:damage.find("B")]) * conversion["B"])
  return updated_damages

updated_damages = converted_damages_data(damages)
# test function by updating damages
#print(updated_damges)

# 3 
# Create a dictionary
def create_dictionary(names, months, years, max_sustained_winds, areas_affected,     updated_damages, deaths):
  hurricanes = {}
  num_hurricane = len(names)
  # Create and view the hurricanes dictionary
  for i in range(num_hurricane):
    hurricanes[names[i]] = {"Name": names[i], 
                           "Months": months[i], 
                           "Year": years[i], 
                           "Max Sustained Winds": max_sustained_winds[i], 
                           "Areas Affected": areas_affected[i], 
                           "Damages": updated_damages[i],
                           "Deaths": deaths[i]}
  return hurricanes
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)

# 4
# Organizing by Year
def hurricanes_by_years(hurricanes):
  hurricane_year = {}
# create a new dictionary of hurricanes with year and key
  for h in hurricanes:
    current_year = hurricanes[h]["Year"]
    current_cane = hurricanes[h]
    if current_year not in hurricane_year:
      hurricane_year[current_year] = [current_cane]
    else:
      hurricane_year[current_year].append(current_cane)
  return hurricane_year

hurricane_year = hurricanes_by_years(hurricanes)

#print(hurricane_year)
# 5
# Counting Damaged Areas
def count_affected_area(hurricanes):
  damaged_area = {}
# create dictionary of areas to store the number of hurricanes involved in
  for h in hurricanes.values():
    for area in h["Areas Affected"]:
     if area not in damaged_area:
        damaged_area[area] = 1
     else:
       damaged_area[area] += 1
  return damaged_area

damaged_area = count_affected_area(hurricanes)

#print(damaged_area)
# 6 
# Calculating Maximum Hurricane Count
def most_affected_area(count_affected_area):
  max_num_hurricanes = 0
  max_location = "none"
  # find most frequently affected area and the number of hurricanes involved in
  for l in damaged_area:
    if damaged_area[l] > max_num_hurricanes:
      max_num_hurricanes = damaged_area[l]
      max_location = l
  return max_location, max_num_hurricanes

max_location, max_num_hurricanes = most_affected_area(count_affected_area)

#print(max_location + " had " + str(max_num_hurricanes) + " hurricanes hit them.")    

# 7
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes):
  # find highest mortality hurricane and the number of deaths
  max_mortality_cane = 'Cuba I'
  max_mortality = 0
  for h in hurricanes:
    if hurricanes[h]["Deaths"] > max_mortality:
      max_mortality = hurricanes[h]["Deaths"]
      max_mortality_cane = h
  return max_mortality_cane, max_mortality

max_mortality_cane, max_mortality = deadliest_hurricane(hurricanes)
#print(max_mortality_cane, max_mortality)

# 8
def categorize_by_mortality(hurricanes):
  # Rating Hurricanes by Mortality
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  # categorize hurricanes in new dictionary with mortality severity as key
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] > mortality_scale[0] and hurricanes[cane]["Deaths"] <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] > mortality_scale[1] and hurricanes[cane]["Deaths"] <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] > mortality_scale[2] and hurricanes[cane]["Deaths"] <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] > mortality_scale[3] and hurricanes[cane]["Deaths"] <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricanes[cane])    
  return hurricanes_by_mortality

hurricanes_by_mortality = categorize_by_mortality(hurricanes)

# print(hurricanes_by_mortality)

# 9 Calculating Hurricane Maximum Damage
def hurrican_max_damage(hurricanes):
  most_damage = 0
  hurricane_name = 0
  # find highest damage inducing hurricane and its total cost
  for cane in hurricanes:
    if hurricanes[cane]["Damages"] == "Damages not recorded":
      pass
    elif hurricanes[cane]["Damages"] > most_damage:
     most_damage = hurricanes[cane]["Damages"]
     hurricane_name = cane
  return most_damage, hurricane_name
most_damage, hurricane_name = hurrican_max_damage(hurricanes)

# print(str(most_damage) + " " + hurricane_name)

# 10
# Rating Hurricanes by Damage
def hurricanes_by_damage(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}  
  # categorize hurricanes in new dictionary with damage severity as key
  hurricanes_damage_scale = {0:[], 1:[], 2:[],3:[], 4:[], 5:[]}
  for canes in hurricanes:
    if hurricanes[canes]["Damages"] == "Damages not recorded":
      hurricanes_damage_scale[0].append(hurricanes[canes])
    elif hurricanes[canes]["Damages"] == 0:
      hurricanes_damage_scale[0].append(hurricanes[canes])
    elif hurricanes[canes]["Damages"] > damage_scale[0] and hurricanes[canes]["Damages"] <= damage_scale[1]:
      hurricanes_damage_scale[1].append(hurricanes[canes])
    elif hurricanes[canes]["Damages"] > damage_scale[1] and hurricanes[canes]["Damages"] <= damage_scale[2]:
      hurricanes_damage_scale[2].append(hurricanes[canes])
    elif hurricanes[canes]["Damages"] > damage_scale[2] and hurricanes[canes]["Damages"] <= damage_scale[3]:
      hurricanes_damage_scale[3].append(hurricanes[canes])
    elif hurricanes[canes]["Damages"] > damage_scale[3] and hurricanes[canes]["Damages"] <= damage_scale[4]:
      hurricanes_damage_scale[4].append(hurricanes[canes])
    elif hurricanes[canes]["Damages"] > damage_scale[4] :
      hurricanes_damage_scale[5].append(hurricanes[canes])
  return hurricanes_damage_scale

hurricanes_damage_scale = hurricanes_by_damage(hurricanes)

print(hurricanes_damage_scale)
