import server
import sys

def main():

    print sys.argv[1]
    print sys.argv[2]
    server_app = server.Server(host = sys.argv[1], port = int(sys.argv[2]))
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
