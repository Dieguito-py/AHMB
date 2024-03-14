from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
from urllib.parse import parse_qs
import threading

print("[1] Repousando\n[2] Digitando\n[3] Escrevendo\n")

atv = int(input("Atividade: "))
time = float(input("Tempo de atividade: "))

PORT = 80

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data_str = post_data.decode("utf-8")
        
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Salvar os dados 
        with open('dados.csv', 'a') as file:
            file.write(f'{date_time},{data_str},{atv}\n')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Dados recebidos com sucesso!", 'utf-8'))
        print(data_str)

def shutdown_server(server):
    print("Encerrando o servidor...")
    server.shutdown()

if __name__ == "__main__":
    try:
        server = HTTPServer(('0.0.0.0', PORT), RequestHandler)
        print(f'Servidor rodando na porta {PORT}')

        shutdown_timer = threading.Timer(time, shutdown_server, args=[server])
        shutdown_timer.start()

        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the server')
        server.socket.close()
