import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data into a DataFrame
column_names = (
    ["Family", "Individual", "Father", "Mother", "Sex", "Disease_Status"] +
    [f"SNP{i}_{allele}" for i in range(1, 7) for allele in ["A1", "A2"]]
)

data = pd.read_csv("TP_DATA_PROG/TP_DATA_PROG/I.b.Fbat/fam", sep='\s+', header=None, names=column_names)

# Melting the data for the allele columns to long format for easier plotting
allele_columns = [f"SNP{i}_A1" for i in range(1, 7)] + [f"SNP{i}_A2" for i in range(1, 7)]

# Melting the dataframe
data_melted = data.melt(id_vars=["Family", "Individual", "Disease_Status"], 
                        value_vars=allele_columns, 
                        var_name="SNP_Allele", 
                        value_name="Allele")

# Now split the 'SNP_Allele' into 'SNP' and 'Allele_Type' for better grouping
data_melted[['SNP', 'Allele_Type']] = data_melted['SNP_Allele'].str.split('_', expand=True)

# Plotting
plt.figure(figsize=(14, 10))

# Creating the barplot
sns.countplot(x="Disease_Status", hue="Allele_Type", data=data_melted, palette="Set1")

# Title and labels
plt.title("Distribution of Alleles by Disease Status for Each SNP", fontsize=16)
plt.xlabel("Disease Status", fontsize=14)
plt.ylabel("Allele Count", fontsize=14)

# Display plot
plt.legend(title='Allele Type')
plt.tight_layout()
plt.show()
