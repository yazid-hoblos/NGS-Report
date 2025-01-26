import pandas as pd
import numpy as np


df = pd.read_csv('denovo_check.csv', sep=',', dtype=str, header=None)

d=[]
num_denovo = 0
for i in range(0, len(df)):
    f_gametes=[x for x in df.iloc[i, 1]]
    m_gametes=[x for x in df.iloc[i, 2]]
    allele1 = df.iloc[i, 0][0]
    allele2 = df.iloc[i, 0][1]
    if '.' in f_gametes or '.' in m_gametes or '.' in df.iloc[i, 0]:
        d.append('missing data')
        continue
    
    if allele1 not in f_gametes and allele1 not in m_gametes:
        d.append('denovo')
        print(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2])
        num_denovo += 1
    elif allele1 in f_gametes and allele1 not in m_gametes:
        if allele2 not in m_gametes:
            d.append('denovo')
            print(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2])
            num_denovo += 1
        else:
            d.append('not denovo')
    elif allele1 in m_gametes and allele1 not in f_gametes:
        if allele2 not in f_gametes:
            d.append('denovo')
            print(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2])
            num_denovo += 1
        else:
            d.append('not denovo')
    else:
        if allele2 not in f_gametes and allele2 not in m_gametes:
            d.append('denovo')
            print(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2])
            num_denovo += 1
        else:
            d.append('not denovo')
            

print('Number of de novo mutations:', num_denovo)
print('frequency of de novo mutations:', num_denovo/len(df))

#write d to a file with each element in a new line
# with open('denovo_check_results.txt', 'w') as f:
    # for item in d:
        # f.write("%s\n" % item)