import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def read_variants(file_path):
    with open(file_path, 'r') as file:
        variants = set(line.strip() for line in file)
    return variants

file1_variants = read_variants('TP_DATA_PROG/TP_DATA_PROG/II.a.Plink/geno_alpha')
file2_variants = read_variants('TP_DATA_PROG/TP_DATA_PROG/II.a.Plink/allelic_alpha')

venn2([file1_variants, file2_variants], set_labels=('Genotypic', 'Allelic'))

# Display the Venn diagram
plt.title("Venn Diagram of Variants")
plt.savefig('venn_diagram.png')
