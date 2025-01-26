import numpy as np
from statsmodels.stats.multitest import multipletests

# Read p-values from a file
filename = "TP_DATA_PROG/TP_DATA_PROG/ii.a.Plink/allelic"  # Replace with your file name
with open(filename, 'r') as file:
    p_values = [float(line.strip()) for line in file]

# Benjamini-Hochberg (FDR) correction
_, pvals_bh, _, _ = multipletests(p_values, alpha=0.05, method='fdr_bh')

# Holm-Bonferroni correction
_, pvals_holm, _, _ = multipletests(p_values, alpha=0.05, method='holm')

# Combine results into a list of tuples (original, BH, Holm)
corrected_pvalues = list(zip(p_values, pvals_bh, pvals_holm))

# Sort by the most significant (lowest corrected p-values)
corrected_pvalues.sort(key=lambda x: x[1])  # Sort by Benjamini-Hochberg corrected p-values

# Print the top 10 most significant p-values
print(f"{'Original':<12}{'BH Corrected':<20}{'Holm Corrected':<20}")
print("=" * 52)
for original, bh, holm in corrected_pvalues[:10]:
    print(f"{original:<12.4g}{bh:<20.4g}{holm:<20.4g}")
    
# Save the corrected p-values to a file
output_file = "corrected_pvalues_2.txt"
with open(output_file, 'w') as file:
    file.write("Original\tBH Corrected\tHolm Corrected\n")
    for original, bh, holm in corrected_pvalues:
        file.write(f"{original}\t{bh}\t{holm}\n")
