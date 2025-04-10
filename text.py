import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Gera HTML dinâmico usando Python
            html_content = """
            <!DOCTYPE html>
            <html lang="pt">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Exemplo Python e HTML</title>
            </head>
            <body>
                <h1>Olá, este conteúdo é gerado por Python!</h1>
                <p>Python está gerando este HTML no servidor e enviando para o navegador.</p>
            </body>
            </html>
            """
            # Envia o cabeçalho HTTP (código 200 significa que tudo está OK)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode())  # Envia o conteúdo HTML gerado
        else:
            super().do_GET()  # Para outras requisições, retorna o arquivo estático normal

# Cria o servidor HTTP
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    httpd.serve_forever()