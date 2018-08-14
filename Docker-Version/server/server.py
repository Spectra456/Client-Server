import socket
import pickle
import logging

logging.basicConfig(level=logging.INFO)

class Server():
    def __init__(self, host='localhost', port=14902, listeners=1):
        self._host = host
        self._port = port
        self._listeners = listeners
        self._socket = None
        self._connection = None

    def create_Server(self):
        """
        Creating server
        :return socket
        """
        self._socket = socket.socket()
        self._socket.bind((self._host, self._port))
        self._socket.listen(self._listeners)

        logging.info("Server was created with parameters {} and with {} listeners".format(self._socket, self._listeners))

    def receive_Connection(self):
        """
        Connecting to client
        """
        self._connection, address = self._socket.accept()

        logging.info("Connection established")
        logging.info("Client ip: {} port: {}".format(address[0], address[1]))

    def receive_Data(self):
        """
        Receive information from client(byte -> str)
        :return: return int information
        """

        data = self._connection.recv(4096)


        try:
           logging.info("Received data: {}".format(int(data)))
        except:
           logging.info("Received data is not correct: {}".format(data.decode()))
           self.send("Please, enter correct input")
           return

        if int(data) < 0 or int(data) == 0:
            self.send("Please, enter correct input")
            return

        return int(data)

    def prime_Factors(self, num):
        """
        Calculating prime factors of num from client
        :param num
        :return: list with prime factors
        """
        if num == 1: return 1
        i = 2
        prime_numbers = []
        while i * i <= num:
            while num % i == 0:
                prime_numbers.append(i)
                num = num / i
            i = i + 1
        if num > 1:
            prime_numbers.append(int(num))

        logging.info("Prime factors was been calculated: {}".format(prime_numbers))
        return prime_numbers

    def send(self, data):
        """
        Sending list from server to client
        """
        if not data:
            return
        self._connection.send(pickle.dumps(data))
        logging.info("{} |was been sended ".format(data))

    def close_Connection(self):
        """
        Closing connection with client
        """
        self._connection.close()
        logging.info("Connection was closed.")



