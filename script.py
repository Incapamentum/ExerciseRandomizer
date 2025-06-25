import json

with open("exercises/exercises.json", "r") as f:
    data_load = json.load(f)

exercise_group = data_load["Arms & Shoulders"]
calisthenics = exercise_group["Calisthenics"]

print(calisthenics)
print(f'Length of calisthenics: {len(calisthenics)}')

for i in calisthenics:
    name = i["name"]
    targets = i["targets"]
    sets = i["sets"]
    reps = i["reps"]

    print(f'{name} {targets} {sets} {reps}')