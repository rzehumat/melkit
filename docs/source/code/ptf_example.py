'''
PTF files manipulation
'''

from melkit.ptf import PTF, compare_ptf

PATH_A = 'example_A.PTF'
PATH_B = 'example_B.PTF'
PATH_C = 'example_C.PTF'

# Create ptf objects
ptf_a = PTF(PATH_A)
ptf_b = PTF(PATH_B)
ptf_c = PTF(PATH_C)

# List columns in PTF file
cols = ptf_a.columns
print(cols)

# Load a subset of columns and convert it to pandas DataFrame
df = ptf_a.to_dataframe(cols[:5])
df.to_csv('ptf_a_col0to4.csv')

# Compare 2 variables between the PTF files:

## A) plot variables
compare_ptf([ptf_a, ptf_b, ptf_c],
            ['RN2-DFBBT-10-cls_7', 'RN2-DFBBT-10-cls_8'])

## B) plot variables and save them as PNG
compare_ptf([ptf_a, ptf_b, ptf_c],
            ['RN2-DFBBT-10-cls_7', 'RN2-DFBBT-10-cls_8'], save_dir='out')

## C) plot some variables from a single file
ptf_a.plot(['RN2-DFBBT-10-cls_7', 'RN2-DFBBT-10-cls_8'],
           output_path='out/RN2_cl78.png')