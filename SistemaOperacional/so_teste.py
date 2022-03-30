import platform
import getpass
from datetime import datetime

print("Nome Maquina........", platform.node())
print("Arquitetura.........", platform.architecture())
print("Sistema Operacional.", platform.system())
print("Versao do SO........", platform.release())
print("Processador.........", platform.processor())
print("Versao do Python....", platform.python_version())

print(datetime.now())

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha...")

if usuario == 'stephanie' and senha == 'hello':
    print("Bem vinda Stephanie")

else:
    print("Vocŵ não tem acesso")
