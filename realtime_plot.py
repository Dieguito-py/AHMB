import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.DataFrame(columns=['Data_Hora', 'X', 'Y', 'Z'])

def update_plot(i):
    global df

    latest_data = pd.read_csv('dados.csv', names=['Data_Hora', 'X', 'Y', 'Z']).tail(1)
    
    df = pd.concat([df, latest_data], ignore_index=True)
    
    #calcualr média data/hora
    df['Data_Hora'] = pd.to_datetime(df['Data_Hora'])
    df = df.resample('10S', on='Data_Hora').mean().dropna().reset_index()

    plt.clf()
    
    plt.plot(df['Data_Hora'], df['X'], label='X')
    plt.plot(df['Data_Hora'], df['Y'], label='Y')
    plt.plot(df['Data_Hora'], df['Z'], label='Z')
    plt.title('Leituras do Acelerômetro')
    plt.xlabel('Data e Hora')
    plt.ylabel('Valor Normalizado')
    plt.legend()
    plt.grid(True)

ani = FuncAnimation(plt.gcf(), update_plot, interval=1000)

plt.show()
