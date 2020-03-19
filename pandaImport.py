import pandas as pd

animais = ['Tiger', 'Bear', 'Moose']
pd.Series(animais)

numeros = [1, 2, 3]
pd.Series(numeros)

animais = ['Tiger', 'Bear', None]
pd.Series(animais)

numeros = [1, 2, None]
pd.Series(numeros)

import numpy as np
np.nan == None
