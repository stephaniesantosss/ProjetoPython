from ftplib import *

ftp = FTP("ftp.ibiblio.org")
print(ftp.getwelcome())

usuario = input("Digite o usuario: ")

senha = input("Digite a senha: ")

ftp.login(usuario, senha)

print("Diretório atual do trabalho: ", ftp.pwd())

ftp.cwd('pub')

print("Diretorio corrente: ", ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()
