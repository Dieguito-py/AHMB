import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")

dados.columns = ['tempo', 'xaxle', 'yaxle', 'zaxle', 'service']

plt.figure(figsize=(10, 6))
sns.boxplot(x='service', y='xaxle', data=dados)
plt.xlabel('Service')
plt.ylabel('X Axle')
# plt.title('Boxplot de X Axle por Service')
plt.show()
