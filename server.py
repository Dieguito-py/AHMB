from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(__name__)

x_data, y_data, z_data = [], [], []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.data.decode('utf-8')
    if data:
        ax, ay, az = map(float, data.split(','))
        x_data.append(ax)
        y_data.append(ay)
        z_data.append(az)
        print(f"Received data: X={ax}, Y={ay}, Z={az}")
    return 'Data received'

@app.route('/plot')
def plot_data():
    plt.figure(figsize=(8, 6))
    plt.plot(x_data, label='X')
    plt.plot(y_data, label='Y')
    plt.plot(z_data, label='Z')
    plt.xlabel('Samples')
    plt.ylabel('Accelerometer Values')
    plt.legend()
    plt.title('MPU6050 Accelerometer Data')
    plt.savefig('static/plot.png')  # Salva o gráfico como um arquivo estático
    plt.close()
    return render_template('plot.html')

if __name__ == '__main__':
    app.run(debug=True)
