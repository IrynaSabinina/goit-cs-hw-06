import socket
import ast
from db.mongo import MongoDB

mongo = MongoDB()

def handle_data(data: str):
    try:
        msg = ast.literal_eval(data)
        saved = mongo.save_message(msg)
        print("Saved:", saved)

    except Exception as e:
        print("Error:", e)


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(5)

    print("Socket server running on 5000")

    while True:
        conn, addr = server.accept()
        data = conn.recv(1024).decode()
        handle_data(data)
        conn.close()


if __name__ == "__main__":
    run_server()