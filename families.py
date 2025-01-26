import pandas as pd

# Load the data (replace 'linkage_data.ped' with your file path)
# Assuming tab-separated or space-separated data
data = pd.read_csv("TP_DATA_PROG/TP_DATA_PROG/I.b.Fbat/fam", sep="\t", header=None)

# Rename the columns for clarity (example for standard linkage format)
data.columns = ['Family_ID', 'Individual_ID', 'Father_ID', 'Mother_ID', 
                'Sex', 'Phenotype'] + [f'Marker_{i+1}' for i in range(len(data.columns) - 6)]

# Count the number of individuals per family
family_sizes = data.groupby('Family_ID')['Individual_ID'].count().reset_index()
family_sizes.columns = ['Family_ID', 'Num_Individuals']

# Save the family sizes to a CSV (optional)
# family_sizes.to_csv('family_sizes.csv', index=False)

# Print the total number of families and a sample of family sizes
print(f"Total families: {len(family_sizes)}")
print("Sample family sizes:")
print(family_sizes.head())

# Check families with the most and least individuals
max_family = family_sizes[family_sizes['Num_Individuals'] == family_sizes['Num_Individuals'].max()]
min_family = family_sizes[family_sizes['Num_Individuals'] == family_sizes['Num_Individuals'].min()]

print("\nFamily with the most individuals:")
print(max_family)

print("\nFamily with the least individuals:")
print(min_family)

print('number of families:', len(family_sizes))

#display families with more than 3 individuals
large_families = family_sizes[family_sizes['Num_Individuals'] == 5]
print(large_families)


# plot the distribution of family sizes
# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.figure(figsize=(10, 6))
# sns.histplot(family_sizes['Num_Individuals'], bins=range(1, 6), color='blue',edgecolor='black')
# plt.title('Distribution of Family Sizes')
# plt.xlabel('Number of Individuals')
# plt.ylabel('Frequency')
# # plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()