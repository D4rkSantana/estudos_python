import sys
import pandas as pd

path = sys.argv[1]
dataf = pd.read_excel(path)
print(dataf)

nomes = dataf.loc[:, 'Nome']
numeros = dataf.loc[:, 'Numero']

