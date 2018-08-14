import client
import sys

def input_data(client):
    print("Please, enter number for factorization")
    print("For exit program, enter 'exit'")
    num = input()

    if num == "exit":
        client.close_Connection()
        print("Application was closed")
        raise SystemExit

    if not num:
        print("Please, enter correct number")
        input_data(client)
    else:
        client.send_Data(num)

    print(client.receive_Data())

def main():
    client__app = client.Client()
    client__app.connect()

    while(True):
        input_data(client__app)


if __name__ == '__main__':
    main()