# Client-Server

This is a simple Client-Server application based on Python 3 socket .

# Features

  - You can send any number from 0 to maxInt, and find the prime number of this number

### Tech

This application uses *Socket* library from stantard python library

### Launching

Server-Client requires [Python](https://www.python.org/) v3.5+ to run.

Download archive and unpack it.

```sh
$ cd Server-Client
```

Primarily launch server application

```sh
$ cd  server
$ python -u server_app.py 127.0.0.1 14902
```
It is default host ip and port, if necessary you can change it.

After them, you can launch client application:

```sh
$ cd  client
$ python -u client_app.py 127.0.0.1 14902
```

### Using
After launching a client, you must see this strings:
```sh
$ Please, enter number for factorization
$ For exit program, enter 'exit'
```
Enter number from *2* to *python integer maxsize*:
```sh
$ 300
$ [2, 2, 3, 5, 5]
```
In order to close the application, you need enter exit command in you client apllication
```sh
$ exit
$ Application was closed
```
After closure application, you need laucnh server and client application every time.

### Docker
This application is very easy to install and deploy in a Docker container.

All you need build and launch prepared containers
Also you can change default ip and port by the editing docker-compose.yml

```sh
cd Server-Client
cd Docker-Version
```
Build containers
```sh
docker-compose --build server
docker-compose --build client
```

This will create the server and client image's and pull in the necessary dependencies.

Once done, run the Docker image's , in different console windows

Server
```sh
docker-compose --run server
```

Client
```sh
docker-compose --run client
```
###### ATTENTION!
In docker version of application, you need enter exit in quotation marks
```sh
"exit"
```

