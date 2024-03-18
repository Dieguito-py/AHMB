import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")

dados.columns = ['tempo', 'xaxle', 'yaxle', 'zaxle', 'service']

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
sns.boxplot(x='service', y='xaxle', data=dados)
plt.xlabel('Service')
plt.ylabel('X Axle')
plt.title('X Axle')

plt.subplot(1, 3, 2)
sns.boxplot(x='service', y='yaxle', data=dados)
plt.xlabel('Service')
plt.ylabel('Y Axle')
plt.title('Y Axle')

plt.subplot(1, 3, 3)
sns.boxplot(x='service', y='zaxle', data=dados)
plt.xlabel('Service')
plt.ylabel('Z Axle')
plt.title('Z Axle')

plt.tight_layout()
plt.show()
