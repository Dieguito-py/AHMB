import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data_file = pd.read_csv('dados.csv')
# print(data_file)

plt.figure( figsize=(10, 5))
data_file.head()
# sns.boxplot(data= data_file, x='yaxle', y='service');