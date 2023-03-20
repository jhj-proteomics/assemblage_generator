import csv
import random
import pandas as pd

# Define the possible species values and their proportions
species_proportions = {'ovicaprine': 0.28, 'bos': 0.3, 'sus': 0.41}

# Calculate the number of rows for each species based on their proportions
num_rows_per_species = {species: round(proportion * 500) for species, proportion in species_proportions.items()}

# Define the possible bone values for each species
bone_values = {'ovicaprine': ['humerus', 'femur', 'tibia', 'radius', 'ulna', 'scapula', 'pelvis', 'skull', 'mandible', 'carpal', 'tarsal', 'metacarpal', 'metatarsal'],
               'bos': ['humerus', 'femur', 'tibia', 'radius', 'ulna', 'scapula', 'pelvis', 'skull', 'mandible', 'carpal', 'tarsal', 'metacarpal', 'metatarsal'],
               'sus': ['humerus', 'femur', 'tibia', 'radius', 'ulna', 'scapula', 'pelvis', 'skull', 'mandible', 'carpal', 'tarsal', 'metacarpal', 'metatarsal']}

# Generate a list of id numbers
id_values = random.sample(range(1, 1000), sum(num_rows_per_species.values()))

# Shuffle the id values to ensure they are randomly distributed
random.shuffle(id_values)

# Generate the data for each species
data = []
for species, num_rows in num_rows_per_species.items():
    bone_column = [random.choice(bone_values[species]) for _ in range(num_rows)]
    side_column = [random.choice(['r', 'l']) for _ in range(num_rows)]
    age_column = [random.randint(6, 56) if bone == 'mandible' else None for bone in bone_column]
    species_column = [species] * num_rows
    data += list(zip(id_values[:num_rows], species_column, bone_column, side_column, age_column))
    id_values = id_values[num_rows:]


# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['id', 'species', 'bone', 'side', 'age (months)'])

# Save the DataFrame to an Excel and a .csv file
df.to_excel('C:/Users/skl448/Desktop/python/scripts/assemblage_generator/test_assemblage.xlsx', index=False)
df.to_csv('C:/Users/skl448/Desktop/python/scripts/assemblage_generator/test_assemblage.csv', index=False)
