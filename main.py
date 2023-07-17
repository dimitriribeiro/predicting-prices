import pandas as pd
from nomes_das_colunas import lista
dataset_carros = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data',
                             sep=',')

#tratamento dos dados
dataset_carros.columns = lista