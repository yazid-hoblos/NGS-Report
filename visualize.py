import pandas as pd

# Load the data into a DataFrame
column_names = (
    ["Family", "Individual", "Father", "Mother", "Sex", "Disease_Status"] +
    [f"Marker{i}_{allele}" for i in range(1, 14) for allele in ["A1", "A2"]]
)

data = pd.read_csv("TP_DATA_PROG/TP_DATA_PROG/I.a.Paramlink/fam.txt", sep='\s+', header=None, names=column_names)


import matplotlib.pyplot as plt
import seaborn as sns

## Disease stutus distribution

# sns.countplot(x="Disease_Status", data=data)
# plt.title("Distribution of Disease Status")
# plt.show()

sns.countplot(x="Disease_Status", hue="Sex", data=data)
plt.title("Disease Status and Gender Distribution")
plt.legend(["Male", "Female"])
plt.savefig("disease.png")    

## Allele frequencies for each marker

# for i in range(1, 14):
#     marker_cols = [f"Marker{i}_A1", f"Marker{i}_A2"]
#     marker_data = data[marker_cols].melt(value_vars=marker_cols)
#     sns.countplot(x="value", data=marker_data)
#     plt.title(f"Allele Frequencies for Marker {i}")
#     plt.show()

## Allele frequencies for each marker in subplots

import matplotlib.pyplot as plt
import seaborn as sns


# Define the number of markers
num_markers = 13

# Create a grid of subplots
fig, axes = plt.subplots(4, 4, figsize=(15, 15))  # Adjust grid size as needed (4x4 for up to 16 markers)

# Flatten axes for easy iteration
axes = axes.flatten()

# Plot each marker in its respective subplot
for i in range(1, num_markers + 1):
    marker_cols = [f"Marker{i}_A1", f"Marker{i}_A2"]
    marker_data = data[marker_cols].melt(value_vars=marker_cols)
    sns.countplot(x="value", data=marker_data, ax=axes[i - 1])
    axes[i - 1].set_title(f"Marker {i}")
    axes[i - 1].set_xlabel("Allele")
    axes[i - 1].set_ylabel("Count")

# Remove any unused subplots if the grid size exceeds the number of markers
for j in range(num_markers, len(axes)):
    fig.delaxes(axes[j])

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig("subplots.png")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## Combine data for all markers into one DataFrame

# Combine data for all markers into one DataFrame
all_markers = []
for i in range(1, 14):
    marker_cols = [f"Marker{i}_A1", f"Marker{i}_A2"]
    marker_data = data[marker_cols].melt(value_vars=marker_cols, var_name="Marker", value_name="Allele")
    marker_data["Marker"] = f"Marker {i}"
    all_markers.append(marker_data)

# Concatenate all markers into a single DataFrame
combined_data = pd.concat(all_markers)

