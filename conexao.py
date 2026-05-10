import docker
from dotenv import load_dotenv

load_dotenv()

def criar_cliente():
    client = docker.from_env()
    client.ping()
    return client


def testar_conexao():
    try:
        client = criar_cliente()
        info = client.info()
        print(f"Conectado: {info['Name']} — Docker {info['ServerVersion']}")
        print(f"Containers: {info['Containers']} total, {info['ContainersRunning']} rodando")
        return client
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None


if __name__ == "__main__":
    testar_conexao()
