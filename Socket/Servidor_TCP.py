from socket import *

servidor = "127.0.0.1"  # localhost
porta = 43210  # porta definida pra criar o meu servidor

# AF_INET é tipo de identificação que eu vou ter com o servidor usando o ip ou hostname
# SOCK_STREAM utilizado pra usar o protocolo TCP
obj_socket = socket(AF_INET, SOCK_STREAM)

# bind seta o ip do servidor e a porta
obj_socket.bind((servidor, porta))

# com listen eu informo a qtde de usuarios que vão acessar meu servidor
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)

    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah Cliente'
        con.send(msg_enviada)
        break
        con.close()
