import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv', names=['Data_Hora', 'X', 'Y', 'Z'])

df['Data_Hora'] = pd.to_datetime(df['Data_Hora'])

plt.figure(figsize=(10, 6))
plt.plot(df['Data_Hora'], df['X'], label='X')
plt.plot(df['Data_Hora'], df['Y'], label='Y')
plt.plot(df['Data_Hora'], df['Z'], label='Z')
plt.title('Leituras do Acelerômetro')
plt.xlabel('Data e Hora')
plt.ylabel('Valor Normalizado')
plt.legend()
plt.grid(True)
plt.show()
