import server

def main():
    server_app = server.Server()
    server_app.create_Server()
    server_app.receive_Connection()

    while(True):
        data = server_app.receive_Data()
        if not data: continue
        data = server_app.prime_Factors(data)
        server_app.send(data)


    server_app.close_Connection()

if __name__ == '__main__':
    main()