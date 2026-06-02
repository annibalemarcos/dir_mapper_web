"""DIR MAP Web — servidor local simples."""
import http.server
import os
import socket
import socketserver
import sys
import threading
import webbrowser

DEFAULT_PORT = 8765
APP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass


def find_free_port(preferred):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", preferred))
        s.close()
        return preferred
    except OSError:
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
        s.close()
        return port


def main():
    args = sys.argv[1:]
    open_browser = "--no-open" not in args
    args = [a for a in args if a != "--no-open"]
    port = int(args[0]) if args and args[0].isdigit() else DEFAULT_PORT
    port = find_free_port(port)
    if not os.path.isdir(APP_DIR):
        print(f"ERRO: pasta '{APP_DIR}' nao encontrada.")
        sys.exit(1)
    os.chdir(APP_DIR)
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", port), Handler)
    httpd.allow_reuse_address = True
    url = f"http://localhost:{port}"
    print("=" * 56)
    print(" DIR MAP Web — servidor local")
    print(f" Acesse: {url}")
    print(" Pressione Ctrl+C para encerrar.")
    print("=" * 56)
    if open_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrando...")
        httpd.shutdown()

if __name__ == "__main__":
    main()
