import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
plt.style.use('bmh')

tipo_processos = pd.read_csv("C:/Users/EquipeDev/Documents/processo_por_tipo.csv", encoding='latin1')
print(tipo_processos)

plt.figure(figsize=(14,8))
plt.barh(tipo_processos["Tipo"], tipo_processos["Quantidade"])
plt.ylabel("Tipo de processo")
plt.yticks(fontsize = 8)
plt.xlabel("Quantidade de termos")
plt.title('Quantidade de processos por tipo - 2022')
plt.show()

