# data provided
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

# data analysed using python
# 1
# update recorded damages into numerical form
updated_damages = []
# create function to update damages into numerical form
def damages_in_float(input_1):
    conversion = {"B": 1000000000, "M": 1000000}
    for damage in input_1:
        if "M" in damage:
            new_value = float(damage.strip("M"))
            conversion_rate = conversion.get("M")
            final = new_value * conversion_rate
            updated_damages.append(final)
        elif "B" in damage:
            new_value = float(damage.strip("B"))
            conversion_rate = conversion.get("B")
            final = new_value * conversion_rate
            updated_damages.append(final)
        else:
            updated_damages.append(damage)
damages_in_float(damages)
'''print(updated_damages)'''

# 2 
# create dictionary for hurricanes with corresponding info
hurricanes = {}

for i in range(0, len(names)):
  hurricanes[names[i]] = {
    'Name': names[i],
    'Month': months[i],
    'Year': years[i],
    'Max Sustained Wind': max_sustained_winds[i],
    'Areas Affected': areas_affected[i],
    'Damage': updated_damages[i],
    'Deaths': deaths[i]
  }
'''print(hurricanes)'''

# 3
# organizing the hurricanes by year in new dictionary
new_cane_dict = {}
unique_years = list(dict.fromkeys(years))

# values are lists containing a dictionary for each hurricane occurred that year
for i in range(0, len(unique_years)):
  current_year = unique_years[i]
  new_cane_dict[current_year] = []
  for j in range(0, len(hurricanes)):
    if hurricanes[names[j]]['Year'] == current_year:
      new_cane_dict[current_year].append(hurricanes[names[j]])
'''print(new_cane_dict)'''

# 4
# counting how often each area have been affected by a hurricane
# create a list of unique areas affected by a hurricane
new_list_areas = []
for listed_areas in areas_affected:
  for area in listed_areas:
    new_list_areas.append(area)

unique_areas = list(dict.fromkeys(new_list_areas))

# create dictionary of areas to store how many times the areas were affected
area_count = {}
for area in unique_areas:
    count = new_list_areas.count(area)
    area_count[area] = count
'''print(area_count)'''

# 5 
# find area affected by the most hurricanes
max_key = max(area_count, key=area_count.get)
'''print(max_key)'''
# find the number of times the same area was hit by hurricanes
no_of_hurricanes = area_count['Central America']
'''print(no_of_hurricanes)'''

# 6
# find the deadliest hurricane
deadliest = max(hurricanes, key= lambda v: hurricanes[v]['Deaths'])
'''print(deadliest)'''
# find the number of deaths it caused
'''print(hurricanes[deadliest]['Deaths'])'''

# 7
# categorize hurricanes in new dictionary with mortality severity as key
mortality_scale = {0: 0, 
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
cane_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

# rating hurricanes by mortality
for i in range(0, len(hurricanes)):
  deaths = hurricanes[names[i]]['Deaths']
  if deaths == 0:
    cane_by_mortality[0].append(hurricanes[names[i]])
  elif 0 < deaths <= 100:
    cane_by_mortality[1].append(hurricanes[names[i]])
  elif 100 < deaths <= 500:
    cane_by_mortality[2].append(hurricanes[names[i]])
  elif 500 < deaths <= 1000:
    cane_by_mortality[3].append(hurricanes[names[i]])
  elif 1000 < deaths <= 10000:
    cane_by_mortality[4].append(hurricanes[names[i]])
  else:
    cane_by_mortality[5].append(hurricanes[names[i]])

'''print(cane_by_mortality)'''

# 8 
# find hurricane that caused greatest damage
# first assume one hurricane to be most costly
max_damage_cane = 'Cuba I'
max_damage = 0

# iterate through each hurricane to find most damage caused
for i in range(0, len(hurricanes)):
  value = hurricanes[names[i]]['Damage']
  if value == 'Damages not recorded':
    continue
  elif value > max_damage:
    max_damage = value
    max_damage_cane = list(hurricanes)[i]
  else:
    continue

'''print(max_damage_cane)
print(max_damage)'''

# 9
# rating hurricanes by damage caused
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage rating as key
cane_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

# categorize hurricanes by damage scale rating
for i in range(0, len(hurricanes)):
  damage = hurricanes[names[i]]['Damage']
  if damage == 'Damages not recorded':
    cane_by_damage[0].append(hurricanes[names[i]])
  elif float(damage) == 0:
    cane_by_damage[0].append(hurricanes[names[i]])
  elif 0 < float(damage) <= 100000000:
    cane_by_damage[1].append(hurricanes[names[i]])
  elif 100000000 < float(damage) <= 1000000000:
    cane_by_damage[2].append(hurricanes[names[i]])
  elif 1000000000 < float(damage) <= 10000000000:
    cane_by_damage[3].append(hurricanes[names[i]])
  elif 10000000000 < float(damage) <= 50000000000:
    cane_by_damage[4].append(hurricanes[names[i]])
  else:
    cane_by_damage[5].append(hurricanes[names[i]])

'''print(cane_by_damage)'''