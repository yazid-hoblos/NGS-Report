import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from pysnptools.snpreader import Bed

ped_file = 'TP_DATA_PROG/TP_DATA_PROG/II.a.Plink/hapmap.ped'
ped_data = pd.read_csv(ped_file, sep='\s+', header=None)

genotype_data = ped_data.iloc[:, 6:]  
# genotype_data = genotype_data.replace({0: genotype_data.mean(axis=0)}) 

# scaler = StandardScaler()
# genotype_data_scaled = scaler.fit_transform(genotype_data.fillna(0))  


# bed_file = 'TP_DATA_PROG/TP_DATA_PROG/II.a.Plink/IndMkMAFHWE.bed'
# bed = Bed(bed_file, count_A1=False)

# genotype_data = bed.read().val

# genotype_data = pd.DataFrame(genotype_data).replace(0, np.nan)
# genotype_data = genotype_data.fillna(0)

pca = PCA(n_components=2)  
pca_result = pca.fit_transform(genotype_data)

phe_file = 'TP_DATA_PROG/TP_DATA_PROG/II.a.Plink/hapmap.phe' #IndMkMAFHWE.fam hapmap.phe
phe_data = pd.read_csv(phe_file, sep='\s+', header=None)


phenotype = phe_data.iloc[:, 2].map({'CHB': 1, 'JPT': 0}).values
# phenotype = phe_data.iloc[:, 5].values

plt.figure(figsize=(8, 6))
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=phenotype, cmap='viridis')
# plt.colorbar(label='Disease Status (0=Control, 1=Case)')
plt.title('PCA of Genotype Data')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.savefig('PCA_ethnicity.png')

print("Explained variance ratio:", pca.explained_variance_ratio_)
