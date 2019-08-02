import socket

host = str(input('IP: '))

print('Open Ports: ')
for porta in range(1, 65536):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    retorno = sock.connect_ex((host, porta))

    sock.close()

    if retorno == 0:
        print(porta)
