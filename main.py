from conexao import criar_cliente

def listar_container():
    cliente = criar_cliente()
    for container in cliente.containers.list():
        print(container.id, container.status, container.name, container.ports, container.health)


if __name__ == "__main__":
    listar_container()