# Plot allele frequencies for all markers in a single grouped bar plot
plt.figure(figsize=(15, 8))
sns.countplot(x="Marker", hue="Allele", data=combined_data, palette="tab10")
plt.title("Allele Frequencies Across All Markers", fontsize=16)
plt.xlabel("Markers", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(title="Allele", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("grouped_barplot.png")


## Boxplot for all markers

# Select all marker columns
marker_columns = [col for col in data.columns if col.startswith("Marker")]

# Reshape the data for all markers
melted_data = data.melt(id_vars=["Disease_Status"], value_vars=marker_columns, 
                        var_name="Marker", value_name="Allele")

# Create a combined boxplot for all markers
plt.figure(figsize=(15, 8))
sns.boxplot(x="Marker", y="Allele", hue="Disease_Status", data=melted_data, palette="tab10")
plt.title("Allele Distribution Across All Markers by Disease Status", fontsize=16)
plt.xlabel("Markers", fontsize=14)
plt.ylabel("Allele", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(title="Disease Status", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("boxplot.png")


## Haplotype Heatmap

haplotype_data = data[[f"Marker{i}_A2" for i in range(1, 14)]].values
haplotype_df = pd.DataFrame(haplotype_data, columns=[f"Marker{i}_A2" for i in range(1, 14)])

haplotype_df.index = data['Individual']
haplotype_df = haplotype_df.sort_index()

plt.figure(figsize=(12, 8))
sns.heatmap(haplotype_df, cmap="viridis")
plt.title("Haplotype Heatmap")
plt.xlabel("Markers")
plt.ylabel("Individuals")
plt.savefig("plots/marker2.png")

# # Select allele 2 columns for all markers
haplotype_data = data[[f"Marker{i}_A1" for i in range(1, 14)]].values

# Convert to DataFrame to adjust index
haplotype_df = pd.DataFrame(haplotype_data, columns=[f"Marker{i}_A1" for i in range(1, 14)])

haplotype_df.index = data['Individual']
haplotype_df = haplotype_df.sort_index()
# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(haplotype_df, cmap="viridis")
plt.title("Haplotype Heatmap")
plt.xlabel("Markers")
plt.ylabel("Individuals")
plt.savefig("plots/marker1.png")


# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# # Select allele 2 columns for all markers
# haplotype_data = data[[f"Marker{i}_A2" for i in range(1, 14)]].values

# # Convert to DataFrame to adjust index
# haplotype_df = pd.DataFrame(haplotype_data, columns=[f"Marker{i}_A2" for i in range(1, 14)])

# # Add Disease Status to the DataFrame for row annotations
# haplotype_df['Disease_Status'] = data['Disease_Status']

# # Create a color map for disease status (can adjust colors if needed)
# disease_colors = haplotype_df['Disease_Status'].map({1: 'blue', 2: 'red', 0: 'gray'})

# haplotype_df.index = range(1, len(haplotype_df) + 1)

# # Plot the clustermap with disease status as row colors
# sns.clustermap(haplotype_df.drop(columns='Disease_Status'), 
#                cmap="viridis", 
#                row_colors=disease_colors,  # Highlight disease status with color
#                cbar_kws={'label': 'Allele Value'}, 
#                figsize=(12, 8))

# plt.title("Haplotype Clustermap with Disease Status Highlighting", fontsize=16)
# plt.show()


## Haplotype Clustermap

# Select allele 2 columns for all markers
haplotype_data = data[[f"Marker{i}_A1" for i in range(1, 14)]].values

# Convert to DataFrame to adjust index
haplotype_df = pd.DataFrame(haplotype_data, columns=[f"Marker{i}_A1" for i in range(1, 14)])

# Add Disease Status to the DataFrame for row annotations
haplotype_df['Disease_Status'] = data['Disease_Status']

# Create a color map for disease status (can adjust colors if needed)
disease_colors = haplotype_df['Disease_Status'].map({1: 'blue', 2: 'red', 0: 'gray'})

# Plot the clustermap with disease status as row colors
g=sns.clustermap(haplotype_df.drop(columns='Disease_Status'), 
               cmap="viridis", 
               row_colors=disease_colors,  # Highlight disease status with color
               cbar_kws={'label': 'Alleles'},
               figsize=(12, 8), col_cluster=False)


# g.fig.suptitle("Haplotype Clustermap with Disease Status", fontsize=16)
g.cax.set_position([0.02, 0.05, 0.05, 0.1])
plt.savefig("clustermap.png")


# Select allele 2 columns for all markers
haplotype_data = data[[f"Marker{i}_A2" for i in range(1, 14)]].values

# Convert to DataFrame to adjust index
haplotype_df = pd.DataFrame(haplotype_data, columns=[f"Marker{i}_A2" for i in range(1, 14)])

# Add Disease Status to the DataFrame for row annotations
haplotype_df['Disease_Status'] = data['Disease_Status']

# Create a color map for disease status (can adjust colors if needed)
disease_colors = haplotype_df['Disease_Status'].map({1: 'blue', 2: 'red', 0: 'gray'})

# Plot the clustermap with disease status as row colors
g=sns.clustermap(haplotype_df.drop(columns='Disease_Status'), 
               cmap="viridis", 
               row_colors=disease_colors,  # Highlight disease status with color
               cbar_kws={'label': 'Alleles'},
               figsize=(12, 8), col_cluster=False)

# g.fig.suptitle("Haplotype Clustermap with Disease Status", fontsize=16,ha='center')
g.cax.set_position([0.02, 0.05, 0.05, 0.1])

plt.savefig("clustermap2.png")