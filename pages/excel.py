import pandas as pd

df = pd.read_excel(
       io='testPython.xlsx',
       engine='openpyxl',
       sheet_name='Test',
       skiprows=3,
       usecols='A:D'
       nrows=10,

)

print(df)