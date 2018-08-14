import socket
import pickle
import logging

logging.basicConfig(level=logging.INFO)

class Client():
    def __init__(self, host='localhost', port=14902):
        self._host = host
        self._port = port
        self._socket = None

    def connect(self):
        """
        Connection to server
        """
        self._socket = socket.socket()
        self._socket.connect((self._host, self._port))
        logging.info("Connection with server established:{}".format(self._socket))

    def send_Data(self, data):
        """
        Sending str(byte) to server
        :param data:
        """
        self._socket.send(data.encode())
        logging.info("{} | was been sended to server".format(data))

    def receive_Data(self):
        """
        Receiving data from server and unserialization
        :return: list with prime factors
        """
        data = pickle.loads(self._socket.recv(1024))

        logging.info("{} | was been received from server".format(data))
        return data

    def close_Connection(self):
        """
        Closing connection with server
        :return:
        """
        self._socket.close()
        logging.info("Connection was closed")


