import requests
import matplotlib.pyplot as plt

def fetch_data_from_server():
    url = 'http://localhost/send-data' 
    response = requests.post(url)
    if response.status_code == 200:
        data = response.text
        return data
    else:
        print('Falha ao buscar dados do servidor')
        return None

def plot_data(data):
    if data:
        print('Resposta do servidor:', data)

        numeric_values = [val.strip() for val in data.split(',') if val.replace('.', '', 1).isdigit()]
        if numeric_values:
            values = [float(val) for val in numeric_values]
            plt.plot(values)
            plt.title('Dados do Acelerômetro')
            plt.xlabel('Amostras')
            plt.ylabel('Valores')
            plt.show()
        else:
            print('Nenhum dado numérico encontrado na resposta do servidor')
    else:
        print('Nenhum dado recebido do servidor')


if __name__ == '__main__':
    data_from_server = fetch_data_from_server()
    plot_data(data_from_server)
