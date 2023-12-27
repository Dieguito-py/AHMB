from flask import Flask, request

app = Flask(__name__)

@app.route('/send-data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        print("Dados recebidos:", data)
        return "Dados recebidos com sucesso!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
