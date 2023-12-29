import requests
import matplotlib.pyplot as plt

def fetch_data_from_server():
    url = 'http://localhost:5000/send-data'  
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text  
        return data
    else:
        print("Falha ao buscar dados do servidor")
        return None

def plot_data(data):
    x = ['AcelX', 'AcelY', 'AcelZ']
    y = [10, 20, 15]  
    plt.bar(x, y)
    plt.xlabel('Eixos do Acelerômetro')
    plt.ylabel('Valores')
    plt.title('Dados do Acelerômetro')
    plt.show()

if __name__ == '__main__':
    fetched_data = fetch_data_from_server()
    if fetched_data:
        plot_data(fetched_data)
