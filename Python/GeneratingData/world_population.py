import json
from pygal.style import RotateStyle
from pygal.maps.world import World



from country_codes import get_country_code

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population


# Group the countries in 4 populations levels.

cc_pops_1, cc_pops_2, cc_pops_3, cc_pops_4 = {}, {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 500000:
        cc_pops_1[cc] = pop
    elif pop < 20000000:
        cc_pops_2[cc] = pop
    elif pop < 1000000000:
        cc_pops_3[cc] = pop
    else:
        cc_pops_4[cc] = pop

# See how many contries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3), len(cc_pops_4))

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-5m', cc_pops_1)
wm.add('5m-20m', cc_pops_2)
wm.add('20m-1bn', cc_pops_3)
wm.add('>1bn', cc_pops_4)

wm.render_to_file('world_population.svg')
