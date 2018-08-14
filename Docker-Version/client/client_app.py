import client
import sys
import time

def input_data(client):
    print("Please, enter number for factorization")
    print("For exit program, enter 'exit'")
    num = str(input())
    

    if num == "exit":
        client.close_Connection()
        print("Program was closed")
        raise SystemExit

    if not num:
        print("Please, enter correct number")
        input_data(client)
    else:
        client.send_Data(num)

    print(client.receive_Data())

def main():
    time.sleep(2)
    print sys.argv[1]
    print sys.argv[2]
    client__app = client.Client(host = sys.argv[1], port = int(sys.argv[2]))
    client__app.connect()

    while(True):
        input_data(client__app)


if __name__ == '__main__':
    main()
