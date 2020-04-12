import json
with open('./india_states_UT_district.geojson') as f:
    data = json.load(f)
features = data['features']
for dist in features:
    # states = dist['properties']['ST_NM']
    distt = dist['properties']['DISTRICT']
    print(distt)

